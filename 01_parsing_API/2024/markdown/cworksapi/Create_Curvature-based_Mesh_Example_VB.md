---
title: "Create Curvature-based Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Curvature-based_Mesh_Example_VB.htm"
---

# Create Curvature-based Mesh Example (VBA)

This example shows how to create a curvature-based mesh for a part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified part exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part.
 ' 2. Creates a curvature-based mesh for study, Ready.
 ' 3. In SOLIDWORKS, click Ready, right-click Mesh
 '    in the Simulation study tree, and click Show Mesh.
 ' 4. Gets mesh connectivity data and node normal coordinates. Because the
 '    amount of data returned is large, the display code is commented out.
 '    Uncomment the display code or add break points to inspect the returned
 '    arrays in the Locals window.
 ' 5. Zoom in on the part and examine the mesh.
 ' 6. Examine the Immediate window.
 '
 ' NOTE: Because the part document is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Option Explicit
 Sub main()
     Dim swApp As SldWorks.SldWorks
     Dim COSMOSWORKS As Object
     Dim COSMOSObject As CosmosWorksLib.CwAddincallback
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CwMesh As CosmosWorksLib.CwMesh
     Dim errCode As Long
     Dim errors As Long
     Dim warnings As Long

    Const fileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\bikeframe.sldprt"
     Set swApp = Application.SldWorks
    Set COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg swApp, "No Simulation add-in"
     Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "No COSMOSWORKS object"
    swApp.OpenDoc6 fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_Silent, "", errors, warnings
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg swApp, "No active document"
    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg swApp, "No CWStudyManager object"
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg swApp, "No study"
     If (Study.Name <> "Ready") Then ErrorMsg swApp, "Wrong study"
     Debug.Print ("Name of study: " & Study.Name)
    Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg swApp, "No mesh"

     ' Set type of mesh to curvature-based
     CwMesh.MesherType = swsMesherTypeAlternate

     ' Set mesh parameters
     CwMesh.GrowthRatio = 1.6
     CwMesh.MinElementsInCircle = 8
     CwMesh.GetDefaultMaxAndMinElementSize swsLinearUnitMillimeters, 20, 4

    ' Create mesh
     errCode = Study.CreateMesh(swsLinearUnitMillimeters, 20, 1)
     Debug.Print "Error code: " & errCode '0 indicates successful creation of the mesh
     If errCode <> 0 Then ErrorMsg swApp, "Mesh failed; check error code"

    ' Get maximum and minimum element sizes used for boundaries
     Debug.Print "Maximum element size used for boundaries with lowest curvature: " & CwMesh.MaxElementSize
     Debug.Print "Minimum element size used for boundaries with highest curvature: " & CwMesh.MinElementSize

     Dim Var As Variant
     Dim Var1 As Variant
     Dim i As Long
     'Debug.Print "Mesh connectivity data"
     'Debug.Print "Number of nodes in connectivity unit, node numbers in connectivity unit"
     i = 0
     Var = CwMesh.GetConnectivity(errCode)
     'Do While i <= UBound(Var)
         'Debug.Print Var(i)
         'i = i + 1
     'Loop

    'Debug.Print "Mesh node normals"
     'Debug.Print "Node #, x-coord, y-coord, z-coord of node's normal vector"
     i = 0
     Var1 = CwMesh.GetNodeOutwardDirections(errCode)
     'Do While i <= UBound(Var1)
         'If 0 = i Mod 4 Then
             'Debug.Print "Node: " & Var1(i)
             'Debug.Print "  Normal vector (x, y, z coordinates):"
         'Else
             'Debug.Print "    " & Var1(i)
         'End If
         'i = i + 1
     'Loop

End Sub
 Sub ErrorMsg(swApp As SldWorks.SldWorks, Message As String)
     swApp.SendMsgToUser2 Message, 0, 0
     swApp.RecordLine "'*** WARNING - General"
     swApp.RecordLine "'*** " & Message
     swApp.RecordLine ""
 End Sub
```

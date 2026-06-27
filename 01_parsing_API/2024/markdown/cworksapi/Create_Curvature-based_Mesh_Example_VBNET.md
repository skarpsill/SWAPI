---
title: "Create Curvature-based Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Curvature-based_Mesh_Example_VBNET.htm"
---

# Create Curvature-based Mesh Example (VB.NET)

This example shows how to create a curvature-based mesh for a part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified part exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part document.
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
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports SolidWorks.Interop.cosworks

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim COSMOSWORKS As Object
         Dim COSMOSObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CwMesh As CwMesh
         Dim errCode As Integer
         Dim errors As Integer
         Dim warnings As Integer

         Const fileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\bikeframe.sldprt"

         COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "No Simulation add-in")
         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

         swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No study")
         If (Study.Name <> "Ready") Then ErrorMsg(swApp, "Wrong study")
         Debug.Print("Name of study: " & Study.Name)

         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(swApp, "No mesh")

         ' Set type of mesh to curvature-based
         CwMesh.MesherType = swsMesherType_e.swsMesherTypeAlternate

         ' Set mesh parameters
         CwMesh.GrowthRatio = 1.6
         CwMesh.MinElementsInCircle = 8
         CwMesh.GetDefaultMaxAndMinElementSize(swsLinearUnit_e.swsLinearUnitMillimeters, 20, 4)

         ' Create mesh
         errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, 20, 1)
         Debug.Print("Error code: " & errCode) '0 indicates successful creation of the mesh
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed; check error code")

         ' Get maximum and minimum element sizes used for boundaries
         Debug.Print("Maximum element size used for boundaries with lowest curvature: " & CwMesh.MaxElementSize)
         Debug.Print("Minimum element size used for boundaries with highest curvature: " & CwMesh.MinElementSize)

         Dim Var As Object
         Dim Var1 As Object
         'Dim i As Integer
         'Debug.Print("Mesh connectivity data")
         'Debug.Print("Number of nodes in connectivity unit, node numbers in connectivity unit")
         'i = 0
         Var = CwMesh.GetConnectivity(errCode)
         'Do While i <= UBound(Var)
            'Debug.Print(Var(i))
            'i = i + 1
         'Loop

         'Debug.Print("Mesh node normals")
         'Debug.Print("Node #, x-coord, y-coord, z-coord of node's normal vector")
         'i = 0
         Var1 = CwMesh.GetNodeOutwardDirections(errCode)
         'Do While i <= UBound(Var1)
            'if 0 = i Mod 4 Then
               'Debug.Print("Node: " & Var1(i))
               'Debug.Print("  Normal vector (x, y, z coordinates):")
            'Else
               'Debug.Print("    " & Var1(i))
            'End If
            'i = i + 1
         'Loop

     End Sub

     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String)
         swApp.SendMsgToUser2(Message, 0, 0)
         swApp.RecordLine("'*** WARNING - General")
         swApp.RecordLine("'*** " & Message)
         swApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End   Class
```

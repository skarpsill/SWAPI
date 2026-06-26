---
title: "Get Stress Tensor Values For Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Stress_Tensor_Values_for_Mesh_Example_VB.htm"
---

# Get Stress Tensor Values For Mesh Example (VBA)

This example shows how to get the stress tensor values for a mesh in a static study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation  version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Activates the Ready study.
 ' 2. Meshes and runs the study.
 ' 3. Gets the stress tensor values for all nodes of element 10 of the mesh.
 ' 4. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Option Explicit
 Sub main()
     Dim SwApp As SldWorks.SldWorks
     Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CWMesh As CosmosWorksLib.CWMesh
     Dim CWResult As CosmosWorksLib.CWResults
     Dim errCode As Long
     Dim el As Double, tl As Double
     Dim Stress As Variant
     Dim elem As Variant
     Dim i As Long

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks
     Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"

     'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No study manager object"
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No study object"

    'Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
     CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

     'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed"

     'Get results
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object"

    'Get two-dimensional array of stress tensor values at all nodes of element 10 of the mesh
     Stress = CWResult.GetStressTensorValuesForAllNodesOfElement(10, swsStrengthUnitPascal, 1, errCode)
     If errCode <> 0 Then
         ErrorMsg SwApp, "Error getting stress tensor values as defined in swsNodalResultsOfElementError_e: " & errCode
     Else
         For i = LBound(Stress) To UBound(Stress)
             elem = Stress(i)
             If i = 0 Then
                 Debug.Print "Stress tensor values for all nodes of element 10 of the mesh:"
                 Debug.Print ""
             Else
                 Debug.Print "==================================================="
             End If
             Debug.Print "Element index: " & elem(0)
             Debug.Print "Shell face (0=top, 1=bottom, -1=none): " & elem(1)
             Debug.Print "Node index: " & elem(2)
             Debug.Print "Stress tensor 1 (N/m**2): " & elem(3)
             Debug.Print "Stress tensor 2 (N/m**2): " & elem(4)
             Debug.Print "Stress tensor 3 (N/m**2): " & elem(5)
             Debug.Print "Stress tensor 4 (N/m**2): " & elem(6)
             Debug.Print "Stress tensor 5 (N/m**2): " & elem(7)
             Debug.Print "Stress tensor 6 (N/m**2): " & elem(8)
         Next i
     End If

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```

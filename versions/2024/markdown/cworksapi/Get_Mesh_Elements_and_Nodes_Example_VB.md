---
title: "Get Mesh Elements and Nodes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Mesh_Elements_and_Nodes_Example_VB.htm"
---

# Get Mesh Elements and Nodes Example (VBA)

This example shows how to get the elements and nodes of a solid mesh.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in
 '    (in SOLIDWORKS, click Tools > Add-ins > SOLIDWORKS Simulation).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference
 '    (in the IDE, click Tools > References > SOLIDWORKS
 '    Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Activates the Ready study.
 ' 2. Creates a solid mesh.
 ' 3. Gets the elements and nodes of the solid mesh.
 ' 4. Gets the elements and nodes at a depth of 0.001m in the solid mesh.
 ' 5. Runs the study.
 ' 6. Inspect the Immediate window.
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

    Dim errCode As Long
     Dim el As Double, tl As Double
     Dim num As Long
     Dim idList As Variant
     Dim normalNum As Variant
     Dim normalVec As Variant

    Set SwApp = Application.SldWorks
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

    'Get the elements of this solid mesh
     num = CWMesh.GetElementList(0, idList)
     Debug.Print "Number of elements in the mesh: " & num

    'Get the nodes of this solid mesh
     num = CWMesh.GetNodeList(0, idList)
     Debug.Print "Number of nodes in the mesh: " & num

    'Get the elements at a depth of 0.001m in this solid mesh
     num = CWMesh.GetSolidElementList(0.001, 2, idList)
     Debug.Print "Number of elements at a depth of 0.001m: " & num

     'Get the nodes at a depth of 0.001m in this solid mesh
     num = CWMesh.GetSolidNodeList(0.001, 2, idList)
     Debug.Print "Number of nodes at a depth of 0.001m: " & num

    'Get the nodes and normal vectors at the surface of this solid mesh
     num = CWMesh.GetSurfaceNodesAndNormals(idList, normalNum, normalVec)
     Debug.Print "Number of surface nodes: " & num

     'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```

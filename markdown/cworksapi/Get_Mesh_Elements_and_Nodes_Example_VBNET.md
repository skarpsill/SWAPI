---
title: "Get Mesh Elements and Nodes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Mesh_Elements_and_Nodes_Example_VBNET.htm"
---

# Get Mesh Elements and Nodes Example (VB.NET)

This example shows how to get the elements and nodes of a solid mesh.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
  '    (in the IDE, click Project > Add Reference > .NET >
  '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open public_documents\Simulation Examples\tutor1.sldprt.
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWAddinCallBack As CWAddinCallBack
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh

         Dim errCode As Integer
         Dim el As Double, tl As Double
         Dim num As Integer
         Dim idList As Object
         Dim normalNum As Object = Nothing
         Dim normalVec As Object = Nothing

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Get Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager object")
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No study object")

         'Mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No mesh object")
         CWMesh.Quality = 1
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         'Get the elements of this solid mesh
         num = CWMesh.GetElementList(0, idList)
         Debug.Print("Number of elements in the mesh: " & num)

         'Get the nodes of this solid mesh
         num = CWMesh.GetNodeList(0, idList)
         Debug.Print("Number of nodes in the mesh: " & num)

         'Get the elements at a depth of 0.001m in this solid mesh
         num = CWMesh.GetSolidElementList(0.001, 2, idList)
         Debug.Print("Number of elements at a depth of 0.001m: " & num)

         'Get the nodes at a depth of 0.001m in this solid mesh
         num = CWMesh.GetSolidNodeList(0.001, 2, idList)
         Debug.Print("Number of nodes at a depth of 0.001m: " & num)

         'Get the nodes and normal vectors at the surface of this solid mesh
         num = CWMesh.GetSurfaceNodesAndNormals(idList, normalNum, normalVec)
         Debug.Print("Number of surface nodes: " & num)

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: "  & errCode)

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

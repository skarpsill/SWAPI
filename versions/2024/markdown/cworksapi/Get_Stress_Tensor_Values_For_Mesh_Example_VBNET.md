---
title: "Get Stress Tensor Values For Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Stress_Tensor_Values_For_Mesh_Example_VBNET.htm"
---

# Get Stress Tensor Values For Mesh Example (VB.NET)

This example shows how to get the stress tensor values for a mesh in a static study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Activates the Ready static study.
 ' 2. Meshes and runs the study.
  ' 3. Gets the stress tensor values for all nodes of element 10 of the mesh.
 ' 4. Inspect the Immediate window.
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
         Dim CWResult As CWResults
         Dim errCode As Integer
         Dim el As Double, tl As Double
         Dim Stress As Object
         Dim elem As Object
         Dim i As Integer

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

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed")

         'Get results
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No result object")

         'Get two-dimensional array of stress tensor values at all nodes of element 10 of the mesh
         Stress = CWResult.GetStressTensorValuesForAllNodesOfElement(10, swsStrengthUnit_e.swsStrengthUnitPascal, 1, errCode)
         If errCode <> 0 Then
             ErrorMsg(swApp, "Error getting stress tensor values as defined in swsNodalResultsOfElementError_e: " & errCode)
         Else
             For i = LBound(Stress) To UBound(Stress)
                 elem = Stress(i)
                 If i = 0 Then
                     Debug.Print("Stress tensor values for all nodes of element 10 of the mesh:")
                     Debug.Print("")
                 Else
                     Debug.Print("===================================================")
                 End If
                 Debug.Print("Element index: " & elem(0))
                 Debug.Print("Shell face (0=top, 1=bottom, -1=none): " & elem(1))
                 Debug.Print("Node index: " & elem(2))
                 Debug.Print("Stress tensor 1 (N/m**2): " & elem(3))
                 Debug.Print("Stress tensor 2 (N/m**2): " & elem(4))
                 Debug.Print("Stress tensor 3 (N/m**2): " & elem(5))
                 Debug.Print("Stress tensor 4 (N/m**2): " & elem(6))
                 Debug.Print("Stress tensor 5 (N/m**2): " & elem(7))
                 Debug.Print("Stress tensor 6 (N/m**2): " & elem(8))
             Next i
         End If

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

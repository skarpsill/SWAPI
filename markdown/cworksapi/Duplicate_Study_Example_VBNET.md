---
title: "Duplicate Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Duplicate_Study_Example_VBNET.htm"
---

# Duplicate Study Example (VB.NET)

This example shows how to duplicate a simulation study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open  pubic_documents\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Duplicates the Ready study to create the DuplicateReady study.
 ' 2. Meshes and analyzes DuplicateReady.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

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

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack objectnd", True)
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object", True)

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document", True)

         'Get Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager object", True)
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No study object", True)

         'Duplicate study
         Study = StudyMngr.DuplicateStudy2("Ready", "DuplicateReady", "Default", 1, False, False, errCode)
         If Study Is Nothing Then ErrorMsg(swApp, "Study not duplicated", True)

         'Mesh the duplicate study
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No mesh object", False)
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed", True)

         'Run analysis on the duplicate study
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed", True)

         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No result object", False)

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End Class
```

---
title: "Duplicate Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Duplicate_Study_Example_VB.htm"
---

# Duplicate Study Example (VBA)

This example shows how to duplicate a simulation study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open pubic_documents\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Duplicates the Ready study to create the DuplicateReady study.
 ' 2. Meshes and analyzes DuplicateReady.
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

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object", True
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No Cosmosworks object", True

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document", True

    'Get Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No study manager object", True
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No study object", True

    'Duplicate study
     Set Study = StudyMngr.DuplicateStudy2("Ready", "DuplicateReady", "Default", 1, False, False, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Study not duplicated", True

    'Mesh the duplicate study
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object", False
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed", True
    'Run analysis on the duplicate study
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed", True

    Set CWResult = Study.results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object", False

End Sub
```

```
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String, EndTest As Boolean)
    SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""
End Sub
```

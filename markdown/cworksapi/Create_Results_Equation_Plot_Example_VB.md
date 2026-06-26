---
title: "Create Results Equation Plot Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Results_Equation_Plot_Example_VB.htm"
---

# Create Results Equation Plot Example (VBA)

This example shows how to create a results equation plot in a static study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Click View > Locals Window.
 ' 4. Add a breakpoint to the line that begins with "EqnResultMinMax = ".
 ' 5. Add a breakpoint to the line that begins with "EqnResultEntire = ".
 ' 6. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Activates Ready static study.
 ' 2. Meshes and runs the study.
 ' 3. Creates results equation plot, Equation1.
 ' 4. Press F8 to execute the current line.
 ' 5. Inspect local variable EqnResultMinMax to see the nodal minimum and maximum
 '    for Equation1 for the entire model.
 ' 6. Press F8 to execute the current line.
 ' 7. Inspect local variable EqnResultEntire to see the nodal results
 '    for Equation1 for the entire model.
 ' 8. Press F5 to complete the macro.
 ' 9. Inspect My Equation Plot in the graphics area.
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
     Dim PostPlot As CosmosWorksLib.CWPlot

    Dim errCode As Long
     Dim el As Double, tl As Double

    Dim sEqtn As String
     Dim sTitle As String

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object", True
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object", True

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document", True
    'Get Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No study manager object", True
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No study object", True
    'Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object", False
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed", True
    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed", True

    'Get results
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No results", False

    'Create results equation plot
     sEqtn = """P1: 1st Principal Stress"" + ""P2: 2nd Principal Stress"" + ""P3: 3rd Principal Stress"""
     sTitle = "My Equation Plot"

    Set PostPlot = CWResult.CreateResultsEquationPlot(sEqtn, sTitle, False, swsUnitSI, 1, swsShellFace_Top, errCode)

    Dim EqnResultMinMax     As Variant
     Dim EqnResultEntire     As Variant
     EqnResultMinMax = CWResult.GetMinMaxResultsEquationValues(sEqtn, False, 0, 1, 0, errCode)
     EqnResultEntire = CWResult.GetResultsEquationValuesForEntities(sEqtn, False, 0, 1, 0, Nothing, errCode)

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String, EndTest As Boolean)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```

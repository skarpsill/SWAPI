---
title: "Create Results Equation Plot Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Results_Equation_Plot_Example_VBNET.htm"
---

# Create Results Equation Plot Example (VB.NET)

This example shows how to create a results equation plot in a static study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Add a breakpoint to the line that begins with "EqnResultMinMax = ".
 ' 4. Add a breakpoint to the line that begins with "EqnResultEntire = ".
 ' 5. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Activates Ready static study.
 ' 2. Meshes and runs the study.
 ' 3. Creates results equation plot, Equation1.
 ' 4. Press F8 to execute the current line.
 ' 5. Click Debug > Windows > Locals.
 ' 6. Inspect local variable EqnResultMinMax to see the nodal minimum and maximum
 '    for Equation1 for the entire model.
 ' 7. Press F8 to execute the current line.
 ' 8. Inspect local variable EqnResultEntire to see the nodal results
 '    for Equation1 for the entire model.
 ' 9. Press F5 to complete the macro.
 '10. Inspect My Equation Plot in the graphics area.
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
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh
         Dim CWResult As CWResults
         Dim PostPlot As CWPlot

         Dim errCode As Integer
         Dim el As Double, tl As Double

         Dim sEqtn As String
         Dim sTitle As String

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object", True)
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

         'Mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No mesh object", False)
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed", True)

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed", True)

         'Get results
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No results", False)

         'Create results equation plot
         sEqtn = """P1: 1st Principal Stress"" + ""P2: 2nd Principal Stress"" + ""P3: 3rd Principal Stress"""
         sTitle = "My Equation Plot"

         PostPlot = CWResult.CreateResultsEquationPlot(sEqtn, sTitle, False, swsUnit_e.swsUnitSI, 1, swsShellFace_e.swsShellFace_Top, errCode)

         Dim EqnResultMinMax As Object
         Dim EqnResultEntire As Object
         EqnResultMinMax = CWResult.GetMinMaxResultsEquationValues(sEqtn, False, 0, 1, 0, errCode)
         EqnResultEntire = CWResult.GetResultsEquationValuesForEntities(sEqtn, False, 0, 1, 0, Nothing, errCode)

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)
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

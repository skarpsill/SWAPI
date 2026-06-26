---
title: "Create Trend Tracker Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Trend_Tracker_Example_VBNET.htm"
---

# Create Trend Tracker Example (VB.NET)

This example shows how to create a Trend Tracker for a static study.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Copy public_documents\samples\tutorial\api\tjoint.sldprt to another name and replace
 '    file_name in the code with the new name.
 '
 ' Postconditions:
 '  1. Opens the model document.
 '  2. Gets the static study.
 '  3. Meshes the model.
 '  4. Sets the solver type.
 '  5. Analyzes the study.
 '  6. Click Yes if asked to save the model.
 '  7. Adds Trend Tracker to the Simulation study tree.
 '  8. Sets the baseline of Trend Tracker to the current results.
 '  9. Deletes Pressure-1.
 ' 10. Meshes the model and analyzes the study.
 ' 11. Appends new results to Trend Tracker.
 ' 12. Inspect Trend Tracker (-Iteration 2-) to verify that the Simulation study
 '     tree contains:
 '     * Trend Journal
 '     * Mass1
 '     * Stress1
 '     * Displacement1
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim fileName As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim errCode As Integer
         Dim COSMOSWORKS As CosmosWorks
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim StaticOptions As CWStaticStudyOptions
         Dim trendTracker As CWTrendTracker
         Dim LARManager As CWLoadsAndRestraintsManager
         Dim CWFeatObj As CWMesh

         Const MeshEleSize As Double = 1.4769 'mm
         Const MeshTol As Double = 0.073847 'mm

         If SwApp Is Nothing Then Exit Sub

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\file_name.sldprt"
         Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, 1, "", errors, warnings)

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS

         ActDoc = COSMOSWORKS.ActiveDoc()

         StudyMngr = ActDoc.StudyManager()
         Study = StudyMngr.GetStudy(0)
         Study.ActivateConfiguration()
         StudyMngr.ActiveStudy = 0

         'Mesh
         CWFeatObj = Study.Mesh
         CWFeatObj.MesherType = 0
         CWFeatObj.Quality = 0
         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
         CWFeatObj = Nothing

         'Set solver type to FFEPlus
         StaticOptions = Study.StaticStudyOptions
         StaticOptions.SolverType = 2

         'Run analysis
         errCode = Study.RunAnalysis

         'Add Trend Tracker
         trendTracker = Study.CreateTrendTracker(errCode)

         'Set baseline of Trend Tracker to current results
         errCode = trendTracker.SetBaseLine

         'Delete a load
         LARManager = Study.LoadsAndRestraintsManager
         LARManager.DeleteLoadsAndRestraints("Pressure-1")

         Study.MeshAndRun()

         'Delete Trend Tracker
         'errCode = Study.DeleteTrendTracker

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

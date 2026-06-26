---
title: "Create Trend Tracker Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Trend_Tracker_Example_VB.htm"
---

# Create Trend Tracker Example (VBA)

This example shows how to create a Trend Tracker for a static study.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Copy public_documents\samples\tutorial\api\tjoint.sldprt to another name and replace
 '    file_name in the code with the new name.
 ' 4. Open the Immediate window.
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
Option Explicit
Sub main()
    Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim fileName        As String
     Dim errors          As Long
     Dim warnings        As Long
     Dim errCode         As Long
     Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc          As CosmosWorksLib.CWModelDoc
     Dim StudyMngr       As CosmosWorksLib.CWStudyManager
     Dim Study           As CosmosWorksLib.CWStudy
     Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
     Dim trendTracker    As CosmosWorksLib.CWTrendTracker
     Dim LARManager      As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim CWFeatObj       As CosmosWorksLib.CWMesh
    Const MeshEleSize       As Double = 1.4769 'mm
     Const MeshTol           As Double = 0.073847 'mm
    Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\file_name.sldprt"
     Set Part = SwApp.OpenDoc6(fileName, swDocPART, 1, "", errors, warnings)
    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    Set StudyMngr = ActDoc.StudyManager()
     Set Study = StudyMngr.GetStudy(0)
     Study.ActivateConfiguration
     StudyMngr.ActiveStudy = 0
    'Mesh
     Set CWFeatObj = Study.Mesh
     CWFeatObj.MesherType = 0
     CWFeatObj.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     Set CWFeatObj = Nothing
    'Set solver type to FFEPlus
     Set StaticOptions = Study.StaticStudyOptions
     StaticOptions.SolverType = 2
    'Run analysis
     errCode = Study.RunAnalysis

    'Add Trend Tracker
     Set trendTracker = Study.CreateTrendTracker(errCode)

    'Set baseline of Trend Tracker to current results
     errCode = trendTracker.SetBaseLine

    'Delete a load
     Set LARManager = Study.LoadsAndRestraintsManager
     LARManager.DeleteLoadsAndRestraints ("Pressure-1")
    Study.MeshAndRun
    'Delete Trend Tracker
     'errCode = Study.DeleteTrendTracker

End Sub
```

---
title: "Run Studies in Batch Mode Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Run_Studies_in_Batch_Mode_Example_VB.htm"
---

# Run Studies in Batch Mode Example (VBA)

This example shows how to run studies in batch mode.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model document.
 ' 2. Sets the run and mesh option for the studies in the batch.
 ' 3. Analyzes the studies in the batch.
 ' 4. Gets the result codes of the studies.
 ' 5. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Option Explicit
Dim swApp           As SldWorks.SldWorks
 Dim Part            As SldWorks.ModelDoc2
 Dim fileName        As String
 Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc          As CosmosWorksLib.CWModelDoc
 Dim StudyMngr       As CosmosWorksLib.CWStudyManager
 Dim RunStudyResults As CosmosWorksLib.CWRunStudiesResults
 Dim RunStudyOptions As CosmosWorksLib.CWRunSpecStudiesRunMeshOptions
 Dim errCode         As Long
 Dim studyName       As String
 Dim result          As Long
 Dim errors          As Long
 Dim warnings        As Long
Sub main()

    Set swApp = Application.SldWorks

    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
     Set Part = swApp.OpenDoc6(fileName, swDocPART, 1, "", errors, warnings)

    Set CWAddinCallBack = swApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     Set StudyMngr = ActDoc.StudyManager()

    Set RunStudyOptions = StudyMngr.RunSpecifiedStudyOptions()
     errCode = RunStudyOptions.AddStudyOption("Partial", swsRunStudiesRunMeshOptions_MeshAndRun)
     errCode = RunStudyOptions.AddStudyOption("Ready - 8 plies", swsRunStudiesRunMeshOptions_MeshAndRun)

    Set RunStudyResults = StudyMngr.RunSpecifiedStudyByName(errCode)

    errCode = RunStudyResults.GetFirstItem(studyName, result)
     Debug.Print "First study in batch: " & studyName
     Debug.Print "  Result code as defined in swsRunStudiesResultsErrorCode_e: " & result

    errCode = RunStudyResults.GetNextItem(studyName, result)
     Debug.Print "Next study in batch: " & studyName
     Debug.Print "  Result code as defined in swsRunStudiesResultsErrorCode_e: " & result
End Sub
```

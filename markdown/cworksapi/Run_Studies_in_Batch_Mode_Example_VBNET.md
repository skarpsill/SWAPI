---
title: "Run Studies in Batch Mode Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Run_Studies_in_Batch_Mode_Example_VBNET.htm"
---

# Run Studies in Batch Mode Example (VB.NET)

This example shows how to run studies in batch mode.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim fileName As String
     Dim COSMOSWORKS As COSMOSWORKS
     Dim CWAddinCallBack As CWAddinCallBack
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim RunStudyResults As CWRunStudiesResults
     Dim RunStudyOptions As CWRunSpecStudiesRunMeshOptions
     Dim errCode As Integer
     Dim studyName As String
     Dim result As Integer
     Dim errors As Integer
     Dim warnings As Integer

     Sub main()

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
         Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, 1, "", errors, warnings)

         CWAddinCallBack = swApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         ActDoc = COSMOSWORKS.ActiveDoc()
         StudyMngr = ActDoc.StudyManager()

         RunStudyOptions = StudyMngr.RunSpecifiedStudyOptions()
         errCode = RunStudyOptions.AddStudyOption("Partial", swsRunStudiesRunMeshOptions_e.swsRunStudiesRunMeshOptions_MeshAndRun)
         errCode = RunStudyOptions.AddStudyOption("Ready - 8 plies", swsRunStudiesRunMeshOptions_e.swsRunStudiesRunMeshOptions_MeshAndRun)

         RunStudyResults = StudyMngr.RunSpecifiedStudyByName(errCode)

         errCode = RunStudyResults.GetFirstItem(studyName, result)
         Debug.Print("First study in batch: " & studyName)
         Debug.Print("  Result code as defined in swsRunStudiesResultsErrorCode_e: " & result)

         errCode = RunStudyResults.GetNextItem(studyName, result)
         Debug.Print("Next study in batch: " & studyName)
         Debug.Print("  Result code as defined in swsRunStudiesResultsErrorCode_e: " & result)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

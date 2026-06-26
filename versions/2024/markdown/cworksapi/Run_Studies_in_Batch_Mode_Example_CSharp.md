---
title: "Run Studies in Batch Mode Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Run_Studies_in_Batch_Mode_Example_CSharp.htm"
---

# Run Studies in Batch Mode Example (C#)

This example shows how to run studies in batch mode.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the model document.
  // 2. Sets the run and mesh option for the studies in the batch.
 // 3. Analyzes the studies in the batch.
 // 4. Gets the result codes of the studies.
 // 5. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace RunBatchStudies_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         string fileName;
         CosmosWorks COSMOSWORKS;
         CwAddincallback CWAddinCallBack;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWRunStudiesResults RunStudyResults;
         CWRunSpecStudiesRunMeshOptions RunStudyOptions;
         int errCode;
         string studyName;
         int result;
         int errors;
         int warnings;

         public void Main()
         {
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\tjoint.sldprt";
             Part = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, 1, "", ref errors, ref warnings);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             ActDoc = COSMOSWORKS.ActiveDoc;
             StudyMngr = ActDoc.StudyManager;

             RunStudyOptions = StudyMngr.RunSpecifiedStudyOptions;
             errCode = RunStudyOptions.AddStudyOption("Partial", (int)swsRunStudiesRunMeshOptions_e.swsRunStudiesRunMeshOptions_MeshAndRun);
             errCode = RunStudyOptions.AddStudyOption("Ready - 8 plies", (int)swsRunStudiesRunMeshOptions_e.swsRunStudiesRunMeshOptions_MeshAndRun);

             RunStudyResults = StudyMngr.RunSpecifiedStudyByName(out errCode);

             errCode = RunStudyResults.GetFirstItem(out studyName, out result);
             Debug.Print("First study in batch: " + studyName);
             Debug.Print("  Result code as defined in swsRunStudiesResultsErrorCode_e: " + result);

             errCode = RunStudyResults.GetNextItem(out studyName, out result);
             Debug.Print("Next study in batch: " + studyName);
             Debug.Print("  Result code as defined in swsRunStudiesResultsErrorCode_e: " + result);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```

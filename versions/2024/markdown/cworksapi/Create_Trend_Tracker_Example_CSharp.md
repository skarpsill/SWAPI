---
title: "Create Trend Tracker Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Trend_Tracker_Example_CSharp.htm"
---

# Create Trend Tracker Example (C#)

This example shows how to create a Trend Tracker for a static study.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Copy public_documents\samples\tutorial\api\tjoint.sldprt to another name and replace
 //    file_name in the code with the new name.
 //
 // Postconditions:
 //  1. Opens the model document.
 //  2. Gets the static study.
 //  3. Meshes the model.
 //  4. Sets the solver type.
 //  5. Analyzes the study.
 //  6. Click Yes if asked to save the model.
 //  7. Adds Trend Tracker to the Simulation study tree.
 //  8. Sets the baseline of Trend Tracker to the current results.
 //  9. Deletes Pressure-1.
 // 10. Meshes the model and analyzes the study.
 // 11. Appends new results to Trend Tracker.
 // 12. Inspect Trend Tracker (-Iteration 2-) to verify that the Simulation study
 //     tree contains:
 //     * Trend Journal
 //     * Mass1
 //     * Stress1
 //     * Displacement1
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
 namespace CreateTrendTracker_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             string fileName = null;
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWStaticStudyOptions StaticOptions = default(CWStaticStudyOptions);
             CWTrendTracker trendTracker = default(CWTrendTracker);
             CWLoadsAndRestraintsManager LARManager = default(CWLoadsAndRestraintsManager);
             CWMesh CWFeatObj = default(CWMesh);

             const double MeshEleSize = 1.4769; //mm
             const double MeshTol = 0.073847; //mm

             if (swApp == null)
                 return;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\file_name.sldprt";
             Part = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, 1, "", ref errors, ref warnings);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;

             ActDoc = COSMOSWORKS.ActiveDoc;

             StudyMngr = ActDoc.StudyManager;
             Study = StudyMngr.GetStudy(0);
             Study.ActivateConfiguration();
             StudyMngr.ActiveStudy = 0;

             //Mesh
             CWFeatObj = Study.Mesh;
             CWFeatObj.MesherType = 0;
             CWFeatObj.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);
             CWFeatObj = null;

             //Set solver type to FFEPlus
             StaticOptions = Study.StaticStudyOptions;
             StaticOptions.SolverType = 2;

             //Run analysis
             errCode = Study.RunAnalysis();

             //Add Trend Tracker
             trendTracker = Study.CreateTrendTracker(out errCode);

             //Set baseline of Trend Tracker to current results
             errCode = trendTracker.SetBaseLine();

             //Delete a load
             LARManager = Study.LoadsAndRestraintsManager;
             LARManager.DeleteLoadsAndRestraints("Pressure-1");

             Study.MeshAndRun();

             //Delete Trend Tracker
             //errCode = Study.DeleteTrendTracker

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```

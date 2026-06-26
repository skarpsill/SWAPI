---
title: "Create Results Equation Plot Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Results_Equation_Plot_Example_CSharp.htm"
---

# Create Results Equation Plot Example (C#)

This example shows how to create a results equation plot in a static study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Add a breakpoint to the line that begins with "EqnResultMinMax = ".
 // 4. Add a breakpoint to the line that begins with "EqnResultEntire = ".
 // 5. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 //
 // Postconditions:
 // 1. Activates Ready static study.
 // 2. Meshes and runs the study.
 // 3. Creates results equation plot, Equation1.
 // 4. Press F8 to execute the current line.
 // 5. Click Debug > Windows > Locals.
 // 6. Inspect local variable EqnResultMinMax to see the nodal minimum and maximum
 //    for Equation1 for the entire model.
 // 7. Press F8 to execute the current line.
 // 8. Inspect local variable EqnResultEntire to see the nodal results
 //    for Equation1 for the entire model.
 // 9. Press F5 to complete the macro.
 //10. Inspect My Equation Plot in the graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using SolidWorks.Interop.cosworks;
 namespace CreateResultsEquationPlot_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CWMesh = default(CWMesh);
             CWResults CWResult = default(CWResults);
             CWPlot PostPlot = default(CWPlot);

             string sEqtn;
             string sTitle;
             int errCode = 0;
             double el = 0;
             double tl = 0;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CWAddinCallBack object", true);
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object", true);

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document", true);

             //Get Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager object", true);
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "Study not created", true);

             //Mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object", false);
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed", true);

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed", true);

             //Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object", false);

             //Create results equation plot
             sEqtn = "\"P1: 1st Principal Stress\" + \"P2: 2nd Principal Stress\" + \"P3: 3rd Principal Stress\"";
             sTitle = "My Equation Plot";

             PostPlot = CWResult.CreateResultsEquationPlot(sEqtn, sTitle, false, (int)swsUnit_e.swsUnitSI, 1, (int)swsShellFace_e.swsShellFace_Top, out errCode);

             object EqnResultMinMax = null;
             object EqnResultEntire = null;
             EqnResultMinMax = CWResult.GetMinMaxResultsEquationValues(sEqtn, false, 0, 1, 0, out errCode);
             EqnResultEntire = CWResult.GetResultsEquationValuesForEntities(sEqtn, false, 0, 1, 0, null, out errCode);

         }

         public void ErrorMsg(SldWorks SwApp, string Message, bool EndTest)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }
 }
```

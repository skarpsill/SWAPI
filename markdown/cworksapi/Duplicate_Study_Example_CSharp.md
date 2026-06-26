---
title: "Duplicate Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Duplicate_Study_Example_CSharp.htm"
---

# Duplicate Study Example (C#)

This example shows how to duplicate a simulation study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open  pubic_documents\Simulation Examples\tutor1.sldprt.
 //
 // Postconditions:
 // 1. Duplicates the Ready study to create the DuplicateReady study.
 // 2. Meshes and analyzes DuplicateReady.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------
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
 namespace DuplicateSimStudy_CSharp.csproj
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
                 ErrorMsg(swApp, "No study object", true);

             //Duplicate study
             Study = StudyMngr.DuplicateStudy2("Ready", "DuplicateReady", "Default", 1, false, false, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Study not duplicated", true);

             //Mesh the duplicate study
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object", false);
             CWMesh.Quality = 0;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed", true);

             //Run analysis on the duplicate study
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed", true);

             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object", false);

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

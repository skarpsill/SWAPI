---
title: "Set Composite Shell Options Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Set_Composite_Shell_Options_Example_CSharp.htm"
---

# Set Composite Shell Options Example (C#)

This example shows how to set composite shell options.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Verify that the specified material library exists.
  // 4. Verify that the specified model document exists.
 //
 // Postconditions:
 // 1. Opens the model.
 // 2. Activates Ready - 8 plies.
 // 3. Sets composite shell options.
 // 4. Meshes the model.
 // 5. Analyzes the study.
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
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         CosmosWorks COSMOSWORKS;
         CwAddincallback COSMOSObject;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWShell Shell;
         CWMesh Mesh;
         CWStaticStudyOptions StaticOptions;
         ModelDoc2 Part;
         CWShellManager ShellMgr;
         CWCompositeShellOptions CWShellOptions;
         int m;
         int errCode;
         int longstatus;
         int longwarnings;
         int bApp;
         int j;
         const double MeshEleSize = 1.4769;
         const double MeshTol = 0.073847;

         public void Main()
         {
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "Simulation add-in not loaded");
             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2022\\Simulation Examples\\Composites\\tjoint.SLDPRT", (int)swDocumentTypes_e.swDocPART, 2, "", ref longstatus, ref longwarnings);
             if (Part == null)
                 ErrorMsg(swApp, "Failed to open tjoint.SLDPRT");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager");
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(1);

             ShellMgr = Study.ShellManager;
             if (ShellMgr == null)
                 ErrorMsg(swApp, "No shell manager");

             Shell = ShellMgr.GetShellAt(0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "No shell");

             Shell.ShellBeginEdit();
             bApp = Shell.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Alloy Steel");
             Shell.Formulation = 2;

             CWShellOptions = Shell.CompositeOptions;
             if (CWShellOptions == null)
                 ErrorMsg(swApp, "No composite shell options");

             CWShellOptions.RotateZeroDegreeReference2 = 0;
             CWShellOptions.MappingType = 0;
             CWShellOptions.Symmetric2 = 0;
             CWShellOptions.Sandwich2 = 0;
             CWShellOptions.PlyRelativeAngle2 = 0;
             CWShellOptions.LengthUnit = 4;
             CWShellOptions.AllPliesSameMaterial2 = -1;

             m = CWShellOptions.GetTotalPlies();
             for (j = 0; j <= m - 1; j++)
             {
                 errCode = CWShellOptions.SetPlyParameters2(j + 1, 0.1 * (j + 1), 0.05 * j, "solidworks materials", "Cast Stainless Steel");
             }

             Shell.ShellEndEdit();

             //Mesh
             Mesh = Study.Mesh;
             Mesh.MesherType = 0;
             Mesh.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);

             StaticOptions = Study.StaticStudyOptions;
             StaticOptions.SolverType = 2;

             //Run analysis
             errCode = Study.RunAnalysis();

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```

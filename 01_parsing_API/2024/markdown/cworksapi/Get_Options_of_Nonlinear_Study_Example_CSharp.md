---
title: "Get Options of Nonlinear Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Options_of_Nonlinear_Study_Example_CSharp.htm"
---

# Get Options of Nonlinear Study Example (C#)

This example shows how to get the properties of nonlinear studies.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified file exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
  // 1. Gets the properties of each nonlinear study.
  // 2. Modifies the step/tolerance options in each nonlinear study.
  // 3. Prints the properties of each nonlinear study in the model to the
 //    Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes.
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
 namespace GetNLOptions_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         CwAddincallback swAddin;
         CosmosWorks ssApp;
         CWModelDoc ssModelDoc;
         CWStudyManager ssStudyMgr;
         CWStudy ssStudy;
         CWNonLinearStudyOptions ssNonLinearStudyOptions;
         string docName;
         int errors;
         int warnings;
         int studyCnt;
         string studyName;
         int studyType;
         int i;
         double maxLoad;
         double maxDisplacement;
         int unit;
         int maxArcSteps;
         double arcLengthMultiplier;
         int displacementComponent;
         object selectedEntity;
         int frequency;
         int maximum;
         double convergence;
         double tolerance;
         double factor;
         Entity swEntity;
         int entityType;
         string selEntityType;

         public void Main()
         {
             docName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Nonlinear\\nl_plate.sldprt";
             swApp.OpenDoc6(docName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             swAddin = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             ssApp = swAddin.CosmosWorks;
             ssModelDoc = ssApp.ActiveDoc;
             ssStudyMgr = ssModelDoc.StudyManager;

             studyCnt = ssStudyMgr.StudyCount;
             for (i = 0; i <= studyCnt - 1; i++)
             {
                 ssStudy = ssStudyMgr.GetStudy(i);
                 studyName = ssStudy.Name;
                 Debug.Print("");
                 Debug.Print("Study name: " + studyName);
                 studyType = ssStudy.AnalysisType;
                 if ((studyType == (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear))
                 {
                     ssNonLinearStudyOptions = ssStudy.NonLinearStudyOptions;
                     Debug.Print("  Nonlinear study subtype as defined in swsNonlinearAnalysisSubType_e: " + ssStudy.NonlinearAnalysisSubType);
                     Debug.Print("    Solution properties:");
                     Debug.Print("       Stepping options:");
                     Debug.Print("          Start time: " + ssNonLinearStudyOptions.StartTime);
                     Debug.Print("          End time: " + ssNonLinearStudyOptions.EndTime);
                     Debug.Print("          Save data for restarting analysis? (1=yes, 0=no) " + ssNonLinearStudyOptions.SaveDataForRestartingAnalysis);
                     Debug.Print("          Solution-time increment: " + ssNonLinearStudyOptions.TimeIncrement);
                     Debug.Print("          Fixed-time increment: " + ssNonLinearStudyOptions.FixedTimeIncrement);
                     Debug.Print("       Geometry nonlinearity options:");
                     Debug.Print("          Use large displacement formulation? (1=yes, 0=no) " + ssNonLinearStudyOptions.UseLargeDisplacement);
                     Debug.Print("          Update direction of load at every solution step with deflection? (1=yes, 0=no) " + ssNonLinearStudyOptions.UseUpdateLoadDirection);
                     Debug.Print("          Use large strain formulation? (1=yes, 0=no) " + ssNonLinearStudyOptions.UseLargeStrain);
                     Debug.Print("          Keep bolt pre-stress? (1=yes, 0=no) " + ssNonLinearStudyOptions.KeepBoltPreStress);
                     Debug.Print("       Solver type as defined in swsSolverType_e: " + ssNonLinearStudyOptions.SolverType);
                     Debug.Print("       Results folder path: " + ssNonLinearStudyOptions.ResultFolderPath);

                     Debug.Print("    Advanced properties:");
                     Debug.Print("       Methods:");
                     Debug.Print("          Control type as defined in swsNonLinearOptionControlMethodType_e: " + ssNonLinearStudyOptions.ControlMethodType);
                     Debug.Print("          Integration type as defined in swsNonLinearOptionIntegrationMethodType_e: " + ssNonLinearStudyOptions.IntegrationMethodType);
                     Debug.Print("          Iterative type as defined in swsNonLinearOptionIterativeMethodType_e: " + ssNonLinearStudyOptions.IterativeMethodType);

                     Debug.Print("       Displacement control options:");
                     selEntityType = "Nothing";
                     ssNonLinearStudyOptions.GetDisplacementControlOptions2(out displacementComponent, out unit, out selectedEntity);
                     if ((selectedEntity != null))
                     {
                         swEntity = (Entity)selectedEntity;
                         entityType = swEntity.GetType();
                         switch (entityType)
                         {
                             case 3:
                                 selEntityType = "vertex";
                                 break;
                             case 6:
                                 selEntityType = "reference point";
                                 break;
                             case 0:
                                 selEntityType = "Nothing";
                                 break;
                         }
                     }
                     Debug.Print("          Displacement component as defined in swsDisplacementComponent_e: " + displacementComponent);
                     Debug.Print("          Units as defined in swsLinearUnit_e: " + unit);
                     Debug.Print("          Selected reference entity type: " + selEntityType);

                     ssNonLinearStudyOptions.GetArcLengthCompletionOptions(out maxLoad, out maxDisplacement, out unit, out maxArcSteps, out arcLengthMultiplier);
                     Debug.Print("       Arc-Length completion options:");
                     Debug.Print("          Maximum load-pattern multiplier: " + maxLoad);
                     Debug.Print("          Maximum displacement: " + maxDisplacement);
                     Debug.Print("          Units as defined in swsLinearUnit_e: " + unit);
                     Debug.Print("          Maximum number of arc steps: " + maxArcSteps);
                     Debug.Print("          Initial arc length multiplier: " + arcLengthMultiplier);
                     Debug.Print("       Step/Tolerance options:");
                     ssNonLinearStudyOptions.GetStepToleranceOptions(out frequency, out maximum, out convergence, out tolerance, out factor);
                     Debug.Print("          Tolerance: ");
                     Debug.Print("              Frequency of performing equilibrium in number of solution steps: " + frequency);
                     Debug.Print("              Maximum number of equilibrium iterations for any solution step: " + maximum);
                     Debug.Print("              Relative displacement tolerance used for equilibrium convergence: " + convergence);
                     Debug.Print("              Tolerance for strain increment for models with creep or plasticity: " + tolerance);
                     Debug.Print("              Stiffness singularity elimination factor: " + factor);
                     long status = 0;
                     status = ssNonLinearStudyOptions.SetStepToleranceOptions(-1, 10, 0.002, 0.02, 1);
                     ssNonLinearStudyOptions.GetStepToleranceOptions(out frequency, out maximum, out convergence, out tolerance, out factor);
                     Debug.Print("          New Tolerance: ");
                     Debug.Print("              Frequency of performing equilibrium in number of solution steps: " + frequency);
                     Debug.Print("              Maximum number of equilibrium iterations for any solution step: " + maximum);
                     Debug.Print("              Relative displacement tolerance used for equilibrium convergence: " + convergence);
                     Debug.Print("              Tolerance for strain increment for models with creep or plasticity: " + tolerance);
                     Debug.Print("              Stiffness singularity elimination factor: " + factor);

                     Debug.Print("    Flow/Thermal Effects:");
                     Debug.Print("       Thermal options:");
                     Debug.Print("          Temperature source as defined in swsThermalOption_e: " + ssNonLinearStudyOptions.ThermalResults);
                     Debug.Print("          Temperature source:");
                     if (ssNonLinearStudyOptions.ThermalResults == 1)
                     {
                         Debug.Print("          Thermal study: " + ssNonLinearStudyOptions.ThermalStudyName);
                         Debug.Print("          Use temperature from thermal study at each nonlinear time step? (1=yes, 0=no): " + ssNonLinearStudyOptions.CheckUseTempFromThermalStudy);
                         if (ssNonLinearStudyOptions.CheckUseTempFromThermalStudy == 0)
                         {
                             Debug.Print("             Time step of transient thermal study whose temperature to use: " + ssNonLinearStudyOptions.TimeStep);
                         }
                     }
                     else if (ssNonLinearStudyOptions.ThermalResults == 2)
                     {
                         Debug.Print("               SOLIDWORKS Flow Simulation results file: "  + ssNonLinearStudyOptions.FlowTemperatureFile);
                     }
                     else
                     {
                         Debug.Print("               The current model");
                     }

                     Debug.Print("       Fluid pressure option:");
                     Debug.Print("          Import fluid pressure loads from SOLIDWORKS Flow Simulation? (1=yes, 0=no): " + ssNonLinearStudyOptions.CheckFlowPressure);
                     if (ssNonLinearStudyOptions.CheckFlowPressure == 1)
                     {
                         Debug.Print("           SOLIDWORKS Flow Simulation results file: " + ssNonLinearStudyOptions.FlowPressureFile);
                         Debug.Print("           Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " + ssNonLinearStudyOptions.ReferencePressureOption);
                         if (ssNonLinearStudyOptions.ReferencePressureOption == 0)
                         {
                             Debug.Print("             Reference pressure offset: " + ssNonLinearStudyOptions.DefinedReferencePressure);
                         }
                         Debug.Print("          Run as legacy study and import only the normal component of the pressure load? (1=yes, 0=no): " + ssNonLinearStudyOptions.CheckRunAsLegacy);
                     }

                 }
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

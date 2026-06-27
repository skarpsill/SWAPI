---
title: "Create Local Linear Pattern Example(C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Linear_Pattern_Example_CSharp.htm"
---

# Create Local Linear Pattern Example(C#)

## Create Local Linear Pattern Example (C#)

This example shows how to create a local linear pattern feature.

```vb
  //---------------------------------------------------------------------
 // Preconditions: Verify that the assembly exists.
 //
 // Postconditions:
 // 1. Opens the assembly.
 // 2. Selects an edge for Direction 1.
 // 3. Selects a subassembly to pattern.
 // 4. Creates a LocalLPattern1.
 // 5. Examine the FeatureManager design tree and graphics area.
 //
  // NOTE: Because the assembly is used elsewhere, do not save changes.
 //---------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateLocalLinearPattern_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private ModelDocExtension swModelDocExt;
         private FeatureManager swFeatureManager;
         private Feature swFeature;
         private LocalLinearPatternFeatureData swLocalLinearPatternFD;
         private bool status;
         private int errors = 0;
         private int warnings = 0;
         private string fileName;
         public void Main()
         {

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\distance linkage.sldasm";
             swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings);
             swModelDocExt = swModel.Extension;
             swFeatureManager = swModel.FeatureManager;
             status = swModelDocExt.SelectByID2("", "EDGE", 0.222723097227572, -0.193386735236572, -0.10172211746567, false, 2, null, 0);
             status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, true, 1, null, 0);
             swLocalLinearPatternFD = (LocalLinearPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmLocalLPattern);
             swLocalLinearPatternFD.D1ReverseDirection = true;
             swLocalLinearPatternFD.D1Spacing = 0.1516;
             swLocalLinearPatternFD.D1TotalInstances = 4;
             swLocalLinearPatternFD.D2PatternSeedOnly = false;
             swLocalLinearPatternFD.D2ReverseDirection = false;
             swLocalLinearPatternFD.D2Spacing = 0.05;
             swLocalLinearPatternFD.D2TotalInstances = 1;
             swLocalLinearPatternFD.SynchronizeFlexibleComponents = false;
             swFeature = swFeatureManager.CreateFeature(swLocalLinearPatternFD);
             swModel.ClearSelection2(true);
             swModel.ViewZoomtofit2();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

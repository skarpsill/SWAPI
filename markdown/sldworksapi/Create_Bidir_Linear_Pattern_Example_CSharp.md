---
title: "Create Bidirectional Linear Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidir_Linear_Pattern_Example_CSharp.htm"
---

# Create Bidirectional Linear Pattern Example (C#)

This example shows how to create a bidirectional linear pattern feature.

```vb
  //----------------------------------------------------
 // Preconditions: Verify that the part exists.
 //
 // Postconditions:
 // 1. Opens the part.
 // 2. Selects the feature to pattern.
  // 3. Selects the edges for Direction 1 and Direction 2
 //    of the bidirectional linear pattern.
 // 4. Creates LPattern1.
 // 5. Examine the FeatureManager design tree and graphics area.
 //
  // NOTE: Because the part is used elsewhere, do not save
 // changes.
  //------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateLinearPattern_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private ModelDocExtension swModelDocExt;
         private FeatureManager swFeatureManager;
         private Feature swFeature;
         private LinearPatternFeatureData swLinearPatternFeatureData;
         private bool status;
         private int errors = 0;
         private int warnings = 0;
         private string fileName;
         public void Main()
         {

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\box.sldprt";
             swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings);
             swModelDocExt = swModel.Extension;
             swFeatureManager = swModel.FeatureManager;
             //Select feature to pattern
             status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);

             //Select edges for Direction 1 and Direction 2
             status = swModelDocExt.SelectByID2("", "EDGE", -0.0341223962029176, 0.0300321434688158, 0.0460303188361877, true, 1, null, 0);
             status = swModelDocExt.SelectByID2("", "EDGE", 0.0436465176948104, 0.0301916139486593, 0.0114344277122314, true, 2, null, 0);

             //Create linear pattern
             swLinearPatternFeatureData = (LinearPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmLPattern);
             swLinearPatternFeatureData.D1EndCondition = 0;
             swLinearPatternFeatureData.D1ReverseDirection = false;
             swLinearPatternFeatureData.D1Spacing = 0.01;
             swLinearPatternFeatureData.D1TotalInstances = 4;
             swLinearPatternFeatureData.D2EndCondition = 0;
             swLinearPatternFeatureData.D2PatternSeedOnly = false;
             swLinearPatternFeatureData.D2ReverseDirection = false;
             swLinearPatternFeatureData.D2Spacing = 0.01;
             swLinearPatternFeatureData.D2TotalInstances = 4;
             swLinearPatternFeatureData.GeometryPattern = false;
             swLinearPatternFeatureData.VarySketch = false;
             swFeature = swFeatureManager.CreateFeature(swLinearPatternFeatureData);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

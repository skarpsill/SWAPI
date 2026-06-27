---
title: "Create Bidirectional Circular Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm"
---

# Create Bidirectional Circular Pattern Feature Example (C#)

This example shows how to create a bidirectional circular pattern feature.

```vb
//-------------------------------------------------------
 // Preconditions:
 // 1. Verify that the part exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the part.
 // 2. Selects a feature.
 // 3. Selects an edge for Direction 1.
 // 4. Creates a bidirectional circular pattern.
 // 5. Examine the FeatureManager design tree,
 //    graphics area, and Immediate window.
 //
 // NOTE: Because the part is used elsewhere, do not
 // save changes.
 //--------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace Macro1CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             FeatureManager swFeatureManager = default(FeatureManager);
             Feature swFeature = default(Feature);
             CircularPatternFeatureData swCircularPatternFeatureData = default(CircularPatternFeatureData);
             bool status = false;
             int errors = 0;
             int warnings = 0;
             string fileName = null;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\featurecircularpattern.sldprt";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swFeatureManager = (FeatureManager)swModel.FeatureManager;
             status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", -0.0000568552547690615, 0.0336059294503599, 0.0699999999999932, false, 4, null, 0);
             status = swModelDocExt.SelectByRay(0.0289184346104037, 0.0205122863998071, 0.0598787397922251, 0.342497149434059, -0.159204982974168, -0.925931679998983, 0.000912809005339891, 1, true, 1, 0);
             swCircularPatternFeatureData = (CircularPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmCirPattern);
             swFeature = (Feature)swFeatureManager.CreateFeature(swCircularPatternFeatureData);
             swCircularPatternFeatureData = (CircularPatternFeatureData)swFeature.GetDefinition();
             Debug.Print("Direction 1:");
             Debug.Print("  Equal spacing: " + swCircularPatternFeatureData.EqualSpacing);
             Debug.Print("  Spacing: " + swCircularPatternFeatureData.Spacing);
             Debug.Print("  Total instances: " + swCircularPatternFeatureData.TotalInstances);
             if (swCircularPatternFeatureData.Direction2 == true)
             {
                 Debug.Print("Direction 2:");
                 Debug.Print("  Symmetric: " + swCircularPatternFeatureData.Symmetric);
                 Debug.Print("  Equal spacing: " + swCircularPatternFeatureData.EqualSpacing2);
                 Debug.Print("  Spacing: " + swCircularPatternFeatureData.Spacing2);
                 Debug.Print("  Total instances: " + swCircularPatternFeatureData.TotalInstances2);
             }

         }

         /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

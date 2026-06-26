---
title: "Create Derived Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_Pattern_Feature_Example_CSharp.htm"
---

# Create Derived Pattern Feature Example (C#)

This example shows how to create a derived pattern feature.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Verify that the assembly to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Creates a derived pattern feature.
// 3. Gets the type and name of the pattern feature used for
//    the derived pattern feature.
// 4. Changes the position of the pattern instance used as the seed
//    feature in the derived pattern feature.
// 5. Examine the FeatureManager design tree, Immediate window, and
//    graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------

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
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            DerivedPatternFeatureData swDerivedPatternFeatureData = default(DerivedPatternFeatureData);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            Feature patternObj = default(Feature);

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\assem2.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExtension = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swModel.ClearSelection2(true);

            // Create derived pattern feature
            status = swModelDocExtension.SelectByID2("Part2^assem2-7@assem2", "COMPONENT", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExtension.SelectByID2("LPattern1@Part3^assem2-1@assem2", "BODYFEATURE", 0, 0, 0, true, 2, null, 0);
            swDerivedPatternFeatureData = (DerivedPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmDerivedLPattern);
            swFeature = (Feature)swFeatureManager.CreateFeature(swDerivedPatternFeatureData);

            // Get derived pattern feature name and type
            if ((swFeature != null))
            {
                Debug.Print("Derived pattern feature name = " + swFeature.Name);
                Debug.Print("  Type of feature: " + swFeature.GetTypeName2());
                swDerivedPatternFeatureData = (DerivedPatternFeatureData)swFeature.GetDefinition();
                if ((swDerivedPatternFeatureData != null))
                {
                    swDerivedPatternFeatureData.AccessSelections(swModel, null);
                    // Get type of pattern feature used for derived pattern feature
                    patternObj = (Feature)swDerivedPatternFeatureData.PatternFeature;
                    Debug.Print("    Type of pattern feature used for derived pattern feature: " + patternObj.GetTypeName2());
                    // Get pattern feature name
                    Debug.Print("    Name of pattern feature used for the derived pattern feature: " + patternObj.Name);
                    LinearPatternFeatureData swLinearPatternFeatureData = default(LinearPatternFeatureData);
		    // Get the pattern feature used for the derived pattern feature
		    swLinearPatternFeatureData = (LinearPatternFeatureData)patternObj.GetDefinition();
                    int nbrPatternInstances = 0;
		    nbrPatternInstances = (swLinearPatternFeatureData.D1TotalInstances* swLinearPatternFeatureData.D2TotalInstances);
		    Debug.Print("    Total number of pattern instances in pattern feature used for the derived pattern feature: " + nbrPatternInstances);
                    // Get position of the pattern instance used as the seed feature in the derived pattern feature
                    Debug.Print("      Position of the pattern instance used as the seed feature in the derived pattern feature: " + swDerivedPatternFeatureData.SeedPosition);
                    // Change position of the pattern instance to use as the seed feature in the derived pattern feature
                    swDerivedPatternFeatureData.SeedPosition = nbrPatternInstances - 1;
                    Debug.Print("      Modified position of the pattern instance to use as the seed feature in the derived pattern feature: " + swDerivedPatternFeatureData.SeedPosition);
                    swFeature.ModifyDefinition(swDerivedPatternFeatureData, swModel, null);
                }
            }

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Create and Modify Distance Chain Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm"
---

# Create and Modify Distance Chain Pattern Feature Example (C#)

This example shows how to create and modify a distance chain pattern feature.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that the assembly to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly.
// 2. Selects entities to create a distance chain pattern feature.
// 3. Creates the distance chain pattern feature.
// 4. After examining the graphics area and FeatureManager design
//    tree, press F5.
// 5. Modifies the distance chain pattern feature.
// 6. Examine the graphics area to verify step 5.
// 7. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
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
            ChainPatternFeatureData swChainPatternFeatureData = default(ChainPatternFeatureData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\distance linkage.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select entities to create distance chain pattern feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Belt Drive Path", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Mount Base-1@distance linkage", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            swModel.ViewZoomTo2(1.03935160466665, -0.0995602294424154, 0.846177052265487, 1.16810340243326, -0.261325308687639, 0.846177052265488);
            status = swModelDocExt.SelectByID2("", "FACE", 0.187298652259415, -0.193039676915248, 0.113419833821467, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Right Plane@Mount Base-1@distance linkage", "PLANE", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Belt Drive Path", "SKETCH", 0, 0, 0, false, 2, null, 0);
            status = swModelDocExt.SelectByID2("Mount Base-1@distance linkage", "COMPONENT", 0, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.187298652259415, -0.193039676915248, 0.113419833821467, true, 256, null, 0);
            status = swModelDocExt.SelectByID2("Right Plane@Mount Base-1@distance linkage", "PLANE", 0, 0, 0, true, 16384, null, 0);

            //Create distance chain pattern feature
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swChainPatternFeatureData = (ChainPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmLocalChainPattern);
    	    swFeature = (Feature)swFeatureManager.CreateFeature(swChainPatternFeatureData);
            swModel.ClearSelection2(true);
            swModel.ViewZoomtofit2();

            System.Diagnostics.Debugger.Break();
            //Examine the graphics area and FeatureManager design tree
            //Press F5

            //Modify distance chain pattern feature
            swChainPatternFeatureData = (ChainPatternFeatureData)swFeature.GetDefinition();
            status = swChainPatternFeatureData.AccessSelections(swModel, null);
            swChainPatternFeatureData.Spacing = 0.078;
            swChainPatternFeatureData.FillPath = true;
            Debug.Print("Number of instances calculated by SOLIDWORKS to fill the path: " + swChainPatternFeatureData.InstanceCount);
            swFeature.ModifyDefinition(swChainPatternFeatureData, swModel, null);

            //Examine the graphics area
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

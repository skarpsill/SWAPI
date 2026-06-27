---
title: "Modify Chain Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Chain_Pattern_Feature_Example_CSharp.htm"
---

# Modify Chain Pattern Feature Example (C#)

This example shows how to modify a chain pattern feature.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Verify that these files exist in public_documents\samples\tutorial\api:
//    * cam roller.sldprt
//    * distance linkage.sldasm
//    * mount base.sldasm
//    * mount plate.sldprt
// 2. Open distance linkage.sldasm.
//    a. Click Insert > Component Pattern > Chain Pattern.
//       1. Click Distance Linkage in Pitch Method.
//       2. Click Belt Drive Path in the FeatureManager design tree
//          for Path.
//       3. Set Number of Instances to 4.
//       4. Click Mount Base<1> in the FeatureManager design tree
//          for Component to Pattern.
//       5. Set Spacing to approximately 10.
//       6. Click the cylindrical face on Cam Roller<3> (left-front cam)
//          in the graphics area for Path Link1. Zoom in if necessary.
//       7. Click the cylindrical face on Cam Roller<1> (right-front cam)
//          in the graphics area for Path Link2.
//       8. Expand Mount Base<1> and click its Right Plane in the
//          FeatureManager design tree for Path Alignment Plane.
//    b. Click OK to create ChainPattern1 feature.
//    c. Click Zoom to Fit.
// 3. Examine the FeatureManager design tree and graphics area.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Selects the ChainPattern1 feature.
// 2. Gets and sets some ChainPattern1 data.
// 3. Click Zoom to fit.
// 4. Examine the Immediate window and graphics area.
//
// NOTE: Because these models are used elsewhere, do not save changes.
//-------------------------------------------------------------------
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
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            ChainPatternFeatureData swChainPatternFeatureData = default(ChainPatternFeatureData);
            ModelView swModelView = default(ModelView);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelView = (ModelView)swModel.ActiveView;

            //Get ChainPattern1 feature
            //Get and set some of its data
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("ChainPattern1", "COMPPATTERN", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swChainPatternFeatureData = (ChainPatternFeatureData)swFeature.GetDefinition();
            status = swChainPatternFeatureData.AccessSelections(swModel, null);
            Debug.Print("Name of feature: " + swFeature.Name);
            //Get pitch type
            Debug.Print("  Pitch type: " + swChainPatternFeatureData.PitchMethod);
            //Get align method
            Debug.Print("  Align method: " + swChainPatternFeatureData.AlignMethod);
            //Get whether Fill Path selected
            Debug.Print("  Original Fill Path: " + swChainPatternFeatureData.FillPath);
            //Get number of pattern instances and spacing
            Debug.Print("  Original number of instances: " + swChainPatternFeatureData.InstanceCount);
            Debug.Print("  Original distance between each pattern instance: " + swChainPatternFeatureData.Spacing);
            //Set Fill Path to true
            swChainPatternFeatureData.FillPath = true;
            Debug.Print("  Modified Fill Path: " + swChainPatternFeatureData.FillPath);
            //Change spacing
            swChainPatternFeatureData.Spacing = 0.2;
            Debug.Print("  Modified distance between each pattern instance: " + swChainPatternFeatureData.Spacing);

            swFeature.ModifyDefinition(swChainPatternFeatureData, swModel, null);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

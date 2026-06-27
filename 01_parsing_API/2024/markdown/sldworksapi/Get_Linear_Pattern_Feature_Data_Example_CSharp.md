---
title: "Get Linear Pattern Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Linear_Pattern_Feature_Data_Example_CSharp.htm"
---

# Get Linear Pattern Feature Data Example (C#)

This example shows how to get data for a linear pattern feature.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part document with a LPattern1 feature.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets, sets, and prints linear pattern feature data to
//    the Immediate window.
// 2. Examine the FeatureManager design tree, graphics area, and Immediate window.
//----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace LinearPatternFeaturDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            LinearPatternFeatureData swLinearPatternFeatureData = default(LinearPatternFeatureData);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get the linear pattern feature data
            status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swLinearPatternFeatureData = (LinearPatternFeatureData)swFeature.GetDefinition();
            swLinearPatternFeatureData.AccessSelections(swModel, null);
            Debug.Print("Number of features in pattern: " + swLinearPatternFeatureData.GetPatternFeatureCount());
            Debug.Print("Total number of instances: ");
            Debug.Print(" Direction 1: " + swLinearPatternFeatureData.D1TotalInstances);
            Debug.Print(" Direction 2: " + swLinearPatternFeatureData.D2TotalInstances);
            //Change Direction 2 spacing
            Debug.Print("Direction 2 spacing: ");
            Debug.Print(" Original: " + swLinearPatternFeatureData.D2Spacing);
            swLinearPatternFeatureData.D2Spacing = 0.04;
            Debug.Print(" Updated: " + swLinearPatternFeatureData.D2Spacing);
            swFeature.ModifyDefinition(swLinearPatternFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

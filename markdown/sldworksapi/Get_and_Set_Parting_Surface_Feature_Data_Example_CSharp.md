---
title: "Get and Set Parting Surface Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm"
---

# Get and Set Parting Surface Feature Data Example (C#)

This example shows how to get and set parting surface feature data.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a model document that contains a parting surface feature.
// 2. Select the parting surface feature in the FeatureManager design tree.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets and sets parting surface feature data.
// 2. Examine the Immediate window.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace PartingSurfaceFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            PartingSurfaceFeatureData swPartingSurfaceFeatureData = default(PartingSurfaceFeatureData);
            bool state = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get parting surface feature
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swPartingSurfaceFeatureData = (PartingSurfaceFeatureData)swFeature.GetDefinition();

            //Roll back to get and set parting surface feature data
            state = swPartingSurfaceFeatureData.AccessSelections(swModel, null);
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print(" Feature name: " + swFeature.Name);
            Debug.Print("    Number of parting lines: " + swPartingSurfaceFeatureData.GetPartingLinesCount());
            Debug.Print("    Parting line type (0 = parting line feature, 1 = edge): " + swPartingSurfaceFeatureData.GetPartingLinesType());
            Debug.Print("    Parting surface type as defined by swPartingSurfaceMoldParmType_e: " + swPartingSurfaceFeatureData.PartingType);
            if (swPartingSurfaceFeatureData.PartingType == (int)swPartingSurfaceMoldParmType_e.swPartingSurfaceMoldParmPerpendicular)
            {
                Debug.Print("    Offset angle not available for this parting surface type.");
            }
            else
            {
                Debug.Print("    Offset angle: " + swPartingSurfaceFeatureData.OffsetAngle);
            }
            Debug.Print("    Knit all surfaces: " + swPartingSurfaceFeatureData.Knit);
            Debug.Print("    Distance this parting surface feature extends: " + swPartingSurfaceFeatureData.OffsetDistance);
            Debug.Print("    Transition between adjacent edges as defined by swPartingSurfaceSmoothingType_e: " + swPartingSurfaceFeatureData.TransitionType);
            //Reverse alignment
            if (swPartingSurfaceFeatureData.ReverseAlignment == true)
            {
                swPartingSurfaceFeatureData.ReverseAlignment = false;
            }
            else
            {
                swPartingSurfaceFeatureData.ReverseAlignment = true;
            }
            Debug.Print("    Reversed alignment: " + swPartingSurfaceFeatureData.ReverseAlignment);
```

```
            //Modify and roll forward parting surface feature
            swFeature.ModifyDefinition(swPartingSurfaceFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

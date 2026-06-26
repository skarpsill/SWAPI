---
title: "Get and Set Parting Line Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm"
---

# Get and Set Parting Line Feature Data Example (C#)

This example shows how to get and set parting line feature data.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a model document that contains a parting line feature.
// 2. Select the parting line feature in the FeatureManager design tree.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets and sets parting line feature data.
// 2. Examine the Immediate window.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace PartingLineFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            PartingLineFeatureData swPartingLineFeatureData = default(PartingLineFeatureData);
            bool state = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get parting line feature
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swPartingLineFeatureData = (PartingLineFeatureData)swFeature.GetDefinition();

            //Roll back to get and set parting line feature data
            state = swPartingLineFeatureData.AccessSelections(swModel, null);
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print(" Feature name: " + swFeature.Name);
            Debug.Print("    Parting line status as defined by swPartingLineFeatureStatus_e: " + swPartingLineFeatureData.Status());
            Debug.Print("    Draft angle: " + swPartingLineFeatureData.Angle);
            //Reverse pull direction of part line
            Debug.Print("    Pull direction before reversing: " + swPartingLineFeatureData.PullDirection);
            if (swPartingLineFeatureData.PullDirection)
            {
                swPartingLineFeatureData.PullDirection = false;
            }
            else
            {
                swPartingLineFeatureData.PullDirection = true;
            }
            Debug.Print("    Pull direction after reversing: " + swPartingLineFeatureData.PullDirection);
            Debug.Print("    Pull direction type as defined by swSelectType_e: " + swPartingLineFeatureData.PullDirectionType);
            Debug.Print("    Split faces: " + swPartingLineFeatureData.SplitFaces);
            if (swPartingLineFeatureData.SplitFaces)
            {
                Debug.Print("    Split faces options as defined by swSplitFacesOption_e: " + swPartingLineFeatureData.SplitFacesOption);
            }
            Debug.Print("    Core/cavity split: " + swPartingLineFeatureData.CoreCavitySplit);
            Debug.Print("    Number of entities to split: " + swPartingLineFeatureData.GetEntitiesToSplitCount());

            //Modify and roll forward parting line feature
            swFeature.ModifyDefinition(swPartingLineFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

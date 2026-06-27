---
title: "Get Heal Edges Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Heal_Edges_Feature_Data_Example_CSharp.htm"
---

# Get Heal Edges Feature Data Example (C#)

This example shows how to get some data of a heal edges feature.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a part document that contains a HealEdge1 feature.
// 2. Select the HealEdge1 feature.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets HealEdge1 feature data.
// 2. Examine the Immediate window.
//----------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace HealEdgesFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            HealEdgesFeatureData swHealEdgesFeature = default(HealEdgesFeatureData);
            Feature swFeature = default(Feature);
            int before = 0;
            int after = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get and print HealEdge1 feature data
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, 0);
            swHealEdgesFeature = (HealEdgesFeatureData)swFeature.GetDefinition();
            swModel.ClearSelection2(true);
            swHealEdgesFeature.AccessSelections(swModel, null);
            Debug.Print("Number of faces in this heal edges feature: " + swHealEdgesFeature.GetFacesCount());
            Debug.Print("Number of edges before and after healing: ");
            swHealEdgesFeature.GetEdgeInformation(out before, out after);
            Debug.Print("  Before: " + before);
            Debug.Print("  After : " + after);
            Debug.Print(" Maximum angle betweeen the merged edges: " + swHealEdgesFeature.AngularTolerance);
            Debug.Print(" Maximum length of the merged edges: " + swHealEdgesFeature.EdgeLengthTolerance);
            swHealEdgesFeature.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

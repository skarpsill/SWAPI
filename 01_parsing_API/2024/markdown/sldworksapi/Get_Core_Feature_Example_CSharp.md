---
title: "Get Core Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Core_Feature_Example_CSharp.htm"
---

# Get Core Feature Data Example (C#)

This example shows how to get the data for a core feature.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Open a model document that contains a core feature.
// 2. Open the Immediate window.
// 3. Select the core feature in the FeatureManager design tree.
//
// Postconditions:
// 1. Prints the core feature data to the Immediate window.
// 2. Examine the Immediate window.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CoreFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            CoreFeatureData swCoreFeat = default(CoreFeatureData);
            bool b = false;
            string nam = null;
            bool cap = false;
            double d1 = 0;
            double d2 = 0;
            double ang = 0;
            bool useDr = false;
            bool Drout = false;
            bool rev = false;
            int typ1 = 0;
            int typ2 = 0;
            object dir1 = null;
            object dir2 = null;
            int e1 = 0;
            int e2 = 0;
            int ct = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swCoreFeat = (CoreFeatureData)swFeat.GetDefinition();

            //Roll back to the feature before the core feature
            b = swCoreFeat.AccessSelections(swModel, null);

            //Get the bounding sketch of the core feature
            swFeat = swCoreFeat.BoundingSketch;
            nam = swFeat.Name;
            Debug.Print("Name of bounding sketch = " + nam);
            cap = swCoreFeat.CapEnds;
            Debug.Print("Are ends capped? " + cap);
            d1 = swCoreFeat.get_Depth(0);
            Debug.Print("Depth along extraction direction = " + d1);
            d2 = swCoreFeat.get_Depth(1);
            Debug.Print("Depth away from extraction direction = " + d2);
            useDr = swCoreFeat.UseDraft;
            Debug.Print("Drafted? " + useDr);
            if (useDr)
            {
                ang = swCoreFeat.DraftAngle;
                Debug.Print("Angle of draft = " + ang);
                Drout = swCoreFeat.DraftOutward;
                Debug.Print("Drafted outward? = " + Drout);
            }
            e1 = swCoreFeat.get_EndCondition(0);
            Debug.Print("End condition along extraction = " + e1);
            e2 = swCoreFeat.get_EndCondition(1);
            Debug.Print("End condition away from extraction = " + e2);
            rev = swCoreFeat.ReverseDirection;
            Debug.Print("Direction of extraction reversed? " + rev);
            ct = swCoreFeat.GetExtractionDirection(out typ1, out dir1, out typ2, out dir2);
            Debug.Print("Number of entities that define extraction = " + ct);

            //Roll forward
            swCoreFeat.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

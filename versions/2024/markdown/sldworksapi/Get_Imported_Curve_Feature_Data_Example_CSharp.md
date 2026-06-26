---
title: "Get Imported Curve Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Imported_Curve_Feature_Data_Example_CSharp.htm"
---

# Get Imported Curve Feature Data Example (C#)

This example shows how to get the number of curves in an imported curve feature.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open a part document that has an ImportedCurve1 feature.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the ImportedCurve1 feature.
// 2. Gets the number of curves in ImportedCurve1.
// 3. Examine the Immediate window.
//-----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ImportedCurveFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            ImportedCurveFeatureData swImportedCurveFeatureData = default(ImportedCurveFeatureData);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Select ImportedCurve1 and get the number of curves in the feature
            status = swModelDocExt.SelectByID2("ImportedCurve1", "REFERENCECURVES", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swImportedCurveFeatureData = (ImportedCurveFeatureData)swFeature.GetDefinition();
            Debug.Print("Number of curves: " + swImportedCurveFeatureData.GetCurveCount());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

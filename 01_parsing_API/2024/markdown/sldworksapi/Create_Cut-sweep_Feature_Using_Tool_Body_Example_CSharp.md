---
title: "Create Cut-sweep Feature Using Tool Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Tool_Body_Example_CSharp.htm"
---

# Create Cut-sweep Feature Using Tool Body Example (C#)

This example shows how to create a cut-sweep feature using a tool body.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a boss-extrude feature.
// 2. Creates a sketch.
// 3. Creates a revolve feature.
// 4. Selects the revolve feature, sketch, and extrude feature and
//    creates a cut-sweep feature.
// 5. Accesses the cut-sweep feature.
// 6. Gets the names of the cut-sweep feature's tool body and path.
// 7. Releases access of the cut-sweep feature.
// 8. Examine the Immediate window, FeatureManager design tree,
//    and graphics area.
//---------------------------------------------------------------
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
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureMgr = default(FeatureManager);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            SweepFeatureData swSweepFeatureData = default(SweepFeatureData);
            object swProfileObj = null;
            Body2 swProfileBody = default(Body2);
            Feature swPathFeature = default(Feature);
            object[] sketchLines = null;
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create extrude feature
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.000361, 0.001416, 0.0, 0.024462, -0.045092, 0.0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, true, 0, 0, 0.09, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);

            //Create sketch
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelectionMgr.EnableContourSelection = false;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-1.9E-05, 0.00051, 0.0, 0.026716, -0.0401, 0.0);
            swSketchMgr.InsertSketch(true);
            swModel.ClearSelection2(true);

            //Create revolve feature
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.0266210577384013, -0.0248555003438298, 0, -0.0378465609175683, -0.0475106067599669, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", -0.0264169576805983, -0.0449999999999998, 0.0293457016154969, false, 16, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureRevolve2(true, true, false, false, false, false, 0, 0, 6.2831853071796, 0,
            false, false, 0.01, 0.01, 0, 0, 0, false, true, true);
            swSelectionMgr.EnableContourSelection = false;
            swModel.ClearSelection2(true);

            //Create cut-sweep feature
            status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, true, 2048, null, 0);
            swFeature = (Feature)swFeatureMgr.InsertCutSwept5(false, true, 0, false, false, 0, 0, false, 0, 0,
            0, 0, true, false, 0, true, true, true, false, false,
            0, 0);
            Debug.Print("Feature name = " + swFeature.Name);
            swSweepFeatureData = (SweepFeatureData)swFeature.GetDefinition();

            // Roll back to access selections
            status = swSweepFeatureData.AccessSelections(swModel, null);
            swProfileObj = (object)swSweepFeatureData.Profile;
            swProfileBody = (Body2)swProfileObj;
            Debug.Print("  Tool body = " + swProfileBody.Name);
            swPathFeature = (Feature)swSweepFeatureData.Path;
            Debug.Print("  Path = " + swPathFeature.Name);

            // Roll forward
            swSweepFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

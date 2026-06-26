---
title: "Get Guide Curves in Sweep Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Guide_Curves_in_Sweep_Feature_Example_CSharp.htm"
---

# Get Guide Curves in Sweep Feature Example (C#)

This example shows how to get the guide curves in a sweep feature.

```
//----------------------------------------
// Preconditions:
// 1. Verify that the part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part document.
// 2. Creates a sweep feature.
// 3. Gets the number of guide curves in the sweep
//    feature.
// 4. Accesses the guide curves in the sweep feature.
// 5. Gets the feature types of the guide curves.
// 6. Releases access of the sweep feature.
// 7. Examine the Immediate window.
//----------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GuideCurvesSweepFeatureCSharp.csproj
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
            SweepFeatureData swSweepFeatureData = default(SweepFeatureData);
            object pointArray = null;
            double[] points = null;
            object[] guideCurves = null;
            object guideCurve = null;
            int nbrGuideCurves = 0;
            int[] guideCurvesTypes = null;
            int guideCurveType = 0;
            bool status = false;
            long i = 0;

            //Create new model document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2017\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Sketch an ellipse for sweep profile
            swModel.ClearSelection2(true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchMgr.InsertSketch(true);
            swSketchSegment = swSketchMgr.CreateEllipse(0, 0, 0, -0.064925207354862, 0, 0, 0, -0.0360377802938881, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Sketch a line for sweep path
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchMgr.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.0, 0.0, 0.0, 0.0, 0.059816, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Sketch a spline for sweep guide curve
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchMgr.InsertSketch(true);
            points = new double[6];
            points[0] = -0.064925207354862;
            points[1] = 0;
            points[2] = 0;
            points[3] = -0.00576005360247873;
            points[4] = 0.0595205538922803;
            points[5] = 0;
            pointArray = points;
            swSketchSegment = swSketchMgr.CreateSpline((pointArray));
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Unknown", "MANIPULATOR", -0.0481685228359519, 0.0168573405240843, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            swModel.ViewZoomtofit2();

            //Select the profile, path, and guide curve
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, true, 2, null, 0);

            //Create the sweep feature
            swFeatureMgr = swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertProtrusionSwept4(false, false, (int)swTwistControlType_e.swTwistControlFollowPath, false, false, (int)swTangencyType_e.swTangencyNone, (int)swTangencyType_e.swTangencyNone, false, 0, 0, (int)swThinWallType_e.swThinWallOneDirection, 0, true, true, true, 0, true, false, 0, 0);
            Debug.Print("Feature type: " + swFeature.GetTypeName2());

            //Change the orientation of the view
            swModel.ShowNamedView2("*Isometric", 7);

            //Access sweep feature data, get guide curves,
            //get feature type of guide curves, and release
            //access to sweep feature
            swSweepFeatureData = (SweepFeatureData)swFeature.GetDefinition();
            nbrGuideCurves = swSweepFeatureData.GetGuideCurvesCount();
            Debug.Print("  Number of guide curves: " + nbrGuideCurves);
            status = swSweepFeatureData.AccessSelections(swModel, null);
            Debug.Print("    Guide curve: ");
            guideCurves = (object[])swSweepFeatureData.GuideCurves;
            guideCurvesTypes = (int[])swSweepFeatureData.GetGuideCurvesType();
            for (i = 0; i <= (nbrGuideCurves - 1); i++)
            {
                guideCurve = (object)guideCurves[i];
                guideCurveType = (int)guideCurvesTypes[i];
                Debug.Print("      Type of feature as defined in swSelectType_e: " + guideCurveType);
            }
            swSweepFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Get Guide Curves in Loft Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Guide_Curves_in_Loft_Feature_Example_CSharp.htm"
---

# Get Guide Curves in Loft Feature Example (C#)

This example shows how to get the guide curves in a loft feature.

```
//----------------------------------------
// Preconditions:
// 1. Verify that the specified part document
//    template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part document.
// 2. Creates a loft feature.
// 3. Prints to the Immediate window
//    the feature type and feature name of the loft
//    feature.
// 4. Accesses the guide curves in the loft feature.
// 5. Prints to the Immediate window whether the
//    loft is a boss feature, the number guide
//    curves in the loft, and the feature types of
//    the guide curves.
// 6. Releases access to the loft feature.
// 7. Examine the Immediate window.
//----------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace LoftGuideCurveCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        FeatureManager swFeatureManager;
        RefPlane swRefPlane;
        SketchManager swSketchManager;
        SketchSegment swSketchSegment;
        Feature swFeature;
        LoftFeatureData swLoftFeatureData;
        object pointArray = null;
        double[] points = null;
        object[] guideCurves = null;
        object guideCurve;
        int nbrGuideCurves;
        int[] guideCurvesTypes = null;
        int guideCurveType = 0;
        int i = 0;
        bool status = false;

        public void Main()
        {
            //Open new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create reference plane
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(8, 0.0635, 0, 0, 0, 0);
            swModel.ClearSelection2(true);

            //Create circle for loft feature
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, true, 0, null, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(-0.0, 0.0, 0.0, 0.003857, -0.009744, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            //Create another circle for loft feature
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(-0.0, 0.0, 0.0, 0.014007, -0.029232, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            //Create sketch for guide curve
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            points = new double[9];
            points[0] = 0;
            points[1] = 0.0324150959148675;
            points[2] = 0;
            points[3] = 0.02176137524458;
            points[4] = 0.0209549481725162;
            points[5] = 0;
            points[6] = 0.0635;
            points[7] = 0.0104797609372824;
            points[8] = 0;
            pointArray = points;
            swSketchManager.InsertSketch(true);
            swSketchSegment = swSketchManager.CreateSpline((pointArray));
            swSketchManager.InsertSketch(true);

            //Create loft feature with guide curve
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0635, 0, -0.0104797609372824, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, -0.0324150959148675, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, true, 4098, null, 0);
            swFeature = (Feature)swFeatureManager.InsertProtrusionBlend2(false, true, false, 1, 0, 0, 1, 1, true, true, false, 0, 0, 0, true, true, true, (int)swGuideCurveInfluence_e.swGuideCurveInfluenceNextGlobal);
            Debug.Print("Feature:");
            Debug.Print("  Type: " + swFeature.GetTypeName2());
            Debug.Print("  Name: " + swFeature.Name);

            //Change the orientation of the view
            swModel.ShowNamedView2("*Isometric", 7);

            //Access loft feature data, get guide curves,
            //get feature type of guide curves, and release
            //access to loft feature
            swLoftFeatureData = (LoftFeatureData)swFeature.GetDefinition();
            Debug.Print("   Boss feature: " + swLoftFeatureData.IsBossFeature());
            nbrGuideCurves = swLoftFeatureData.GetGuideCurvesCount();
            Debug.Print("   Number of guide curves: " + nbrGuideCurves);
            status = swLoftFeatureData.AccessSelections(swModel, null);
            Debug.Print("    Guide curve: ");
            guideCurves = (object[])swLoftFeatureData.GuideCurves;
            guideCurvesTypes = (int[])swLoftFeatureData.GetGuideCurvesType();
            for (i = 0; i <= (nbrGuideCurves - 1); i++)
            {
                guideCurve = (object)guideCurves[i];
                guideCurveType = (int)guideCurvesTypes[i];
                Debug.Print("        Type of feature: " + guideCurveType);
            }
            swLoftFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

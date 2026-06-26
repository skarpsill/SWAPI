---
title: "Insert Solid Body Boundary Surface Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Solid_Body_Boundary_Surface_Feature_Example_CSharp.htm"
---

# Insert Solid Body Boundary Surface Feature Example (C#)

This example shows how to insert a solid body boundary surface feature.

```
//-------------------------------------------------------------
// Preconditions: Verify that the specified part template
// exists.
//
// Postconditions:
// 1. Opens a new part.
// 2. Inserts a sketch of a rectangle, Sketch1, on Front Plane.
// 3. Creates Surface-Plane1 using Sketch1.
// 4. Creates Plane1.
// 5. Creates a sketch of a circle, Sketch2, on Plane1.
// 6. Creates Surface-Plane2 using Sketch2.
// 7. Inserts a solid body boundary surface feature, Boundary-Surface1,
//    using Surface-Plane1 and Surface-Plane2.
// 8. Examine the graphics area and expand Solid Bodies(1) in the
//    FeatureManager design tree to verify step 7.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureMgr = default(FeatureManager);
            SketchManager swSketchMgr = default(SketchManager);
            RefPlane swRefPlane = default(RefPlane);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            object[] sketchSegments = null;
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;

            //Create Surface-Plane1
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0687189668956523, 0.0593633502290038, 0.00936526409663904, false, 0, null, 0);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchSegments = (object[])swSketchMgr.CreateCornerRectangle(-0.0399911197344551, 0.02969400507229, 0, 0.0502882343966202, -0.0299334728551311, 0);
            swSketchMgr.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModel.InsertPlanarRefSurface();
            swModel.ClearSelection2(true);

            //Create Plane1
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swRefPlane = (RefPlane)swFeatureMgr.InsertRefPlane((int)swRefPlaneReferenceConstraints_e.swRefPlaneReferenceConstraint_Distance, 0.15, 0, 0, 0, 0);
            swModel.ClearSelection2(true);

            //Create Surface-Plane2
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, true, 0, null, 0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.003592, 0.003353, 0.0, 0.035202, -0.057233, 0.0);
            swSketchMgr.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 1, null, 0);
            status = swModel.InsertPlanarRefSurface();
            swModel.ClearSelection2(true);
            swModel.ViewZoomtofit2();

            //Insert a solid body boundary surface feature
            status = swModelDocExt.SelectByID2("Surface-Plane1", "SURFACEBODY", -0.0399911197344551, 0.02969400507229, 0, false, 8193, null, 0);
            status = swModelDocExt.SelectByID2("Surface-Plane2", "SURFACEBODY", -0.0463651179854531, -0.0432741101197696, 0.15, true, 16385, null, 0);
            swFeature = (Feature)swFeatureMgr.SetNetBlendCurveData(0, 0, (int)swTangencyType_e.swTangencyNone, 0, 1, true);
            swFeature = (Feature)swFeatureMgr.SetNetBlendCurveData(0, 1, (int)swTangencyType_e.swTangencyNone, 0, 1, true);
            swFeature = (Feature)swFeatureMgr.SetNetBlendDirectionData(0, 32, 0, false, false);
            swFeature = (Feature)swFeatureMgr.SetNetBlendDirectionData(1, 32, 0, false, false);
            swFeature = (Feature)swFeatureMgr.InsertNetBlend2(2, 2, 0, false, 0.0001, false, true, true, true, false,
            -1, -1, false, -1, false, false, -1, false, -1, true,
            true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

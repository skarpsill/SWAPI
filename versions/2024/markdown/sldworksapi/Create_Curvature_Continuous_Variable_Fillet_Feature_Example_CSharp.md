---
title: "Create Curvature Continuous Variable Fillet Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curvature_Continuous_Variable_Fillet_Feature_Example_CSharp.htm"
---

# Create Curvature Continuous Variable Fillet Feature Example (C#)

This example shows how to create a curvature continuous variable fillet feature.

```
//-------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a part with a variable fillet feature with curvature continuous.
// 2. Gets whether the variable fillet feature has curvature continuous set.
// 3. Examine the graphics area and the Immediate window.
//-------------------------------------------------------------------------------
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
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            VariableFilletFeatureData2 swVariableFilletFeatureData = default(VariableFilletFeatureData2);
            bool status = false;
            object radiiArray2 = null;
            double[] radiis2 = null;
            object dist2Array2 = null;
            double[] dists22 = null;
            object conicRhosArray2 = null;
            double[] coniRhos2 = null;
            object setBackArray2 = null;
            double setBacks2 = 0;
            object pointArray2 = null;
            double points2 = 0;
            object pointDist2Array2 = null;
            double pointsDist22 = 0;
            object pointRhoArray2 = null;
            double pointsRhos2 = 0;
            int filletOptions = 0;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchManager = (SketchManager)swModel.SketchManager;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Create part with variable feature fillet with curvature continuous
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swSketchSegment = swSketchManager.CreateLine(-0.070405, 0.03105, 0.0, -0.070405, -0.033217, 0.0);
            swSketchSegment = swSketchManager.CreateLine(-0.070405, -0.033217, 0.0, 0.01733, -0.033217, 0.0);
            swSketchSegment = swSketchManager.CreateLine(0.01733, -0.033217, 0.0, 0.01733, -0.016247, 0.0);
            swSketchSegment = swSketchManager.CreateLine(0.01733, -0.016247, 0.0, -0.026537, -0.009748, 0.0);
            swSketchSegment = swSketchManager.CreateLine(-0.026537, -0.009748, 0.0, -0.04116, 0.024552, 0.0);
            swSketchSegment = swSketchManager.CreateLine(-0.04116, 0.024552, 0.0, -0.070405, 0.03105, 0.0);
            swModel.ShowNamedView2("*Trimetric", 8);
            swModel.ClearSelection2(true);
            swFeature = (Feature)swFeatureManager.FeatureExtrusion3(true, false, false, 0, 0, 0.04064, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionMgr.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 0.0243713283917941, 0.023466279649881, true, 1, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 0.0243713283917941, 0.023466279649881, false, 1, null, 0);
            radiis2 = new double[2];
            radiis2[0] = 0.00508;
            radiis2[1] = 0.01778;
            dists22 = new double[2];
            coniRhos2 = new double[2];
            radiiArray2 = radiis2;
            dist2Array2 = dists22;
            conicRhosArray2 = coniRhos2;
            setBackArray2 = setBacks2;
            pointArray2 = points2;
            pointDist2Array2 = pointsDist22;
            pointRhoArray2 = pointsRhos2;

            filletOptions = (int)swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous + (int)swFeatureFilletOptions_e.swFeatureFilletKeepFeatures + (int)swFeatureFilletOptions_e.swFeatureFilletPropagateFeatToParts;
            swFeature = (Feature)swFeatureManager.FeatureFillet3(filletOptions, 0.00254, 1E-07, 0, 1, 0, 0, (radiiArray2), (dist2Array2), (conicRhosArray2),
            (setBackArray2), (pointArray2), (pointDist2Array2), (pointRhoArray2));

            //Verify variable fillet feature has curvature continuous set
            swVariableFilletFeatureData = (VariableFilletFeatureData2)swFeature.GetDefinition();
            status = swVariableFilletFeatureData.AccessSelections(swModel, null);
            Debug.Print("Variable fillet feature has continuous curvature set: " + swVariableFilletFeatureData.CurvatureContinuous);
            swVariableFilletFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

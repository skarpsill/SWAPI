---
title: "Get Projected Curve Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Projected_Curve_Feature_Data_Example_CSharp.htm"
---

# Get Projected Curve Feature Data Example (C#)

This example shows how to get data for a projected curve feature.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects a face and sketches a spline on that face.
// 3. Selects the sketch of the spline and a face.
// 4. Inserts a projected curve feature.
// 5. Gets some projected curve feature data and prints it
//    to the Immediate window.
// 6. Examine the Immediate window, FeatureManager design tree, and
//    the graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ProjectCurveCSharp.csproj
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
            SelectionMgr swSelectionManager = default(SelectionMgr);
            ProjectionCurveFeatureData swProjectionCurveFeatureData = default(ProjectionCurveFeatureData);
            Sketch swSketch = default(Sketch);
            object pointArray = null;
            double[] points = new double[11];
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Sketch a spline on the selected face
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.0499223104334874, 0.0396239999998897, 0.00738137362270663, false, 0, null, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            points[0] = -0.0624778997860176;
            points[1] = 0.00729572078180673;
            points[2] = 0;
            points[3] = -0.0364588790258153;
            points[4] = 0.0324586288177215;
            points[5] = 0;
            points[6] = 0.0104252377344665;
            points[7] = 0.0140473535914225;
            points[8] = 0;
            points[9] = 0.0646002912861796;
            points[10] = 0.0100590221094308;
            pointArray = points;
            swSketchSegment = (SketchSegment)swSketchManager.CreateSpline2((pointArray), false);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);

            //Insert projected curve
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0497146993259321, 0, -0.0256283866693252, true, 0, null, 0);
            swFeature = (Feature)swModel.InsertProjectedSketch2(1);

            //Get projected curve data
            status = swModelDocExt.SelectByID2("Curve1", "REFCURVE", 0, 0, 0, false, 0, null, 0);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionManager.GetSelectedObject6(1, -1);
            swProjectionCurveFeatureData = (ProjectionCurveFeatureData)swFeature.GetDefinition();
            swProjectionCurveFeatureData.AccessSelections(swModel, null);
            Debug.Print("Is reversed = " + swProjectionCurveFeatureData.Reverse);
            Debug.Print("Number of targeted faces = " + swProjectionCurveFeatureData.GetFaceArrayCount());
            swFeature = (Feature)swProjectionCurveFeatureData.Sketch;
            swSketch = (Sketch)swFeature.GetSpecificFeature2();
            Debug.Print("Name of sketch = " + swFeature.Name);
            swProjectionCurveFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

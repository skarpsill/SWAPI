---
title: "Insert Fill-surface Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Fill-surface_Feature_Example_CSharp.htm"
---

# Insert Fill-surface Feature Example (C#)

This example shows how to insert a fill-surface feature.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Sketches a circle on the Front Plane.
// 2. Offsets the Front Plane to create Plane1.
// 3. Sketches a circle on Plane1.
// 4. Creates a thin-feature loft using the circles
//    created in steps 1 and 3.
// 5. Selects one of the sketches to use for
//    the fill-surface feature.
// 6. Creates a fill-surface feature named Surface-Fill1.
// 7. Gets, sets, and prints some properties of the fill-surface feature
//    to the Immediate window.
// 8. Examine the FeatureManager design, graphics area, and the
//    the Immediate window.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace InsertFillFeature2CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            FeatureManager swFeatMgr = default(FeatureManager);
            RefPlane swRefPlane = default(RefPlane);
            Feature swFeat = default(Feature);
            FillSurfaceFeatureData swFillSurfaceFeatureData = default(FillSurfaceFeatureData);
            object selObj = null;
            bool status = false;
            int nbrPatchEntities = 0;
            object[] patchEntities = null;
            object entTypes = null;
            int[] entTypesArray;
            int i = 0;

            //Open a new model document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\part.prtdot", (int)swDwgPaperSizes_e.swDwgPaperAsize, 0, 0);

            //Select the front plane and sketch a circle
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swModel.ClearSelection2(true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.018863, -0.048015, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Offset the front plane to create Plane1
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swRefPlane = (RefPlane)swFeatMgr.InsertRefPlane(8, 0.0762, 0, 0, 0, 0);
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.005144, -0.017148, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            //Create a loft as a thin feature
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0120997659765269, 0.0131954647737917, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -0.0137458916138411, 0.0497220981864567, 0, true, 1, null, 0);
            swFeatMgr.InsertProtrusionBlend2(false, true, false, 1, 0, 0, 1, 1, true, true,
            true, 0.000254, 0.000254, 0, true, true, true, (int)swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge);

            //Get the sketch for the fill-surface feature
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0309259362651374, -0.0150632202505945, 0.0265529245975468, true, 257, null, (int)swSelectOption_e.swSelectOptionDefault);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            selObj = (object)swSelMgr.GetSelectedObject6(1, 257);

            //Insert the fill-surface feature
            swFeat = (Feature)swFeatMgr.InsertFillSurface2(2, (int)swFeatureFillSurfaceOptions_e.swOptimizeSurface, selObj, (int)swContactType_e.swContact, null, null);

            //Access the fill-surface feature
            swFillSurfaceFeatureData = (FillSurfaceFeatureData)swFeat.GetDefinition();
            status = swFillSurfaceFeatureData.AccessSelections(swModel, null);
            Debug.Print("Fill-surface feature: ");
            Debug.Print("  Number of constraint curves: " + swFillSurfaceFeatureData.GetConstraintCurvesCount());
            nbrPatchEntities = swFillSurfaceFeatureData.GetPatchBoundaryCount();
            Debug.Print("  Number of entities used to define the patch boundary: " + nbrPatchEntities);
            if (nbrPatchEntities > 0)
            {
                //Get the type of patch boundary entities
                patchEntities = (object[])swFillSurfaceFeatureData.GetPatchBoundary(out entTypes);
                entTypesArray = (int[])entTypes;
                for (i = 0; i <= nbrPatchEntities - 1; i++)
                {
                    Debug.Print("  Type of entity for patch boundary " + (i + 1) + " (1 = edge; 9 = sketch) : " + entTypesArray[i]);
                }
                Debug.Print("  Results merged? " + swFillSurfaceFeatureData.Merge);
                swFillSurfaceFeatureData.OptimizeSurface = false;
                Debug.Print("  Patch optimized? " + swFillSurfaceFeatureData.OptimizeSurface);
                Debug.Print("  Original resolution control: " + swFillSurfaceFeatureData.ResolutionControl);
                if (swFillSurfaceFeatureData.OptimizeSurface == false)
                {
                    swFillSurfaceFeatureData.ResolutionControl = 1;
                }
                Debug.Print("  Updated resolution control (valid values 1, 2 and 3; setting this value only valid if patch is not optimized): " + swFillSurfaceFeatureData.ResolutionControl);
            }
            status = swFeat.ModifyDefinition(swFillSurfaceFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

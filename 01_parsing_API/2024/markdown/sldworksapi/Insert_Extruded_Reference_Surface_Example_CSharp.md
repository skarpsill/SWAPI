---
title: "Insert Extruded Surface Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Extruded_Reference_Surface_Example_CSharp.htm"
---

# Insert Extruded Surface Example (C#)

This example shows how to insert an extruded surface in a model.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part and inserts Surface-Extrude1.
// 2. Expand the Surface Bodies folder to verify that it contains:
//    * Surface-Extrude[1]
//    * Surface-Extrude[2]
//    * Surface-Extrude[3]
// 3. Examine the Immediate window and graphics area.
//---------------------------------------------------------------------------
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
            object[] sketchLines = null;
            SketchSegment swSketchSegment = default(SketchSegment);
            SelectionMgr swSelMgr = default(SelectionMgr);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            SurfExtrudeFeatureData swSurfExtrudeFeature = default(SurfExtrudeFeatureData);
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2017\\templates\\Part.prtdot", 0, 0, 0);

            //Create sketches for extruded surface feature
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.03891024234798, 0.02968528649877, 0.0003646590412283, false, 0, null, 0);
            swModel.ClearSelection2(true);
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(-0.05517876768764, 0.008130204900836, 0, -0.02399076855985, -0.0155939995639, 0);
            swModel.ClearSelection2(true);
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(-0.003731897331531, 0.008130204900836, 0, 0.0285223581767, -0.02998846069981, 0);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.053579, 0.013995, 0.0, 0.06819, 0.018462, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);
            swModel.ShowNamedView2("*Trimetric", 8);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);

            // Create a blind surface extrude
            // in two directions from the selected sketch
            // in a direction normal to the selected sketch plane
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeatureManager.FeatureExtruRefSurface3(false, false, (int)swStartConditions_e.swStartSketchPlane, 0, (int)swEndConditions_e.swEndCondBlind, (int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, true, false,
            false, false, 0.4, 0, false, false, false, false, false, false,
            false, false);
            swModel.ClearSelection2(true);

            // Get Surface-Extrude1 feature
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            status = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swSurfExtrudeFeature = (SurfExtrudeFeatureData)swFeature.GetDefinition();

            //Access Surface-Extrude1 feature data
            swSurfExtrudeFeature.AccessSelections(swModel, null);

            Debug.Print(swFeature.Name);
            Debug.Print("  Depth:");
            Debug.Print("    Forward direction: " + swSurfExtrudeFeature.GetDepth(true));
            Debug.Print("    Reverse direction: " + swSurfExtrudeFeature.GetDepth(false));
            Debug.Print("  End condition as defined in swSurfaceExtendEndCond_e:");
            Debug.Print("    Forward direction: " + swSurfExtrudeFeature.GetEndCondition(true));
            Debug.Print("    Reverse direction: " + swSurfExtrudeFeature.GetEndCondition(false));
            Debug.Print("  Reverse offset enabled:");
            Debug.Print("    Forward direction? " + swSurfExtrudeFeature.GetReverseOffset(true));
            Debug.Print("    Reverse direction? " + swSurfExtrudeFeature.GetReverseOffset(false));
            Debug.Print("  Translate surface setting enabled:");
            Debug.Print("    Forward direction? " + swSurfExtrudeFeature.GetTranslateSurface(true));
            Debug.Print("    Reverse direction? " + swSurfExtrudeFeature.GetTranslateSurface(false));
            Debug.Print("  Surface extruded in both directions? " + swSurfExtrudeFeature.BothDirections);
            Debug.Print("  Extrusion reversed? " + swSurfExtrudeFeature.ReverseDirection);
            Debug.Print("  Direction 1 end:");
            Debug.Print("    Capped? " + swSurfExtrudeFeature.D1CapEnd);
            Debug.Print("    Drafted? " + swSurfExtrudeFeature.D1DraftOn);
            if (swSurfExtrudeFeature.D1DraftOn)
            {
                Debug.Print("      Angle: " + swSurfExtrudeFeature.D1DraftAngle);
                Debug.Print("      Inward (false) or outward (true)? " + swSurfExtrudeFeature.D1DraftOutward);
            }
            Debug.Print("  Direction 2 end:");
            Debug.Print("    Capped? " + swSurfExtrudeFeature.D2CapEnd);
            Debug.Print("    Drafted? " + swSurfExtrudeFeature.D2DraftOn);
            if (swSurfExtrudeFeature.D2DraftOn)
            {
                Debug.Print("      Angle: " + swSurfExtrudeFeature.D2DraftAngle);
                Debug.Print("      Inward (false) or outward (true)? " + swSurfExtrudeFeature.D2DraftOutward);
            }
            Debug.Print("  Delete original face? " + swSurfExtrudeFeature.DeleteOriginalFace);
            Debug.Print("  Knit extrusion result? " + swSurfExtrudeFeature.KnitResult);

            //Release Surface-Extrude1 feature data
            swSurfExtrudeFeature.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

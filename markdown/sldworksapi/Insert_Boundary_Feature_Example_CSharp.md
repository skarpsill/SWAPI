---
title: "Insert Boundary Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Boundary_Feature_Example_CSharp.htm"
---

# Insert Boundary Feature Example (C#)

This example shows how to insert and modify a boundary feature.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates two boss-extrude features.
// 3. Selects a face on each boss-extrude feature.
// 4. Creates a boundary feature using the the selected faces.
// 5. Gets and sets some boundary feature data.
// 6. Examine the Immediate window, FeatureManager design tree,
//    and the graphics area.
//-------------------------------------------------------------------
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
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            SketchManager swSketchMgr = default(SketchManager);
            BoundaryBossFeatureData swBoundaryBossFeatureData = default(BoundaryBossFeatureData);
            bool status = false;
            object[] sketchLines = null;
            int nbrCurves = 0;
            object directionVectorEntity = null;
            int directionVectorEntityType = 0;
            int tangencyType = 0;
            object[] d1Curves = null;
            int curveType = 0;
            int i = 0;

            //Open new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            //Create two boss-extrude features
            //and boundary feature
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.107624731933299, 0.0371047716348016, 0, -0.083196263303762, -0.00987284730888405, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, false, 0, 0, 0.0508, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.0391822613366912, 0.0227443468893966, 0, 0.0479123594660678, -0.0893283426445919, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swFeature = (Feature)swFeatureMgr.FeatureExtrusion3(true, false, false, 0, 0, 0.0508, 0.0508, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0831962633037051, -0.000743092842242277, 0.0342529447572133, false, 8193, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0391822613366344, -0.00670639010576224, 0.0375699693011029, true, 16385, null, 0);
            swFeatureMgr.SetNetBlendCurveData(0, 0, 0, 0, 1, true);
            swFeatureMgr.SetNetBlendCurveData(0, 1, 0, 0.26179938779915, 1, true);
            swFeatureMgr.SetNetBlendDirectionData(0, 32, 0, false, false);
            swFeatureMgr.SetNetBlendDirectionData(1, 32, 0, false, false);
            swFeatureMgr.InsertNetBlend(1, 2, 0, false, 0.0001, true, true, true, true, false,
            -1, -1, false, -1, false, false, -1, false, -1, true);

            //Get boundary feature
            //Get and set some of its data
            status = swModelDocExt.SelectByID2("Boundary1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swBoundaryBossFeatureData = (BoundaryBossFeatureData)swFeature.GetDefinition();
            Debug.Print("Name of feature: " + swFeature.Name);
            swModel.ClearSelection2(true);
            status = swBoundaryBossFeatureData.AccessSelections(swModel, null);
            //Get number of curves
            nbrCurves = swBoundaryBossFeatureData.GetCurvesCount((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First);
            Debug.Print("  Number of curves in Direction 1: " + nbrCurves);
            if (nbrCurves >= 0)
            {
                //Get tangency type
                tangencyType = swBoundaryBossFeatureData.GetGuideTangencyType((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0);
                if (tangencyType == (int)swBoundaryBossTangencyType_e.swBoundaryBossTangency_DirectionVector)
                {
                    directionVectorEntity = swBoundaryBossFeatureData.GetDirectionVector((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0);
                    status = swSelectionMgr.AddSelectionListObject(directionVectorEntity, null);
                    directionVectorEntityType = swSelectionMgr.GetSelectedObjectType3(1, -1);
                    Debug.Print("  Type of entity selected for Direction Vector for curve 1 in Direction 1: " + directionVectorEntityType);
                }
                else
                {
                    Debug.Print("  Tangency type for curve 1 in Direction 1: " + tangencyType);
                    Debug.Print("    NOTE: Tried to get entity for Direction Vector. Failed because");
                    Debug.Print("    tangency type must be 2 (swBoundaryBossTangencyType_e.swBoundaryBossTangency_DirectionVector),");
                    Debug.Print("    so type of entity used for Direction Vector is not available.");
                }
            }
             //Get and set draft angle
            Debug.Print("  Original draft angle for curve 1 in Direction 1: " + swBoundaryBossFeatureData.GetDraftAngle((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0));
            swBoundaryBossFeatureData.SetDraftAngle((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0, 0.015);
            Debug.Print("  Modified draft angle for curve 1 in Direction 1: " + swBoundaryBossFeatureData.GetDraftAngle((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0));
            //Flip draft angle
            swBoundaryBossFeatureData.SetDraftAngleReverseDirection((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0, true);
            Debug.Print("  Draft angle flipped for curve 1 in Direction 1: " + swBoundaryBossFeatureData.GetDraftAngleReverseDirection((int)swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0));
            //Get curves
            swModel.ClearSelection2(true);
            d1Curves = (object[])swBoundaryBossFeatureData.D1Curves;
            for (i = 0; i < nbrCurves; i++)
            {
                status = swSelectionMgr.AddSelectionListObject(d1Curves[i], null);
                curveType = swSelectionMgr.GetSelectedObjectType3(i + 1, -1);
                Debug.Print("  Curve " + (i + 1) + " type: " + curveType);
            }
            Debug.Print("  Is thin feature? " + swBoundaryBossFeatureData.IsThinFeature());
            status = swFeature.ModifyDefinition(swBoundaryBossFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

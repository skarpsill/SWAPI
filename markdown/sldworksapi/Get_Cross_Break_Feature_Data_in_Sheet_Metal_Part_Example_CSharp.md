---
title: "Get Cross Break Feature Data in Sheet Metal Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm"
---

# Get Cross Break Feature Data in Sheet Metal Part Example (C#)

This example shows how to get cross break feature data in a sheet metal part.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a sheet metal part with a cross break feature.
// 2. Iterates over all features in the part and gets the
//    cross break feature.
// 3. Names the cross break feature's face.
// 4. Prints to the Immediate window this cross break
//    feature data:
//    * Name of the face
//    * Whether its direction is reversed
//    * Radius
//    * Angle
// 5. Examine the Immediate window.
//----------------------------------------------------------------
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
            PartDoc swPart = default(PartDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            SketchManager swSketchManager = default(SketchManager);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            CustomBendAllowance swCustomBendAllowance = default(CustomBendAllowance);
            Feature swFeature = default(Feature);
            CrossBreakFeatureData swCrossBreakFeatureData = default(CrossBreakFeatureData);
            Face2 swFace = default(Face2);
            Entity swEntity = default(Entity);
            object[] sketchLines = null;
            object[] features = null;
            string faceName = null;
            bool status = false;
            int i = 0;

            //Create sheet metal part with cross break feature
            swPart = (PartDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\part.prtdot", 0, 0, 0);
            swModel = (ModelDoc2)swPart;
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            status = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(0, 0, 0, 0.112582864792503, -0.0690084337349398, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);
            swModel.ShowNamedView2("*Trimetric", 8);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swCustomBendAllowance = (CustomBendAllowance)swFeatureManager.CreateCustomBendAllowance();
            swCustomBendAllowance.KFactor = 0.5;
            swFeature = (Feature)swFeatureManager.InsertSheetMetalBaseFlange2(0.0007366, false, 0.01905, 0.00508, 0.00254, false, 0, 0, 1, swCustomBendAllowance,
            false, 0, 0.0001, 0.0001, 0.5, true, false, true, true);
            status = swModelDocExt.SelectByID2("Base-Flange1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0440948432654409, -0.0302769643316765, 0, true, 0, null, 0);
            swFeature = (Feature)swFeatureManager.InsertCrossBreak(1.5707963267949, 0.000635);
            swModel.ClearSelection2(true);

            //Get the cross break feature
            //by iterating over all features
            features = (object[])swFeatureManager.GetFeatures(true);
            for (i = 0; i < features.Length; i++)
            {
                swFeature = (Feature)features[i];
                if (swFeature.GetTypeName2() == "CrossBreak")
                {
                    swCrossBreakFeatureData = (CrossBreakFeatureData)swFeature.GetDefinition();
                    swCrossBreakFeatureData.AccessSelections(swModel, null);
                    swFace = (Face2)swCrossBreakFeatureData.Face;
                    swEntity = (Entity)swFace;
                    faceName = "CrossBreakFace";
                    status = swPart.SetEntityName(swEntity, faceName);
                    faceName = swModel.GetEntityName(swEntity);
                    Debug.Print("Cross break feature data:");
                    Debug.Print("  Name of face: " + faceName);
                    Debug.Print("  Reverse direction: " + swCrossBreakFeatureData.ReverseDirection);
                    Debug.Print("  Radius: " + swCrossBreakFeatureData.BreakRadius);
                    Debug.Print("  Angle: " + swCrossBreakFeatureData.BreakAngle);
                    swCrossBreakFeatureData.ReleaseSelectionAccess();
                }
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

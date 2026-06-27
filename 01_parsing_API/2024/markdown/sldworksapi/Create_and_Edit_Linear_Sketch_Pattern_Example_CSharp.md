---
title: "Create and Edit Linear Sketch Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Edit_Linear_Sketch_Pattern_Example_CSharp.htm"
---

# Create and Edit Linear Sketch Pattern Example (C#)

This example shows how to create and edit a linear sketch pattern.

```
//---------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Creates an extrude feature.
// 2. Opens a sketch on the front face of the extrude feature.
// 3. Creates a linear sketch pattern.
// 4. Closes the sketch.
// 5. Opens the linear sketch pattern.
// 6. Deletes an entity (i.e., Line3) in each instance of the linear
//    sketch pattern.
// 7. Examine the graphics area.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureMgr = default(FeatureManager);
            object vSkLines = null;
            bool boolstatus = false;
            int longstatus = 0;

            // Reset the counts for untitled documents for this macro
            swApp.ResetUntitledCount(0, 0, 0);

            // Create part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part1", false, ref longstatus);
            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Select the Front plane
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);

            // Open a sketch and sketch a rectangle
            swSketchMgr = swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            swModel.ClearSelection2(true);
            vSkLines = swSketchMgr.CreateCornerRectangle(-0.07606134448097, 0.04933121484909, 0, 0.07649598073515, -0.0510697598658, 0);

            // Change view orientation and clear all selections
            swModel.ShowNamedView2("*Trimetric", 8);
            swModel.ClearSelection2(true);

            // Select the sketch entities to extrude
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);

            // Create the extrude feature
            swFeatureMgr = swModel.FeatureManager;
            swFeature = swFeatureMgr.FeatureExtrusion2(true, false, false, 0, 0, 0.0508, 0.381, false, false, false,
            false, 0.01745329251994, 0.01745329251994, false, false, false, false, true, true, true, 0, 0, false);

            // Fit the model in the graphics area
            swModel.ViewZoomtofit2();

            // Select the face on the extrude feature and sketch the entities to pattern
            swModel.ShowNamedView2("*Front", 1);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.05428715407583, 0.03314479661076, 0.05079999999998, false, 0, null, 0);
            vSkLines = swSketchMgr.CreateCornerRectangle(-0.00838865116811, 0.00609746454014, 0, 0.00738895920642, -0.007221297464333, 0);

            // Create a linear sketch pattern using the newly
            // sketched rectangle as the linear pattern seed feature
            boolstatus = swSketchMgr.CreateLinearSketchStepAndRepeat(2, 2, 0.0254, 0.0254, 0.296705972839, 1.134464013796, "", true, true, false, true, true);
            swModel.ClearSelection2(true);

            // Close the sketch
            swSketchMgr.InsertSketch(true);

            // Select an entity in the linear sketch seed
            // pattern and open the linear sketch pattern to edit
            boolstatus = swModelDocExt.SelectByID2("Line3@Sketch2", "EXTSKETCHSEGMENT", -0.002651338304644, -0.007221297464333, 0, false, 0, null, 0);
            swModel.EditSketch();

            // Delete the Line3 sketch entity from each instance
            // of the linear sketch pattern
            boolstatus = swSketchMgr.EditLinearSketchStepAndRepeat(3, 2, 0.0254, 0.0254, 0.296705972839, 1.134464013796, "", false, false, false, true, true, "Line2_Line1_Line4_");

        }

        public SldWorks swApp;

    }
}
```

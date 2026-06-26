---
title: "Select Multiple Sketch Segments for Sweep Path Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Paths_for_Sweep_Path_Example_CSharp.htm"
---

# Select Multiple Sketch Segments for Sweep Path Example (C#)

This example shows how to select multiple sketch segments for the path for a sweep feature.

```
//--------------------------------------------------------
// Preconditions: Verify that the part template exists.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates:
//    * sketch of a circle.
//    * sketch of a line.
//    * another sketch of a line.
// 3. Selects the sketch of the circle for the sweep profile.
// 4. Selects the sketches of the lines for the sweep path
//    and groups them as an object.
// 5. Creates a sweep feature.
// 6. Examine the FeatureManager design tree and graphics
//    area.
//---------------------------------------------------------
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
            SketchSegment swSketchSegment = default(SketchSegment);
            SketchManager swSketchManager = default(SketchManager);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchManager = (SketchManager)swModel.SketchManager;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;

            //Create sketch of circle for the sweep profile
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.002394, -0.006333, 0.0);
            swSketchManager.InsertSketch(true);

            //Create sketches of lines for the sweep path
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.0, 0.0, 0.0, 0.088481, 0.035691, 0.0);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.088481, 0.035691, 0.0, 0.079214, 0.076295, 0.0);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);

            //Select the sketch of the circle for the sweep profile
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -0.00586834883582351, -0.00337646707201764, 0, false, 1, null, 0);

            //Select the sketches of the lines for the sweep path and group them as an object
            status = swModelDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 0.0379259971310087, 0.0152983890733924, 0, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("Line1@Sketch3", "EXTSKETCHSEGMENT", 0.0848435978763939, 0.0516285284155501, 0, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("Unknown", "SELOBJGROUP", 0, 0, 0, true, 4, null, 0);

            //Create the sweep feature
            swFeature = (Feature)swFeatureManager.InsertProtrusionSwept4(false, false, 0, false, false, 0, 0, false, 0, 0,
            0, 0, true, true, true, 0, true, false, 0, 0);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

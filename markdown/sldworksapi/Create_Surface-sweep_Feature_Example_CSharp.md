---
title: "Create Surface-sweep Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Surface-sweep_Feature_Example_CSharp.htm"
---

# Create Surface-sweep Feature Example (C#)

This example shows how to create a surface-sweep feature.

```
//---------------------------------------------------
// Preconditions: Verify that the part template exists.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates two sketches.
// 3. Inserts a surface-sweep feature.
// 4. Examine the FeatureManager design tree and
//    graphics area.
//---------------------------------------------------

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
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            bool status = false;

            //Open new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\templates\\part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create a sketch
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.0, 0.0, 0.068491, 0.049604, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.068491, 0.049604, 0.0, 0.10923, 0.112837, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.10923, 0.112837, 0.0, 0.194652, 0.154023, 0.0);
            swSketchManager.InsertSketch(true);

            swModel.ViewZoomtofit2();
            swModel.ShowNamedView2("*Isometric", 7);
            swModel.ClearSelection2(true);

            //Create another sketch
            status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.0, 0.0, 0.0, 0.021042, 0.091756, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.021042, 0.091756, 0.0, 0.098366, 0.085093, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.098366, 0.085093, 0.0, 0.143062, 0.122696, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            //Insert surface sweep
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 4, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertSweepSurface3(false, 0, false, false, 0, 0, 0, true, true, 0,
            true, false, 0, 0);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

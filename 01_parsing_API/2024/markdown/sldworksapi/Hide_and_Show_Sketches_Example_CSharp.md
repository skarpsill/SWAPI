---
title: "Hide and Show Sketches Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_Sketches_Example_CSharp.htm"
---

# Hide and Show Sketches Example (C#)

This example shows how to hide and show sketches in a model.

```
//---------------------------------------
// Preconditions: Run the macro.
//
// Postconditions:
// 1. Opens a new part document and
//    creates two sketches.
// 2. Selects one sketch and hides it.
// 3. Examine the graphics area to verify
//    and press F5.
// 4. Selects the hidden sketch and shows
//    it.
//--------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace BlankUnBlankSketchesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            object[] sketchLines = null;
            SketchSegment swSketchSegment = default(SketchSegment);
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2013\\templates\\Part.prtdot", (int)swDwgPaperSizes_e.swDwgPaperAsizeVertical, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;

            // Sketch a rectangle
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.0684166678777842, 0.0376953152008355, 0, -0.0273535635019471, 0.00483994917499331, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            // Sketch a circle
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.044426, 0.079347, 0.0, 0.057359, 0.06229, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);

            swModel.ClearSelection2(true);

            // Select a sketch and hide it
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.BlankSketch();

            System.Diagnostics.Debugger.Break();
            // Examine the graphics area
            // to verify that the selected sketch
            // is hidden
            // Press F5

            swModel.ClearSelection2(true);

            // Select the just hidden sketch again
            // and show it
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.UnblankSketch();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

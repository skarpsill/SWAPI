---
title: "Offset Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Offset_Example_CSharp.htm"
---

# Offset Sketch Example (C#)

This example shows how to offset a sketch.

```
//----------------------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Creates a new part.
// 2. Sketches a line.
// 3. Offsets the line 2.54 mm in both directions.
// 4. Examine the graphics area.
// ---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Runtime.InteropServices;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        SketchManager swSketchManager;
        ModelDocExtension swModelDocExt;
        SketchSegment swSketchSegment;
        bool status;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", -0.0770466366627886, 0.00233041566204965, 0.0390732100788036, false, 0, null, 0);
            swModel.ClearSelection2(true);

            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.081532, 0.028203, 0.0, -0.029228, -0.017264, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.029228, -0.017264, 0.0, 0.035382, -0.025468, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.035382, -0.025468, 0.0, 0.087008, -0.070346, 0.0);
            swModel.ClearSelection2(true);

            status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, false, 1, null, 0);
            status = swSketchManager.SketchOffset2(0.00254, true, true, (int)swSkOffsetCapEndType_e.swSkOffsetArcCaps, (int)swSkOffsetMakeConstructionType_e.swSkOffsetMakeBothConstruction, true);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

        }

        public SldWorks swApp;
    }

}
```

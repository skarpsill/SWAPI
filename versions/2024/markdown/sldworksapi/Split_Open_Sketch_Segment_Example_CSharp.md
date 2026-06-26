---
title: "Split Open Sketch Segment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_Open_Sketch_Segment_Example_CSharp.htm"
---

# Split Open Sketch Segment Example (C#)

This example shows how to split an open sketch segment.

```vb
 //---------------------------------------------------------------
 // Preconditions:
 // 1. Open a new part document.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens a sketch.
 // 2. Creates a line segment.
 // 3. Splits the line segment into two segments.
 // 4. Examine the Immediate window.
 //----------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace SplitOpenSegment_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SketchSegment swSketchSegment;
         object[] skSegmentArray;

         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swApp.SetUserPreferenceToggle(int swUserPreferenceToggle_e.swSketchInference, false);

             boolstatus = swModel.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  false, 0,  null, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);

             // Create a line
             swSketchSegment = swModel.SketchManager.CreateLine(-0.055964, 0.033212, 0.0, 0.102938, -0.014129, 0.0);
             swModel.ViewZoomtofit2();

             skSegmentArray = (object[])swModel.SketchManager.SplitOpenSegment(0.02, 0.01, 0.0);

             // Close the sketch and rebuild
             swModel.SketchManager.Insert3DSketch(true);
            Debug.Print("Number of segments in sketch = " + skSegmentArray.Length);

         }

         public SldWorks swApp;

     }
 }
```

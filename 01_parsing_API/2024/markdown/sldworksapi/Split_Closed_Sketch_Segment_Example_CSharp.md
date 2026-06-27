---
title: "Split Closed Sketch Segment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_Closed_Sketch_Segment_Example_CSharp.htm"
---

# Split Closed Sketch Segment Example (C#)

This example shows how to split a closed sketch segment.

```vb
 //---------------------------------------------------------------
 // Preconditions:
 // 1. Open a new part document.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens a sketch.
 // 2. Creates a closed spline.
 // 3. Splits the spline into two segments.
 // 4. Examine the Immediate window.
 //----------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace SplitClosedSegment_CSharp.csproj
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

             object pointArray = null;
             double[] points = new double[21];
             points[0] = -0.0243607314462504;
             points[1] = 0.0404155099449417;
             points[2] = 0;
             points[3] = -0.000849151208568891;
             points[4] = 0.0470352752545802;
             points[5] = 0;
             points[6] = 0;
             points[7] = 0.0395024388677502;
             points[8] = 0;
             points[9] = -0.00530037270987752;
             points[10] = 0.0358501545589842;
             points[11] = 0;
             points[12] = -0.00712651486426054;
             points[13] = 0.0283173181721542;
             points[14] = 0;
             points[15] = -0.023219392599761;
             points[16] = 0.0295727909032925;
             points[17] = 0;
             points[18] = -0.0243607314462504;
             points[19] = 0.0404155099449417;
             points[20] = 0;
             pointArray = points;

             swSketchSegment = swModel.SketchManager.CreateSpline((pointArray));
             swModel.ViewZoomtofit2();

             skSegmentArray = (object[])swModel.SketchManager.SplitClosedSegment(-0.0243607314462504, 0.0404155099449417, 0.0, -0.023219392599761, 0.0295727909032925, 0.0);

             // Close the sketch and rebuild
             swModel.SketchManager.Insert3DSketch(true);

            Debug.Print("Number of segments in sketch = " + skSegmentArray.Length);

         }

         public SldWorks swApp;

     }
 }
```

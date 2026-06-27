---
title: "Trim Sketch Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Trim_Sketch_Entities_Example_CSharp.htm"
---

# Trim Sketch Entities Example (C#)

This example shows how to trim a sketch to a corner.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Ensure the specified template exists.
 //
 // Postconditions:
 // 1. Opens a new part document.
 // 2. Sketches some lines.
 // 3. Examine the sketch, then press
 //    F5.
 // 4. Selects two lines and trims them
 //    to a corner.
 // 5. Examine the sketch to verify.
 //-----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace SketchTrimCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SketchManager swSketchMgr = default(SketchManager);
             SketchSegment swSketchSegment = default(SketchSegment);
             bool status = false;

             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2018\\templates\\Part.prtdot", 0, 0, 0);
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swSketchMgr = (SketchManager)swModel.SketchManager;

             // Create sketch of lines
             status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
             swSketchMgr.InsertSketch(true);
             swModel.ClearSelection2(true);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.055275, 0.03236, 0.0, 0.027405, 0.03236, 0.0);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.027405, 0.03236, 0.0, 0.027405, -0.026476, 0.0);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.027405, -0.026476, 0.0, -0.055275, -0.026476, 0.0);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.055275, -0.026476, 0.0, -0.055275, -0.070758, 0.0);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.055275, -0.070758, 0.0, 0.027405, -0.070758, 0.0);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.027405, -0.070758, 0.0, 0.076642, 0.03236, 0.0);
             swModel.ClearSelection2(true);

             System.Diagnostics.Debugger.Break();
             // Examine the sketch before trimming
             // the selected lines to a corner
             // Press F5
             // Select two lines to trim to a corner

             status = swModelDocExt.SelectByID2("Line6", "SKETCHSEGMENT", 0.0391723509933775, -0.0466042594822396, 0, true, 0, null, 0);
             status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.0193539283564118, -0.0264761739915713, 0, true, 0, null, 0);
             status = swSketchMgr.SketchTrim((int)swSketchTrimChoice_e.swSketchTrimCorner, 0, 0, 0);
             swModel.ClearSelection2(true);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

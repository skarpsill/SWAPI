---
title: "Create Path Length Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Path_Length_Dimension_Example_CSharp.htm"
---

# Create Path Length Dimension Example (C#)

This example shows how to create a path length dimension.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a new part document.
 //
 // Postconditions: Select Sketch1 in the FeatureManager design tree to
 // see the path length dimension of 15.75.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace CreatePathLengthDim_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         DisplayDimension myDisplayDim;
         bool boolstatus;

         public void Main()
         {
             swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swInputDimValOnCreate, false);

             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  false, 0,  null, 0);
             Part.SketchManager.InsertSketch(true);
             Part.ClearSelection2(true);
             object vSkLines = null;
             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.075, 0.05, 0, 0.05, -0.025, 0);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = Part.SketchManager.MakeSketchChain();
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0.00661546453402301, 0.0508003665223665, 0,  false, 0,  null, 0);

             myDisplayDim = (DisplayDimension)Part.Extension.AddPathLengthDim(-0.0580395474035344, 0.0841706952643316, 0);
             Part.SketchManager.InsertSketch(true);

         }

         public SldWorks swApp;

     }

 }
```

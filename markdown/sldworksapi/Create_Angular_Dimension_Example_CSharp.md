---
title: "Create Angular Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Angular_Dimension_Example_CSharp.htm"
---

# Create Angular Dimension Example (C#)

This example shows how to add an angular display dimension to a sketch.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\box.sldprt.
 // 2. Press F8 repeatedly to step through the macro.
 //
 // Postconditions:
 // 1. Edits Sketch1.
 // 2. Creates an angular dimension.
 // 3. Displays the dimension for:
 //    * Angle defined by the selected sketch segment and an extension line
 //      that is drawn to the right of the selected sketch point
 //      (Direction = swSmartDimensionDirection_Right)
 //    * Explementary angle
 //    * Vertically opposite angle
 //
  // NOTE: Because the model is used elsewhere, do not save changes to it.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace AddDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         DisplayDimension myDisplayDim;

         bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;
             System.Diagnostics.Debugger.Break();
             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
             Part.EditSketch();

             boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -0.0672289031567236, 0.0180603779387131, 0.0184698306816742, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Point1", "SKETCHPOINT", -0.0811067833265636, 0.0389478433654258, 0, true, 0, null, 0);

             myDisplayDim = (DisplayDimension)Part.Extension.AddDimension(-0.0456250220540824, 0, 0.00150965590938767, (int)swSmartDimensionDirection_e.swSmartDimensionDirection_Right);
             myDisplayDim.ExplementaryAngle();
             myDisplayDim.VerticallyOppositeAngle();

             Part.SketchManager.InsertSketch(true);

         }

         public SldWorks swApp;
     }
 }
```

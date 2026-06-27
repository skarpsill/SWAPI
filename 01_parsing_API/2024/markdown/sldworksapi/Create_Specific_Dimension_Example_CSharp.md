---
title: "Create Specific Dimension in a Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Specific_Dimension_Example_CSharp.htm"
---

# Create Specific Dimension in a Sketch Example (C#)

This example shows how to add an angular display dimension to a sketch.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\box.sldprt.
 //
 // Postconditions:
 // 1. Edits Sketch1.
 // 2. Selects two intersecting lines.
 // 3. Creates an angular display dimension at the specified location in the
 //    sketch.
 // 4. Inserts Sketch1.
 // 5. Inspect Sketch1 in the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes to it.
 // ---------------------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;
 using System.Data;
 using System.Diagnostics;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace CreateAngDim_CSharp
 {
     public partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         DisplayDimension myDisplayDim;
         bool boolstatus;
         int err;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);

             Part.EditSketch();

             boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", -0.0509671483361161, -0.0109842011554073, 0.0296211826739789, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -0.0770411440149667, 0.00496030150977761, 0.0325476150359756, true, 0, null, 0);
             myDisplayDim = (DisplayDimension)Part.Extension.AddSpecificDimension(-0.0456250220540824, 0, 0.00150965590938767, (int)swDimensionType_e.swAngularDimension, err);

             Part.SketchManager.InsertSketch(true);

         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```

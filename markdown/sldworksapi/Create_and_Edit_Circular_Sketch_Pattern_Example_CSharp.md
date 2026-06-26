---
title: "Create and Edit Circular Sketch Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm"
---

# Create and Edit Circular Sketch Pattern Example (C#)

This example shows how to create and edit a circular sketch pattern.

//------------------------------------------------------------ // Preconditions: Verify that the specified part document template // exists. // // Postconditions: // 1. Opens a new part document and creates a sketch. // 2. Inserts a circular sketch pattern of four instances. // 3. Closes the sketch. // 4. Opens the circular sketch pattern for editing. // 5. Deletes an instance of the circular sketch pattern, leaving // three instances. // 6. Examine the graphics area. //------------------------------------------------------------

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace Macro1CSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchManager swSketchMgr = default(SketchManager);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchSegment swSketchSegment = default(SketchSegment);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object vSkLines = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int longstatus = 0;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Reset the counts for untitled documents for this macro
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.ResetUntitledCount(0, 0, 0);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a part document
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.ActivateDoc2("Part1", false, ref longstatus);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr = swModel.SketchManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Sketch a circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchSegment = swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.045549, 0.013926, 0.0);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Clear any selections and change
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// the view orientation to Front
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Front", 1);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a rectangle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vSkLines = swSketchMgr.CreateCornerRectangle(-0.005867589431389, 0.03694408160504, 0, 0.004563680668858, 0.02673012963188, 0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a circular sketch pattern
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// using the rectangle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swSketchMgr.CreateCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 4, 1.570796326795, true, "", true, true, true);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Close the sketch and rebuild
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(true);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select an entity in the circular sketch pattern
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and open the circular sketch pattern to edit it
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.002390499397973, 0.03694408160504, 0, false, 0, null, 0);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditSketch();

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Delete an instance of the circular
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// sketch pattern and close the sketch
  kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swSketchMgr.EditCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 3, 1.570796326795, true, "", true, true, true, "Line2_Line1_Line4_Line3_"kadov_tag{{</spaces>}});
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

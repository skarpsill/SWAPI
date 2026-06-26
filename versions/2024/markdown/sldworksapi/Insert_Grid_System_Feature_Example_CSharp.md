---
title: "Insert Grid System Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Grid_System_Feature_Example_CSharp.htm"
---

# Insert Grid System Feature Example (C#)

This example shows how to insert a Grid System feature into a model.

```vb
//-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified part template exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens a new part document.
 // 2. Creates a sketch of a circle.
 // 3. Inserts GridSystem1, which contains Surface-Extrude1, Level1, Level2,
 //    and two derived sketches, in the FeatureManager design tree.
 // 4. Sets the height of each level of the surface extrude to 50.0 mm.
 // 5. Examine the Immediate window and graphics area.
 // 6. Expand GridSystem1 in FeatureManager design tree.
 //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace InsertGridFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         Feature GridFeature;
         ModelDoc2 Part;
         ModelView myModelView;
         SketchSegment skSegment;
         bool boolstatus;
         int longstatus;

         public void Main()
         {

             swApp.ResetUntitledCount(0, 0, 0);
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
             swApp.ActivateDoc2("Part1", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             myModelView = (ModelView)Part.ActiveView;
             myModelView.FrameLeft = 0;
             myModelView.FrameTop = 0;
             myModelView.FrameState = (int)swWindowState_e.swWindowMaximized;
             Part.ShowNamedView2("*Isometric", 7);

             skSegment = Part.SketchManager.CreateCircle(-0.019633, 0.076084, 0.0, -0.001997, 0.081475, 0.0);
             Part.SketchManager.InsertSketch(true);

             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);

             object offsetArray = null;
             double[] heightsArray = new double[2];
             heightsArray[0] = 0.05;
             heightsArray[1] = 0.05;
             offsetArray = heightsArray;

             GridFeature = Part.FeatureManager.InsertGridFeature((offsetArray));
             Debug.Print(GridFeature.Name + " was created.");

             Part.ViewZoomtofit();
         }

         public SldWorks swApp;

     }
 }
```

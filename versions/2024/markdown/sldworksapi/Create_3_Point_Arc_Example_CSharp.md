---
title: "Create 3-Point Arc Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3_Point_Arc_Example_CSharp.htm"
---

# Create 3-Point Arc Example (C#)

This example shows how to create a 3-point arc in a sketch.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a new part.
 //
 // Postconditions:
 // 1. Creates a 3-point arc in Sketch1.
 // 2. Examine the graphics area and FeatureManager design tree.
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
 namespace Create3PointArc_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         SketchSegment skSegment;
         bool boolstatus;
         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             Part.SketchManager.InsertSketch(true);
             boolstatus = Part.Extension.SelectByID2("Top Plane",  "PLANE", -0.0603680341302297, 0.00853710569474597, 0.0260554052320825,  false, 0,  null, 0);
             Part.ClearSelection2(true);
             skSegment = Part.SketchManager.Create3PointArc(-0.043992, 0.026681, 0.0, 0.033828, 0.037798, 0.0, 0.01604, 0.014611, 0.0);
             Debug.Print("The sketch is 3D? " + skSegment.GetSketch().Is3D());
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);
         }

         public SldWorks swApp;
     }
 }
```

---
title: "Get Sketch Arc Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Arc_Data_Example_CSharp.htm"
---

# Get Sketch Arc Data Example (C#)

This example shows how to get sketch arc data.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Creates a new model document with a sketch of an open arc.
 // 2. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
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

 namespace CreateSketchArc_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         SketchArc skArcSegment;
         ModelDoc2 Part;
         SketchPoint centerPt;
         SketchPoint startPt;
         double[] vNormalVector;
         SketchPoint endPt;

         bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             Part = (ModelDoc2)swApp.ActiveDoc;

             Part.SketchManager.InsertSketch(true);
             boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.0405700227306837, 0.02417279486491, 0.00498560798672921, false, 0, null, 0);
             Part.ClearSelection2(true);

             skArcSegment = (SketchArc)Part.SketchManager.CreateArc(-0.017822, 0.012246, 0.0, 0.010653, 0.040124, 0.0, -0.011244, -0.027057, 0.0, -1);
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);

             centerPt = (SketchPoint)skArcSegment.GetCenterPoint2();
             Debug.Print("Center point: " + centerPt.X + ", " + centerPt.Y + ", " + centerPt.Z);

             startPt = (SketchPoint)skArcSegment.GetStartPoint2();
             Debug.Print("Start point: " + startPt.X + ", " + startPt.Y + ", " + startPt.Z);

             endPt = (SketchPoint)skArcSegment.GetEndPoint2();
             Debug.Print("End point: " + endPt.X + ", " + endPt.Y + ", " + endPt.Z);

             vNormalVector = (double[])skArcSegment.GetNormalVector();
             Debug.Print("Normal vector: " + vNormalVector[0] + ", " + vNormalVector[1] + ", " + vNormalVector[2]);

             Debug.Print("Radius in mm: " + skArcSegment.GetRadius() * 1000.0);
             Debug.Print("Rotation direction (1 = counterclockwise, -1 = clockwise): " + skArcSegment.GetRotationDir());
             Debug.Print("Complete circle (1 = complete, 0 = partial arc): " + skArcSegment.IsCircle());

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

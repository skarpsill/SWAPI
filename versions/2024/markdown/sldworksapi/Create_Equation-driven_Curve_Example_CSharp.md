---
title: "Create Equation-driven Curve Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Equation-driven_Curve_Example_CSharp.htm"
---

# Create Equation-driven Curve Example (C#)

This example shows how to create and modify an equation-driven curve.

```vb
 //---------------------------------------------------------------
 // Preconditions:
  // 1. Open a new part document.
  // 2. Open the Immediate window.
  //
  // Postconditions:
  // 1. Creates a 2D sketch and creates an equation-driven spline of
  //    a sine curve.
  // 2. Examine the graphics area, then Press F5.
  // 3. Edits the curve and creates a cosine curve.
  // 4. Reduces the number of points in the spline.
  // 5. Examine the Immediate window and graphics area.
  //----------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace SimplifySketchSpline_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swExt;
         SelectionMgr swSelMgr;
         bool boolstatus;
         string y;
         double r1;
         double r2;
         bool rad;
         double ang;
         double xOff;
         double yOff;
         bool LockStart;
         bool LockEnd;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             boolstatus = swExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  false, 0,  null, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);

             SketchSegment skSegment = default(SketchSegment);
             skSegment = (SketchSegment)swModel.SketchManager.CreateEquationSpline2("", "sin(x)", "", "0", "6.28", false, 0, 0, 0, true,
             true);
             swModel.ViewZoomtofit2();

             System.Diagnostics.Debugger.Break();
              //Examine the graphics area, then press F5

             SketchSpline skSpline = default(SketchSpline);
             skSpline = (SketchSpline)skSegment;
             skSpline.GetEquationParameters(out y, out r1, out r2, out rad, out ang, out xOff, out yOff, out LockStart, out LockEnd);

             Debug.Print("y: " + y);
             Debug.Print("range start: " + r1);
             Debug.Print("range end: " + r2);
             Debug.Print("radian?: " + rad);
             Debug.Print("ang offset: " + ang);
             Debug.Print("x offset: " + xOff);
             Debug.Print("y offset: " + yOff);
             Debug.Print("lock start: " + LockStart);
             Debug.Print("lock end: " + LockEnd);

             // Change spline to a cosine curve
             y =  "cos(x)";
             skSpline.SetEquationParameters(y, r1, r2, rad, ang, xOff, yOff, LockStart, LockEnd);

             // Reduce the number of points in the spline
             skSpline.Simplify(0.0);

             swModel.SketchManager.InsertSketch(true);

         }

         public SldWorks swApp;

     }
 }
```

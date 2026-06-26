---
title: "Create Broken-Out Section Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_BreakOut_Section_Example_CSharp.htm"
---

# Create Broken-Out Section Example (C#)

This example shows how to create a broken-out section in a drawing view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing.
 // 2. Select Drawing View1.
 //
 // Postconditions: A broken-out section is created in Drawing View1
 // using the specified closed spline.
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
 namespace CreateBreakOutSection_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;
         object pointArray;
         double[] points = new double[12];
         SketchSegment skSegment;
         SelectData selectData = null;
         DrawingDoc dDoc;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             points[0] = -0.0544316967839374;
             points[1] = 0.0413619530906299;
             points[2] = 0;
             points[3] = 0.0530556603589196;
             points[4] = 0.0413619530906299;
             points[5] = 0;
             points[6] = 0.00783232107320536;
             points[7] = 0.00720299635749822;
             points[8] = 0;
             points[9] = -0.0544316967839374;
             points[10] = 0.0413619530906299;
             points[11] = 0;

             pointArray = points;

             skSegment = Part.SketchManager.CreateSpline((pointArray));
             skSegment.Select4(true, selectData);

             dDoc = (DrawingDoc)Part;
             dDoc.CreateBreakOutSection(0.00254);

             Part.ClearSelection2(true);
         }

         public SldWorks swApp;
     }

 }
```

---
title: "Create 2D Spline Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_2D_Spline_Example_CSharp.htm"
---

# Create 2D Spline Example (C#)

This topic shows how to create a 2D spline.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Open a new part.
 //
 // Postconditions:
 // 1. Creates a sketch of a 2D spline.
 // 2. Examine the graphics area.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace Create2DSpline_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModelDoc;
         ModelDocExtension swModelDocExt;
         int i;
         int j;
         double[] x = new double[6];
         double[] y = new double[6];

         bool boolstatus;

         public void Main()
         {
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModelDoc.Extension;
             boolstatus = swModelDocExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  false, 0,  null, 0);

             // Open sketch
             swModelDoc.InsertSketch2(true);

             // Calculate the values for x, y, and z

             for (i = 0; i <= 4; i++)
             {
                 x[i] = i;
                 y[i] = Math.Pow(i, 2) + 3 * i;
             }

             // Initialize the routine and sketch the first point of the spline at 0,0,0
             swModelDoc.SketchSpline(-1, 0, 0, 0);

             // Sketch four more points of the spline
             for (j = 4; j >= 0; j += -1)
             {
                 swModelDoc.SketchSpline(j, x[j], y[j], 0);
             }

             // Exit sketch
             swModelDoc.InsertSketch2(true);

         }

         public SldWorks swApp;

     }
 }
```

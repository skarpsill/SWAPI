---
title: "Insert Conic Curve Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Conic_Curve_Example_CSharp.htm"
---

# Insert Conic Curve Example (C#)

This example shows how to create a conic curve.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Verify that the specified part document template exists.
 //
 // Postconditions:
 // 1. Creates a new part.
 // 2. Inserts a conic curve in the part.
 // 3. Examine the graphics area.
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
 namespace InsertConic_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;

         public void Main()
         {
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             Part = (ModelDoc2)swApp.ActiveDoc;
             SketchSegment skSegment = default(SketchSegment);
             skSegment = Part.SketchManager.CreateConic(0.109436, 0.080614, 0.0, 0.048742, 0.022907, 0.0, -0.017812, 0.0, 0.0, -0.006092,
             -0.069601, 0.0);
             Part.SketchManager.InsertSketch(true);
             Part.ShowNamedView2("*Isometric", 7);
         }

         public SldWorks swApp;
     }
 }
```

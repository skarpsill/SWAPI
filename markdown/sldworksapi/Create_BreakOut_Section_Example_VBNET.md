---
title: "Create Broken-Out Section Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_BreakOut_Section_Example_VBNET.htm"
---

# Create Broken-Out Section Example (VB.NET)

This example shows how to create a broken-out section in a drawing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing.
 ' 2. Select Drawing View1.
 '
 ' Postconditions: A broken-out section is created in Drawing View1
 ' using the specified closed spline.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim pointArray As Object
     Dim points(11) As Double
     Dim skSegment As SketchSegment
     Dim selectData As SelectData

     Sub main()

         Part = swApp.ActiveDoc

         points(0) = -0.0544316967839374
         points(1) = 0.0413619530906299
         points(2) = 0
         points(3) = 0.0530556603589196
         points(4) = 0.0413619530906299
         points(5) = 0
         points(6) = 0.00783232107320536
         points(7) = 0.00720299635749822
         points(8) = 0
         points(9) = -0.0544316967839374
         points(10) = 0.0413619530906299
         points(11) = 0

         pointArray = points

         skSegment = Part.SketchManager.CreateSpline((pointArray))
         skSegment.Select4(True, selectData)

         Part.CreateBreakOutSection(0.00254)

         Part.ClearSelection2(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```

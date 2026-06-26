---
title: "Sketch Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Spline_Example_VB.htm"
---

# Sketch Spline Example (VBA)

This example shows how to sketch a spline.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Open a new part.
 '
 ' Postconditions:
 ' 1. Creates a sketch.
 ' 2. Sketches a spline.
 ' 3. Examine the graphics area.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim nPtData(35) As Double
     Dim vPtData As Variant
     Dim swSketchSeg As SldWorks.SketchSegment
     Dim bRet  As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
    nPtData(0) = 3      'Dimension
     nPtData(1) = 4      'Order
     nPtData(2) = 7      'Number of control points
     nPtData(3) = 0      'Periodicity
    ' Knots
     nPtData(4) = 0
     nPtData(5) = 0
     nPtData(6) = 0
     nPtData(7) = 0
     nPtData(8) = 0.295784969875007
     nPtData(9) = 0.295784969875007
     nPtData(10) = 0.588801176674805
     nPtData(11) = 1
     nPtData(12) = 1
     nPtData(13) = 1
     nPtData(14) = 1
    ' Control points
     nPtData(15) = -101.019623655914 / 1000#:    nPtData(16) = -9.38844086021505 / 1000#:    nPtData(17) = 0#
     nPtData(18) = -119.993564790426 / 1000#:    nPtData(19) = 13.6067814289365 / 1000#:     nPtData(20) = 0#
     nPtData(21) = -138.967505924938 / 1000#:    nPtData(22) = 36.602003718088 / 1000#:      nPtData(23) = 0#
     nPtData(24) = 15.8143947928824 / 1000#:     nPtData(25) = 19.0600549700683 / 1000#:     nPtData(26) = 0#
     nPtData(27) = -59.4979409454141 / 1000#:    nPtData(28) = -24.6206927754025 / 1000#:    nPtData(29) = 0#
     nPtData(30) = 12.2077094083999 / 1000#:     nPtData(31) = -18.3231635953553 / 1000#:    nPtData(32) = 0#
     nPtData(33) = 54.0774193548387 / 1000#:     nPtData(34) = -14.6459677419355 / 1000#:    nPtData(35) = 0#
    vPtData = nPtData
    swModel.InsertSketch2 True
     bRet = swModel.SketchSplineByEqnParams2((vPtData))
     swModel.InsertSketch2 True
 End Sub
```

---
title: "Create Broken-Out Section Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_BreakOut_Section_Example_VB.htm"
---

# Create Broken-Out Section Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim pointArray As Variant
 Dim points() As Double
 Dim skSegment As SldWorks.SketchSegment
 Dim selectData As SldWorks.selectData
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    ReDim points(0 To 11) As Double
     points(0) = -5.44316967839374E-02
     points(1) = 4.13619530906299E-02
     points(2) = 0
     points(3) = 5.30556603589196E-02
     points(4) = 4.13619530906299E-02
     points(5) = 0
     points(6) = 7.83232107320536E-03
     points(7) = 7.20299635749822E-03
     points(8) = 0
     points(9) = -5.44316967839374E-02
     points(10) = 4.13619530906299E-02
     points(11) = 0

    pointArray = points

    Set skSegment = Part.SketchManager.CreateSpline((pointArray))
     skSegment.Select4 True, selectData

    Part.CreateBreakOutSection 0.00254

    Part.ClearSelection2 True

End Sub
```

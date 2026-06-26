---
title: "Create 2D Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_2D_Spline_Example_VB.htm"
---

# Create 2D Spline Example (VBA)

This topic shows how to create a 2D spline.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Open a new part.
 '
 ' Postconditions:
 ' 1. Creates a sketch of a 2D spline.
 ' 2. Examine the graphics area.
 '---------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
 Dim swModelDoc As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim i As Long
 Dim j As Long
 Dim x(5) As Double
 Dim y(5) As Double
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModelDoc = swApp.ActiveDoc
     Set swModelDocExt = swModelDoc.Extension
     boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)

    ' Open sketch
     swModelDoc.InsertSketch2 True

    ' Calculate the values for x, y, and z
     For i = 0 To 4

        x(i) = i
         y(i) = i ^ 2 + 3 * i
     Next i

    ' Initialize the routine and sketch the first point of the spline at 0,0,0
     swModelDoc.SketchSpline -1, 0, 0, 0

    ' Sketch four more points of the spline
     For j = 4 To 0 Step -1
         swModelDoc.SketchSpline j, x(j), y(j), 0
     Next j

    ' Exit sketch
     swModelDoc.InsertSketch2 True
End Sub
```

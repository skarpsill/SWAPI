---
title: "Create Polygon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Polygon_Example_VB.htm"
---

# Create Polygon Example (VBA)

This example shows how to create a polygon.

```
'-------------------------------------------------------------------
' Preconditions: Open a part document.
'
' Postconditions:
' 1. Inserts a sketch.
' 2. Creates a six-sided polygon, circumscribed with a
'    construction circle.
' 3. Examine the graphics area.
'-------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSketchMgr As SldWorks.SketchManager
 Dim polygon() As SldWorks.SketchSegment
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSketchMgr = swModel.SketchManager

    swSketchMgr.InsertSketch False
    polygon = swSketchMgr.CreatePolygon(-2.5, 0.88, 0#, -2.21, -2.13, 0#, 6, False)

    swModel.ViewZoomtofit2
    ' Set the selection mode to default
     swModel.SetPickMode
    swSketchMgr.InsertSketch True
End Sub
```

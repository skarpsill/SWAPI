---
title: "Get and Set Spline Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Spline_Properties_Example_VB.htm"
---

# Get and Set Spline Properties Example (VBA)

This example shows how to get and set various spline properties.

```
'------------------------------------------------------
' Preconditions: Open a new part, create a
' 2D spline, and select the spline in the
' graphics area.
'
' Postconditions:
' 1. Gets and sets properties of the selected spline.
' 2. Examine the graphics area.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSpline As SldWorks.SketchSpline
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Spline1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSpline = swSelMgr.GetSelectedObject6(1, 0)
```

```
    If (swSpline.ShowSplineHandles) Then
        swSpline.ShowSplineHandles = False
    Else
        swSpline.ShowSplineHandles = True
    End If
```

```
    swModel.WindowRedraw  'Required after using swSpine.ShowSplineHandles
```

```
    If (swSpline.DisplayControlPolygon) Then
        swSpline.DisplayControlPolygon = False
    Else
        swSpline.DisplayControlPolygon = True
    End If
```

```
    If (swSpline.ShowInflectionPoints) Then
        swSpline.ShowInflectionPoints = False
    Else
        swSpline.ShowInflectionPoints = True
    End If
```

```
    If (swSpline.ShowMinimumRadius) Then
        swSpline.ShowMinimumRadius = False
    Else
        swSpline.ShowMinimumRadius = True
    End If
```

```
    If (swSpline.ShowCurvatureCombs) Then
        swSpline.ShowCurvatureCombs = False
    Else
        swSpline.ShowCurvatureCombs = True
    End If
```

```
    If (swSpline.Proportional) Then
        swSpline.Proportional = False
    Else
        swSpline.Proportional = True
    End If
```

```
    swModel.WindowRedraw
```

```
End Sub
```

---
title: "Set Spline Tangency and Curvature Controls Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm"
---

# Set Spline Tangency and Curvature Controls Example (VBA)

This example show how to set a spline's tangency and curvature controls.

```
'-------------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch of a spline.
' 2. Select the spline in the graphics area.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sets the tangency and curvature control
'    for the specified points.
' 2. Examine the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSpline As SldWorks.SketchSpline
Dim swSplineH1 As SldWorks.SplineHandle
Dim swSplineH2 As SldWorks.SplineHandle
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
    ' Set tangency control; substitute coordinates of a point in your spline
    Set swSplineH1 = swSpline.AddTangencyControl(-48.92 / 1000, -5.07 / 1000, 0)
    Debug.Print "Spline point number: " & swSplineH1.SplinePointNumber()
```

```
    ' Add curvature control; substitute coordinates of a point in your spline
    Set swSplineH2 = swSpline.AddCurvatureControl(6.3 / 1000, 15.075 / 1000, 0)
    Debug.Print "Spline point number: " & swSplineH2.SplinePointNumber()

    ' Reset all handles
    swSpline.ResetAllHandles
    ' Relax spline
    swSpline.RelaxSpline
```

```
    swModel.WindowRedraw
```

```
End Sub
```

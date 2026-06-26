---
title: "Simplify Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Simplify_Spline_Example_VB.htm"
---

# Simplify Spline Example (VBA)

This example shows how to simplify a spline.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch of a spline.
' 2. Select the spline in the graphics area.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Simplifies the spline.
' 2. Examine the Immediate window and graphics area.
'------------------------------------------------
Option Explicit
```

```
Sub DumpSketchSplineInfo(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSkSpline As SldWorks.SketchSpline)
```

```
    Dim vSplinePt As Variant
    Dim swSkPt As SldWorks.SketchPoint
    Dim i As Long
```

```
    ' Spline passes through these points
    vSplinePt = swSkSpline.GetPoints2
    For i = 0 To UBound(vSplinePt)
        Set swSkPt = vSplinePt(i)
        Debug.Print "  SketchSplinePt[" & i & "] = (" & swSkPt.X * 1000# & ", " & swSkPt.Y * 1000# & ", " & swSkPt.Z * 1000# & ") mm"
    Next i
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSkSeg As SldWorks.SketchSegment
    Dim swSkSpline As SldWorks.SketchSpline
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSkSeg = swSelMgr.GetSelectedObject5(1)
    Set swSkSpline = swSkSeg
```

```
    Debug.Print "Before:"
    DumpSketchSplineInfo swApp, swModel, swSkSpline
    Debug.Print ""
    ' Tolerance value is in meters
    swModel.SimplifySpline 0.1
    Debug.Print "After:"
    DumpSketchSplineInfo swApp, swModel, swSkSpline
    Debug.Print ""
```

```
End Sub
```

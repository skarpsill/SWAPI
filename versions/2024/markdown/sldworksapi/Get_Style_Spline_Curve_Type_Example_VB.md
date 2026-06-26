---
title: "Get Style Spline Curve Type Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Style_Spline_Curve_Type_Example_VB.htm"
---

# Get Style Spline Curve Type Example (VBA)

This example shows how to create a style spline and get its type of curve.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a style spline.
' 3. Selects the style spline.
' 4. Gets whether the selection is a style spline
'    and, if so, gets its curve type.
' 5. Examine the Immediate window.
'---------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchSpline As SldWorks.SketchSpline
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim pointArray As Variant
Dim points() As Double
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
```

```
    ' Create style spline
    ReDim points(0 To 32) As Double
    points(0) = -0.068952134919552
    points(1) = 8.71923799128056E-03
    points(2) = 0
    points(3) = -5.63242730011457E-02
    points(4) = 1.85409083722633E-02
    points(5) = 0
    points(6) = -4.18924308086813E-02
    points(7) = 8.71923799128056E-03
    points(8) = 0
    points(9) = -2.04451097726579E-02
    points(10) = 2.43537336997836E-02
    points(11) = 0
    points(12) = 6.21370983286659E-03
    points(13) = -1.25276407920698E-02
    points(14) = 0
    points(15) = 2.44539548261202E-02
    points(16) = -4.50995068514512E-03
    points(17) = 0
    points(18) = 3.30729716910642E-02
    points(19) = 6.31393095920317E-03
    points(20) = 0
    points(21) = 0.048306582894221
    points(22) = 1.17258717813773E-02
    points(23) = 0
    points(24) = 0.05852913778055
    points(25) = -6.11348870653004E-03
    points(26) = 0
    points(27) = 6.53441743714359E-02
    points(28) = -1.07236605180117E-02
    points(29) = 0
    points(30) = -999999999
    points(31) = -999999999
    points(32) = -999999969
    pointArray = points
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    ' Get whether selection is style spline and, if so, get its curve type
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Spline1@Sketch1", "EXTSKETCHSEGMENT", -3.11890911939585E-02, 1.22942518144824E-02, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swSketchSpline = swSelectionMgr.GetSelectedObject6(1, -1)
    status = swSketchSpline.IsStyleSpline
    Debug.Print "Is the selection a style spline? " & status
    If status Then
        Debug.Print "Style spline curve type (3 = swStyleSplineCurveType_e.BSpline_Degree7): " & swSketchSpline.CurveType
    End If
```

```
End Sub
```

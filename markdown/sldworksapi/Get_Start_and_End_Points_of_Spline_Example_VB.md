---
title: "Get Start and End Points of Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Start_and_End_Points_of_Spline_Example_VB.htm"
---

# Get Start and End Points of Spline Example (VBA)

This example shows how to get the start and end points of a spline.

```
'-------------------------------------------------
' Preconditions:
' 1. Open a sketch that has a spline.
' 2. Select the spline.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the start and end points of the spline.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Long2Rec
    iLower As Long
    iUpper As Long
End Type
```

```
' Extract two integer values from a single double value
' by assigning a DoubleRec to the double value,
' copying the value to a Long2Rec, and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Long, iUpper As Long)
    Dim dr As DoubleRec
    Dim i2r As Long2Rec
    ' Set the double value
    dr.dValue = dValue
    ' Copy the values
    LSet i2r = dr
    ' Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim swCurve As SldWorks.Curve
    Dim nStartParam As Double
    Dim nEndParam As Double
    Dim bIsClosed As Boolean
    Dim bIsPeriodic As Boolean
    Dim vStart As Variant
    Dim vEnd As Variant
    Dim nDummy As Long
    Dim nStartSuccess As Long
    Dim nEndSuccess As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSketchSeg = swSelMgr.GetSelectedObject5(1)
    Set swCurve = swSketchSeg.GetCurve
    bRet = swCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
    vStart = swCurve.Evaluate(nStartParam)
    vEnd = swCurve.Evaluate(nEndParam)
    ExtractFields vStart(6), nStartSuccess, nDummy
    ExtractFields vEnd(6), nEndSuccess, nDummy
```

```
    Debug.Print "Length = " & swCurve.GetLength2(nStartParam, nEndParam) * 1000# & " mm"
    Debug.Print "  Start Pt     = (" & vStart(0) * 1000# & ", " & vStart(1) * 1000# & ", " & vStart(2) * 1000# & ") mm"
    Debug.Print "    tangent    = (" & vStart(3) & ", " & vStart(4) & ", " & vStart(5) & ")"
    Debug.Print "  End   Pt     = (" & vEnd(0) * 1000# & ", " & vEnd(1) * 1000# & ", " & vEnd(2) * 1000# & ") mm"
    Debug.Print "    tangent    = (" & vEnd(3) & ", " & vEnd(4) & ", " & vEnd(5) & ")"
```

```
End Sub
```

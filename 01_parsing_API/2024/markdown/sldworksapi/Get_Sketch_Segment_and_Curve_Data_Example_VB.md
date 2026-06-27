---
title: "Get Sketch Segment and Curve Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_and_Curve_Data_Example_VB.htm"
---

# Get Sketch Segment and Curve Data Example (VBA)

This example shows how to get data about a sketch segment and curve.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Edit a sketch and select a sketch segment.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets sketch segment and curve data.
' 2. Examine the Immediate window.
'---------------------------------------------
```

```
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
' Extract two integer values from of a single double value
' by assigning a DoubleRec to the double value and
' copying the value to a Long2Rec and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Long, iUpper As Long)
    Dim dr As DoubleRec
    Dim i2r As Long2Rec
```

```
    ' Set the double value
    dr.dValue = dValue
```

```
    ' Copy the values
    LSet i2r = dr
```

```
    ' Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
End Function
```

```
Sub ProcessCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swCurve As SldWorks.Curve)
    Dim nStartParam As Double
    Dim nEndParam As Double
    Dim bIsClosed As Boolean
    Dim bIsPeriodic As Boolean
    Dim vStartEval As Variant
    Dim vEndEval As Variant
    Dim nSuccessStart As Long
    Dim nEndStart As Long
    Dim nDummy As Long
    Dim bRet As Boolean
```

```
    bRet = swCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic): Debug.Assert bRet
    vStartEval = swCurve.Evaluate(nStartParam)
    vEndEval = swCurve.Evaluate(nEndParam)
```

```
    ExtractFields vStartEval(6), nSuccessStart, nDummy
    ExtractFields vEndEval(6), nEndStart, nDummy
```

```
    Debug.Print "    IsClosed       = " & bIsClosed
    Debug.Print "    IsPeriodic     = " & bIsPeriodic
    Debug.Print "    IsTrimmed      = " & swCurve.IsTrimmedCurve
    Debug.Print "    Start"
    Debug.Print "      Point        = (" & vStartEval(0) * 1000# & ", " & vStartEval(1) * 1000# & ", " & vStartEval(2) * 1000# & ") mm"
    Debug.Print "      Tangent      = (" & vStartEval(3) & ", " & vStartEval(4) & ", " & vStartEval(5) & ")"
    Debug.Print "      Success      = " & nSuccessStart
    Debug.Print "    Finish"
    Debug.Print "      Point        = (" & vEndEval(0) * 1000# & ", " & vEndEval(1) * 1000# & ", " & vEndEval(2) * 1000# & ") mm"
    Debug.Print "      Tangent      = (" & vEndEval(3) & ", " & vEndEval(4) & ", " & vEndEval(5) & ")"
    Debug.Print "      Success      = " & nEndStart
End Sub
```

```
Sub main()
```

```
    Dim sSkSegmentsName(5) As String
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSkSeg As SldWorks.SketchSegment
    Dim swCurve As SldWorks.Curve
    Dim swSkFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim vID As Variant
    Dim bRet As Boolean
```

```
    sSkSegmentsName(swSketchLINE) = "swSketchLINE"
    sSkSegmentsName(swSketchARC) = "swSketchARC"
    sSkSegmentsName(swSketchELLIPSE) = "swSketchELLIPSE"
    sSkSegmentsName(swSketchSPLINE) = "swSketchSPLINE"
    sSkSegmentsName(swSketchTEXT) = "swSketchTEXT"
    sSkSegmentsName(swSketchPARABOLA) = "swSketchPARABOLA"
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSkSeg = swSelMgr.GetSelectedObject6(1, -1)
    Set swCurve = swSkSeg.GetCurve
    Set swSkFeat = swSkSeg.GetSketch
    Set swSketch = swSkFeat.GetSpecificFeature2
```

```
    vID = swSkSeg.GetID
    Debug.Print "Feature = " & swSkFeat.Name & " [" & swSketch.Is3D & "]"
    Debug.Print "  Sketch segment data"
    Debug.Print "    ID = [" & vID(0) & "," & vID(1) & "]"
    Debug.Print "      Type                 = " & sSkSegmentsName(swSkSeg.GetType)
    Debug.Print "      ConstGeom            = " & swSkSeg.ConstructionGeometry
```

```
    Debug.Print "  Curve data"
    ProcessCurve swApp, swModel, swCurve
```

```
End Sub
```

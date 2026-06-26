---
title: "Get Spline Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Spline_Parameters_Example_VB.htm"
---

# Get Spline Parameters Example (VBA)

This example shows how to get the parameters of a spline.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch of a spline.
' 2. Select the sketch of the spline.
'
' Postconditions:
' 1. Gets the parameters of the spline.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Public Enum swSketchSegments_e
    swSketchLINE = 0
    swSketchARC = 1
    swSketchELLIPSE = 2
    swSketchSPLINE = 3
    swSketchTEXT = 4
    swSketchPARABOLA = 5
End Enum
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Int2Rec
    'Assume C int has 4 bytes
    iLower As Long
    iUpper As Long
End Type
```

```
'Extract two integer values from a single double value
'by assigning a DoubleRec to the double value and then
'copying the value to Int2Rec and
'extracting the integer values
Function ExtractFields(dValue As Double, iLower As Long, iUpper As Long)
```

```
    Dim dr                  As DoubleRec
    Dim i2r                 As Int2Rec
```

```
    'Set the double value
    dr.dValue = dValue
```

```
    'Copy the values
    LSet i2r = dr
```

```
    'Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
```

```
End Function
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFeat                  As SldWorks.Feature
    Dim swSketch                As SldWorks.Sketch
    Dim vSkSeg                  As Variant
    Dim swSkSeg                 As SldWorks.SketchSegment
    Dim swSkSpline              As SldWorks.SketchSpline
    Dim vSplineParam            As Variant
    Dim vSplinePt               As Variant
    Dim swSkPt                  As SldWorks.SketchPoint
    Dim nSplineParam0           As Double
    Dim nSplineParam1           As Double
    Dim nDim                    As Long
    Dim nOrder                  As Long
    Dim nCtrlPoints             As Long
    Dim nPeriodic               As Long
    Dim nNumKnots               As Long
    Dim nStyleLayerParam0       As Double
    Dim nStyleLayerParam1       As Double
    Dim nStyleLayerParam2       As Double
    Dim nColor                  As Long
    Dim nLineStyle              As Long
    Dim nLineWidth              As Long
    Dim nLayer                  As Long
    Dim nLayerOverride          As Long
    Dim nDummy                  As Long
    Dim nIndex                  As Long
    Dim nOffset                 As Long
    Dim i                       As Long
    Dim j                       As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    Debug.Print swFeat.Name
```

```
    vSplineParam = swSketch.GetSplineParams2
    nIndex = 0
```

```
    Do While nIndex < UBound(vSplineParam)
        nOffset = nIndex
```

```
        ' Get spline data from first two packed elements
        nSplineParam0 = vSplineParam(nOffset + 0): nIndex = nIndex + 1
        nSplineParam1 = vSplineParam(nOffset + 1): nIndex = nIndex + 1
        ExtractFields nSplineParam0, nDim, nOrder
        ExtractFields nSplineParam1, nCtrlPoints, nPeriodic
```

```
        If 1 = nPeriodic Then
            nNumKnots = nCtrlPoints + 1
        Else
            nNumKnots = nCtrlPoints + nOrder
        End If
```

```
        Debug.Print "  Dim          = " & nDim
        Debug.Print "  Order        = " & nOrder
        Debug.Print "  CtrlPoints   = " & nCtrlPoints
        Debug.Print "  Periodic     = " & nPeriodic
        Debug.Print "  NumKnots     = " & nNumKnots
        Debug.Print ""
```

```
        ' Get control point data
        ' Dimension is always 3 or 4
        Debug.Assert 3 = nDim Or 4 = nDim
        For i = 2 + nOffset To 2 + nOffset + nCtrlPoints * nDim - 3 Step nDim
            Debug.Print "  CtrlPt[" & i & "] = (" & vSplineParam(i + 0) * 1000# & ", " & vSplineParam(i + 1) * 1000# & ", " & vSplineParam(i + 2) * 1000# & ") mm"
            If 4 = nDim Then
                Debug.Print "    Weight[" & i & "] = " & vSplineParam(i + 3)
            End If
            nIndex = nIndex + nDim
        Next i
        Debug.Print ""
        For i = 2 + nOffset + nCtrlPoints * nDim To 2 + nOffset + nCtrlPoints * nDim + nNumKnots - 1
            ' Knot weights must be non-descending
            Debug.Print "  Knot[" & i & "] = " & vSplineParam(i)
            nIndex = nIndex + 1
        Next i
        Debug.Print ""
```

```
        ' Get style from packed elements - only supported for drawings
        nStyleLayerParam0 = vSplineParam(2 + nOffset + nNumKnots + nCtrlPoints * nDim + 0): nIndex = nIndex + 0
        nStyleLayerParam1 = vSplineParam(2 + nOffset + nNumKnots + nCtrlPoints * nDim + 1): nIndex = nIndex + 1
        nStyleLayerParam2 = vSplineParam(2 + nOffset + nNumKnots + nCtrlPoints * nDim + 2): nIndex = nIndex + 1
        ExtractFields nStyleLayerParam0, nColor, nLineStyle
        ExtractFields nStyleLayerParam1, nLineWidth, nLayer
        ExtractFields nStyleLayerParam2, nLayerOverride, nDummy
```

```
        Debug.Print "  Color            = " & nColor
        Debug.Print "  LineStyle        = " & nLineStyle
        Debug.Print "  LineWidth        = " & nLineWidth
        Debug.Print "  Layer            = " & nLayer
        Debug.Print "  LayerOverride    = " & nLayerOverride
        Debug.Print "  "
        nIndex = nIndex + 1
    Loop
```

```
    vSkSeg = swSketch.GetSketchSegments
    For i = 0 To UBound(vSkSeg)
        Set swSkSeg = vSkSeg(i)
```

```
        If swSketchSPLINE = swSkSeg.GetType Then
            Set swSkSpline = swSkSeg
```

```
            ' Spline passes through these points
            ' first, and the last spline points are the same
            ' as the first and last control points
            vSplinePt = swSkSpline.GetPoints2
            For j = 0 To UBound(vSplinePt)
                Set swSkPt = vSplinePt(j)
                Debug.Print "  SketchSplinePt[" & j & "] = (" & swSkPt.X * 1000# & ", " & swSkPt.Y * 1000# & ", " & swSkPt.Z * 1000# & ") mm"
            Next j
        End If
        Debug.Print ""
    Next i
```

```
End Sub
```

---
title: "Get Length of Spline or Elliptical Edge Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm"
---

# Get Length of Spline or Elliptical Edge Example (VBA)

This example shows how to get the length of an edge using display tessellation.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a spline or elliptical edge.
' 2. Select the spline or elliptical edge.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates two 3D sketches:
'    * Control Pts contains control points for the edge.
'    * Spline Pts contains spline points for the edge.
' 2. Examine the graphics area, FeatureManager design tree,
'    the Immediate window.
'
' NOTE: A sketch with spline points is only created for a spline edge.
'-------------------------------------------------------------------
```

```
Option Explicit
```

```
'  Tolerances that the user can set using IModeler::SetTolerances
```

```
Public Enum swTolerances_e
    swBSCurveOutputTol = 0  ' 3D bspline curve output tolerance (meters)
    swBSCurveNonRationalOutputTol = 1  ' 3D non-rational bspline curve output tolerance (meters)
    swUVCurveOutputTol = 2  ' 2D trim curve output tolerance (fraction of characteristic min. face dimension)
    swSurfChordTessellationTol = 3  ' Chord tolerance or deviation for tessellation for surfaces
    swSurfAngularTessellationTol = 4  ' Angular tolerance or deviation for tessellation for surfaces
    swCurveChordTessellationTol = 5  ' Chord tolerance or deviation for tessellation for curves
End Enum
```

```
Public Enum swCurveTypes_e
    LINE_TYPE = 3001
    CIRCLE_TYPE = 3002
    ELLIPSE_TYPE = 3003
    INTERSECTION_TYPE = 3004
    BCURVE_TYPE = 3005
    SPCURVE_TYPE = 3006
    CONSTPARAM_TYPE = 3008
    TRIMMED_TYPE = 3009
End Enum
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Long2Rec
    iLower As Long ' Assuming that a C int has 4 bytes
    iUpper As Long
End Type
```

```
' Extract two integer values out of a single double value,
' by assigning a DoubleRec to the double value and then
' copying the value over an Long2Rec and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Integer, iUpper As Integer)
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
```

```
End Function
```

```
Sub ProcessModellerSettings(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swModeller As SldWorks.Modeler)
```

```
    ' Process modeler settings
    Debug.Print "Modeler Settings:"
    Debug.Print "  BSCurveOutputTol                 = " & swModeller.GetToleranceValue(swBSCurveOutputTol)
    Debug.Print "  BSCurveNonRationalOutputTol      = " & swModeller.GetToleranceValue(swBSCurveNonRationalOutputTol)
    Debug.Print "  UVCurveOutputTol                 = " & swModeller.GetToleranceValue(swUVCurveOutputTol)
    Debug.Print "  SurfChordTessellationTol         = " & swModeller.GetToleranceValue(swSurfChordTessellationTol)
    Debug.Print "  SurfAngularTessellationTol       = " & swModeller.GetToleranceValue(swSurfAngularTessellationTol)
    Debug.Print "  CurveChordTessellationTol        = " & swModeller.GetToleranceValue(swCurveChordTessellationTol)
    Debug.Print ""
```

```
End Sub
```

```
Sub ProcessBCurveInfo(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vBCurveParam As Variant)
```

```
    Dim nDim As Integer
    Dim nOrder As Integer
    Dim nCtrlPoints As Integer
    Dim nPeriodicity As Integer
    Dim nNumKnots As Integer
    Dim swSketch As SldWorks.Sketch
    Dim swSkFeat As SldWorks.Feature
    Dim swSkPt As SldWorks.SketchPoint
    Dim i As Integer
```

```
    ExtractFields vBCurveParam(0), nDim, nOrder
    ExtractFields vBCurveParam(1), nCtrlPoints, nPeriodicity
    nNumKnots = nOrder + nCtrlPoints
```

```
    Debug.Print "  Dimension        = " & nDim
    Debug.Print "  Order            = " & nOrder
    Debug.Print "  Num Ctrl Pts     = " & nCtrlPoints
    Debug.Print "  Periodicity      = " & nPeriodicity
    Debug.Print "  Num Knots        = " & nNumKnots
    Debug.Print ""
```

```
    For i = 0 To nNumKnots - 1
        ' Knot weights should be increasing monotonically
        Debug.Print "  Knot(" & i & ")          = " & vBCurveParam(2 + i)
    Next i
```

```
    Debug.Print ""
```

```
    swModel.Insert3DSketch2 False
    swModel.SetAddToDB True
    swModel.SetDisplayWhenAdded False
```

```
    Set swSketch = swModel.GetActiveSketch2
    Set swSkFeat = swSketch
```

```
    If 3 = nDim Then
```

```
        For i = 2 + nNumKnots To UBound(vBCurveParam) - 1 Step 3
```

```
            Debug.Print "  Ctrl(" & (i - 2 - nNumKnots) / 3 & ")          = (" & vBCurveParam(i + 0) * 1000# & ", " & vBCurveParam(i + 1) * 1000# & ", " & vBCurveParam(i + 2) * 1000# & ") mm"
            Set swSkPt = swModel.CreatePoint2(vBCurveParam(i + 0), vBCurveParam(i + 1), vBCurveParam(i + 2))
        Next i
    Else
        For i = 2 + nNumKnots To UBound(vBCurveParam) - 1 Step 4
            Debug.Print "  Ctrl(" & (i - 2 - nNumKnots) / 4 & ")          = (" & vBCurveParam(i + 0) * 1000# & ", " & vBCurveParam(i + 1) * 1000# & ", " & vBCurveParam(i + 2) * 1000# & ") mm [" & vBCurveParam(i + 3) & "]"
            Set swSkPt = swModel.CreatePoint2(vBCurveParam(i + 0), vBCurveParam(i + 1), vBCurveParam(i + 2))
       Next i
    End If
```

```
    swModel.SetDisplayWhenAdded True
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
```

```
    swModel.ClearSelection2 True
```

```
    swSkFeat.Name = "Control Pts"
```

```
End Sub
```

```
Sub ProcessSplineInfo(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vSplinePts As Variant)
    Dim swSketch As SldWorks.Sketch
    Dim swSkFeat As SldWorks.Feature
    Dim swSkPt As SldWorks.SketchPoint
    Dim i As Long
```

```
    swModel.Insert3DSketch2 False
    swModel.SetAddToDB True
    swModel.SetDisplayWhenAdded False
```

```
    Set swSketch = swModel.GetActiveSketch2
    Set swSkFeat = swSketch
```

```
    For i = 0 To UBound(vSplinePts) Step 3
        Debug.Print "  SplinePt(" & i / 3 & ")     = (" & vSplinePts(i + 0) * 1000# & ", " & vSplinePts(i + 1) * 1000# & ", " & vSplinePts(i + 2) * 1000# & ") mm"
        Set swSkPt = swModel.CreatePoint2(vSplinePts(i + 0), vSplinePts(i + 1), vSplinePts(i + 2))
    Next i
```

```
    swModel.SetDisplayWhenAdded True
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
```

```
    swModel.ClearSelection2 True
```

```
    swSkFeat.Name = "Spline Pts"
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModeller As SldWorks.Modeler
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim vBCurveParam As Variant
    Dim vSplinePts As Variant
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModeller = swApp.GetModeler
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEdge = swSelMgr.GetSelectedObject5(1)
    Set swCurve = swEdge.GetCurve: Debug.Assert swCurve.IsBcurve
    ProcessModellerSettings swApp, swModel, swModeller
    vBCurveParam = swCurve.GetBCurveParams(False)
    vSplinePts = swCurve.GetSplinePts(vBCurveParam)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Identity         = " & swCurve.Identity
```

```
    ProcessBCurveInfo swApp, swModel, vBCurveParam
```

```
    Debug.Print "  "
```

```
    ' Do not assert because null is a valid return value
    '   ICurve::GetSplinePts
    '       *  If the curve is periodic, then it must not have any repeated knots.
    '       *  If the curve is non-periodic, it must only have repeated
    '          knots at its ends.
    '
    '       The curve must be cubic or lower degree, non-rational, and
    '           have continuous first and second derivatives.
    '
    '       NOTE: For a linear or quadratic curve to satisfy these continuity
    '       requirements, it must consist of a single segment.
```

```
    If Not IsNull(vSplinePts) Then
        ProcessSplineInfo swApp, swModel, vSplinePts
        Debug.Print " "
```

```
    End If
```

```
End Sub
```

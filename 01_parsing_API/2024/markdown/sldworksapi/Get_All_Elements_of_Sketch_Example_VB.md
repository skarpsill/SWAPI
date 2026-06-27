---
title: "Get All Elements of Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Elements_of_Sketch_Example_VB.htm"
---

# Get All Elements of Sketch Example (VBA)

This example shows how to get all of the elements of a sketch.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part and select a sketch.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets all elements of the sketch.
' 2. Examine the Immediate window.
'---------------------------------------------
Option Explicit
```

```
Public Enum swSkSegments_e
    swSketchLINE = 0
    swSketchARC = 1
    swSketchELLIPSE = 2
    swSketchSPLINE = 3
    swSketchTEXT = 4
    swSketchPARABOLA = 5
End Enum
```

```
Sub ProcessTextFormat(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTextFormat As SldWorks.TextFormat)
```

```
    Debug.Print "        BackWards                    = " & swTextFormat.BackWards
    Debug.Print "        Bold                         = " & swTextFormat.Bold
    Debug.Print "        CharHeight                   = " & swTextFormat.CharHeight
    Debug.Print "        CharHeightInPts              = " & swTextFormat.CharHeightInPts
    Debug.Print "        CharSpacingFactor            = " & swTextFormat.CharSpacingFactor
    Debug.Print "        Escapement                   = " & swTextFormat.Escapement
    Debug.Print "        IsHeightSpecifiedInPts       = " & swTextFormat.IsHeightSpecifiedInPts
    Debug.Print "        Italic                       = " & swTextFormat.Italic
    Debug.Print "        LineLength                   = " & swTextFormat.LineLength
    Debug.Print "        LineSpacing                  = " & swTextFormat.LineSpacing
    Debug.Print "        ObliqueAngle                 = " & swTextFormat.ObliqueAngle
    Debug.Print "        Strikeout                    = " & swTextFormat.Strikeout
    Debug.Print "        TypeFaceName                 = " & swTextFormat.TypeFaceName
    Debug.Print "        Underline                    = " & swTextFormat.Underline
    Debug.Print "        UpsideDown                   = " & swTextFormat.UpsideDown
    Debug.Print "        Vertical                     = " & swTextFormat.Vertical
    Debug.Print "        WidthFactor                  = " & swTextFormat.WidthFactor
    Debug.Print ""
End Sub
```

```
Function TransformSketchPointToModelSpace(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkPt As SldWorks.SketchPoint) As SldWorks.MathPoint
```

```
    Dim swMathUtil As SldWorks.MathUtility
    Dim swXform As SldWorks.MathTransform
    Dim nPt(2) As Double
    Dim vPt  As Variant
    Dim swMathPt As SldWorks.MathPoint
```

```
    nPt(0) = swSkPt.X:      nPt(1) = swSkPt.Y:      nPt(2) = swSkPt.Z
    vPt = nPt
```

```
    Set swMathUtil = swApp.GetMathUtility
    Set swXform = swSketch.ModelToSketchTransform
    Set swXform = swXform.Inverse
    Set swMathPt = swMathUtil.CreatePoint((vPt))
    Set swMathPt = swMathPt.MultiplyTransform(swXform)
    Set TransformSketchPointToModelSpace = swMathPt
```

```
End Function
```

```
Sub ProcessSketchLine(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkLine As SldWorks.SketchLine)
```

```
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
    Dim swStartModPt As SldWorks.MathPoint
    Dim swEndModPt As SldWorks.MathPoint

    Set swStartPt = swSkLine.GetStartPoint2
    Set swEndPt = swSkLine.GetEndPoint2
```

```
    Set swStartModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swStartPt)
    Set swEndModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swEndPt)
    Debug.Print "      Start (sketch)   = (" & swStartPt.X * 1000# & ", " & swStartPt.Y * 1000# & ", " & swStartPt.Z * 1000# & ") mm"
    Debug.Print "      Start (model )   = (" & swStartModPt.ArrayData(0) * 1000# & ", " & swStartModPt.ArrayData(1) * 1000# & ", " & swStartModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      End   (sketch)   = (" & swEndPt.X * 1000# & ", " & swEndPt.Y * 1000# & ", " & swEndPt.Z * 1000# & ") mm"
    Debug.Print "      End   (model )   = (" & swEndModPt.ArrayData(0) * 1000# & ", " & swEndModPt.ArrayData(1) * 1000# & ", " & swEndModPt.ArrayData(2) * 1000# & ") mm"
End Sub
```

```
Sub ProcessSketchArc(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkArc As SldWorks.SketchArc)
```

```
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
    Dim swCtrPt As SldWorks.SketchPoint
    Dim vNormal As Variant
    Dim swStartModPt As SldWorks.MathPoint
    Dim swEndModPt As SldWorks.MathPoint
    Dim swCtrModPt As SldWorks.MathPoint

    Set swStartPt = swSkArc.GetStartPoint2
    Set swEndPt = swSkArc.GetEndPoint2
    Set swCtrPt = swSkArc.GetCenterPoint2
    Set swStartModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swStartPt)
    Set swEndModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swEndPt)
    Set swCtrModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swCtrPt)
```

```
    vNormal = swSkArc.GetNormalVector
    Debug.Print "      Start (sketch)   = (" & swStartPt.X * 1000# & ", " & swStartPt.Y * 1000# & ", " & swStartPt.Z * 1000# & ") mm"
    Debug.Print "      Start (model )   = (" & swStartModPt.ArrayData(0) * 1000# & ", " & swStartModPt.ArrayData(1) * 1000# & ", " & swStartModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      End   (sketch)   = (" & swEndPt.X * 1000# & ", " & swEndPt.Y * 1000# & ", " & swEndPt.Z * 1000# & ") mm"
    Debug.Print "      End   (model )   = (" & swEndModPt.ArrayData(0) * 1000# & ", " & swEndModPt.ArrayData(1) * 1000# & ", " & swEndModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Center(sketch)   = (" & swCtrPt.X * 1000# & ", " & swCtrPt.Y * 1000# & ", " & swCtrPt.Z * 1000# & ") mm"
    Debug.Print "      Center(model )   = (" & swCtrModPt.ArrayData(0) * 1000# & ", " & swCtrModPt.ArrayData(1) * 1000# & ", " & swCtrModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Radius           = " & swSkArc.GetRadius * 1000# & " mm"
    Debug.Print "      IsCircle         = " & CBool(swSkArc.IsCircle)
    Debug.Print "      Rot dirn         = " & swSkArc.GetRotationDir
```

```
End Sub
```

```
Sub ProcessSketchEllipse(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkEllipse As SldWorks.SketchEllipse)
```

```
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
    Dim swCtrPt As SldWorks.SketchPoint
    Dim swMajPt As SldWorks.SketchPoint
    Dim swMinPt As SldWorks.SketchPoint
    Dim swStartModPt As SldWorks.MathPoint
    Dim swEndModPt As SldWorks.MathPoint
    Dim swCtrModPt As SldWorks.MathPoint
    Dim swMajModPt As SldWorks.MathPoint
    Dim swMinModPt As SldWorks.MathPoint
```

```
    Set swStartPt = swSkEllipse.GetStartPoint2
    Set swEndPt = swSkEllipse.GetEndPoint2
    Set swCtrPt = swSkEllipse.GetCenterPoint2
    Set swMajPt = swSkEllipse.GetMajorPoint2
    Set swMinPt = swSkEllipse.GetMinorPoint2
    Set swStartModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swStartPt)
    Set swEndModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swEndPt)
    Set swCtrModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swCtrPt)
    Set swMajModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swMajPt)
    Set swMinModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swMinPt)
```

```
    Debug.Print "      Start (sketch)   = (" & swStartPt.X * 1000# & ", " & swStartPt.Y * 1000# & ", " & swStartPt.Z * 1000# & ") mm"
    Debug.Print "      Start (model )   = (" & swStartModPt.ArrayData(0) * 1000# & ", " & swStartModPt.ArrayData(1) * 1000# & ", " & swStartModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      End   (sketch)   = (" & swEndPt.X * 1000# & ", " & swEndPt.Y * 1000# & ", " & swEndPt.Z * 1000# & ") mm"
    Debug.Print "      End   (model )   = (" & swEndModPt.ArrayData(0) * 1000# & ", " & swEndModPt.ArrayData(1) * 1000# & ", " & swEndModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Center(sketch)   = (" & swCtrPt.X * 1000# & ", " & swCtrPt.Y * 1000# & ", " & swCtrPt.Z * 1000# & ") mm"
    Debug.Print "      Center(model )   = (" & swCtrModPt.ArrayData(0) * 1000# & ", " & swCtrModPt.ArrayData(1) * 1000# & ", " & swCtrModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Major (sketch)   = (" & swMajPt.X * 1000# & ", " & swMajPt.Y * 1000# & ", " & swMajPt.Z * 1000# & ") mm"
    Debug.Print "      Major (model )   = (" & swMajModPt.ArrayData(0) * 1000# & ", " & swMajModPt.ArrayData(1) * 1000# & ", " & swMajModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Minor (sketch)   = (" & swMinPt.X * 1000# & ", " & swMinPt.Y * 1000# & ", " & swMinPt.Z * 1000# & ") mm"
    Debug.Print "      Minor (model )   = (" & swMinModPt.ArrayData(0) * 1000# & ", " & swMinModPt.ArrayData(1) * 1000# & ", " & swMinModPt.ArrayData(2) * 1000# & ") mm"
End Sub
```

```
Sub ProcessSketchSpline(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkSpline As SldWorks.SketchSpline)
```

```
    Dim vSplinePtArr As Variant
    Dim vSplinePt As Variant
    Dim swSplinePt As SldWorks.SketchPoint
    Dim swSplineModPt As SldWorks.MathPoint
```

```
    vSplinePtArr = swSkSpline.GetPoints2
    For Each vSplinePt In vSplinePtArr
        Set swSplinePt = vSplinePt
        Set swSplineModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swSplinePt)
```

```
        Debug.Print "      Spline (sketch)  = (" & swSplinePt.X * 1000# & ", " & swSplinePt.Y * 1000# & ", " & swSplinePt.Z * 1000# & ") mm"
        Debug.Print "      Spline (model )  = (" & swSplineModPt.ArrayData(0) * 1000# & ", " & swSplineModPt.ArrayData(1) * 1000# & ", " & swSplineModPt.ArrayData(2) * 1000# & ") mm"
    Next vSplinePt
```

```
End Sub
```

```
Sub ProcessSketchText(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkText As SldWorks.SketchText)
```

```
    Dim vCoordPt As Variant
    Dim swMathUtil  As SldWorks.MathUtility
    Dim swXform As SldWorks.MathTransform
    Dim swCoordModPt As SldWorks.MathPoint
```

```
    vCoordPt = swSkText.GetCoordinates
    Set swMathUtil = swApp.GetMathUtility
    Set swXform = swSketch.ModelToSketchTransform
    Set swXform = swXform.Inverse
    Set swCoordModPt = swMathUtil.CreatePoint((vCoordPt))
    Set swCoordModPt = swCoordModPt.MultiplyTransform(swXform)
    Debug.Print "      Coords (sketch)  = (" & vCoordPt(0) * 1000# & ", " & vCoordPt(1) * 1000# & ", " & vCoordPt(2) * 1000# & ") mm"
    Debug.Print "      Coords (model )  = (" & swCoordModPt.ArrayData(0) * 1000# & ", " & swCoordModPt.ArrayData(1) * 1000# & ", " & swCoordModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Use doc fmt      = " & swSkText.GetUseDocTextFormat
    Debug.Print "      Text             = " & swSkText.Text
```

```
    ProcessTextFormat swApp, swModel, swSkText.GetTextFormat
```

```
End Sub
```

```
Sub ProcessSketchParabola(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSkParabola As SldWorks.SketchParabola)
```

```
    Dim swApexPt As SldWorks.SketchPoint
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
    Dim swFocalPt As SldWorks.SketchPoint
    Dim swApexModPt As SldWorks.MathPoint
    Dim swStartModPt As SldWorks.MathPoint
    Dim swEndModPt As SldWorks.MathPoint
    Dim swFocalModPt As SldWorks.MathPoint
```

```
    Set swApexPt = swSkParabola.GetApexPoint2
    Set swStartPt = swSkParabola.GetStartPoint2
    Set swEndPt = swSkParabola.GetEndPoint2
    Set swFocalPt = swSkParabola.GetFocalPoint2
    Set swApexModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swApexPt)
    Set swStartModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swStartPt)
    Set swEndModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swEndPt)
    Set swFocalModPt = TransformSketchPointToModelSpace(swApp, swModel, swSketch, swFocalPt)
    Debug.Print "      Apex  (sketch)   = (" & swApexPt.X * 1000# & ", " & swApexPt.Y * 1000# & ", " & swApexPt.Z * 1000# & ") mm"
    Debug.Print "      Apex  (model )   = (" & swApexModPt.ArrayData(0) * 1000# & ", " & swApexModPt.ArrayData(1) * 1000# & ", " & swApexModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Start (sketch)   = (" & swStartPt.X * 1000# & ", " & swStartPt.Y * 1000# & ", " & swStartPt.Z * 1000# & ") mm"
    Debug.Print "      Start (model )   = (" & swStartModPt.ArrayData(0) * 1000# & ", " & swStartModPt.ArrayData(1) * 1000# & ", " & swStartModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      End   (sketch)   = (" & swEndPt.X * 1000# & ", " & swEndPt.Y * 1000# & ", " & swEndPt.Z * 1000# & ") mm"
    Debug.Print "      End   (model )   = (" & swEndModPt.ArrayData(0) * 1000# & ", " & swEndModPt.ArrayData(1) * 1000# & ", " & swEndModPt.ArrayData(2) * 1000# & ") mm"
    Debug.Print "      Focal (sketch)   = (" & swFocalPt.X * 1000# & ", " & swFocalPt.Y * 1000# & ", " & swFocalPt.Z * 1000# & ") mm"
    Debug.Print "      Focal (model )   = (" & swFocalModPt.ArrayData(0) * 1000# & ", " & swFocalModPt.ArrayData(1) * 1000# & ", " & swFocalModPt.ArrayData(2) * 1000# & ") mm"
```

```
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
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim vSkSegArr As Variant
    Dim vSkSeg As Variant
    Dim swSkSeg  As SldWorks.SketchSegment
    Dim swSkLine As SldWorks.SketchLine
    Dim swSkArc As SldWorks.SketchArc
    Dim swSkEllipse As SldWorks.SketchEllipse
    Dim swSkSpline As SldWorks.SketchSpline
    Dim swSkText As SldWorks.SketchText
    Dim swSkParabola As SldWorks.SketchParabola
    Dim vID As Variant
    Dim i As Long
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
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature
    Debug.Print "Feature = " & swFeat.Name & " [" & swSketch.Is3D & "]"
    Debug.Print "  Sketch Segments:"
```

```
    vSkSegArr = swSketch.GetSketchSegments
    For Each vSkSeg In vSkSegArr
        Set swSkSeg = vSkSeg
        vID = swSkSeg.GetID
        Debug.Print "    ID = [" & vID(0) & "," & vID(1) & "]"
        Debug.Print "      Type             = " & sSkSegmentsName(swSkSeg.GetType)
        Debug.Print "      ConstGeom        = " & swSkSeg.ConstructionGeometry
        Select Case swSkSeg.GetType
            Case swSketchLINE
                Set swSkLine = swSkSeg
                ProcessSketchLine swApp, swModel, swSketch, swSkLine
            Case swSketchARC
                Set swSkArc = swSkSeg
                ProcessSketchArc swApp, swModel, swSketch, swSkArc
            Case swSketchELLIPSE
                Set swSkEllipse = swSkSeg
                ProcessSketchEllipse swApp, swModel, swSketch, swSkEllipse
            Case swSketchSPLINE
                Set swSkSpline = swSkSeg
                ProcessSketchSpline swApp, swModel, swSketch, swSkSpline
            Case swSketchTEXT
                Set swSkText = swSkSeg
                ProcessSketchText swApp, swModel, swSketch, swSkText
                Case swSketchPARABOLA
                Set swSkParabola = swSkSeg
                ProcessSketchParabola swApp, swModel, swSketch, swSkParabola
            Case Default
                Debug.Assert False
        End Select
```

```
    Next vSkSeg
```

```
End Sub
```

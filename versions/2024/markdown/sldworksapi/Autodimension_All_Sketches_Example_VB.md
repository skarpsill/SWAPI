---
title: "Autodimension All Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_All_Sketches_Example_VB.htm"
---

# Autodimension All Sketches Example (VBA)

This example shows how to autodimension all under-constrained sketches in a part.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts two sketches.
' 3. Autodimensions the sketches.
' 4. Examine the Immediate window.
'-----------------------------------------------------------
Option Explicit
```

```
Const swTnProfileFeature As String = "ProfileFeature"
Const nTolerance As Double = 0.00000001
```

```
Sub FindAllUnderConstrainedSketches(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, sSketchNameArr() As String)
```

```
    Dim swPart As SldWorks.PartDoc
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
```

```
    Set swPart = swModel
    Set swFeat = swPart.FirstFeature
    Do While Not swFeat Is Nothing
        If swTnProfileFeature = swFeat.GetTypeName2 Then
            Set swSketch = swFeat.GetSpecificFeature2
            If swUnderConstrained = swSketch.GetConstrainedStatus Then
                sSketchNameArr(UBound(sSketchNameArr)) = swFeat.Name
                ReDim Preserve sSketchNameArr(UBound(sSketchNameArr) + 1)
            End If
        End If
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    ' Remove last empty sketch name
    ReDim Preserve sSketchNameArr(UBound(sSketchNameArr) - 1)
```

```
End Sub
```

```
Function GetAllSketchLines(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch) As Variant
```

```
    Dim vSketchSegArr As Variant
    Dim vSketchSeg As Variant
    Dim swSketchSeg As SldWorks.sketchSegment
    Dim swSketchCurrLine As SldWorks.SketchLine
    Dim swSketchLineArr() As SldWorks.SketchLine
    ReDim swSketchLineArr(0)
```

```
    vSketchSegArr = swSketch.GetSketchSegments
    If Not IsEmpty(vSketchSegArr) Then
        For Each vSketchSeg In vSketchSegArr
            Set swSketchSeg = vSketchSeg
            If swSketchLINE = swSketchSeg.GetType Then
                Set swSketchCurrLine = swSketchSeg
                Set swSketchLineArr(UBound(swSketchLineArr)) = swSketchCurrLine
                ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) + 1)
            End If
        Next
    End If
```

```
    If 0 = UBound(swSketchLineArr) Then
        ' No straight lines in this sketch
        GetAllSketchLines = Empty
        Exit Function
    End If
```

```
    ' Remove last empty sketch line
    ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) - 1)
    GetAllSketchLines = swSketchLineArr
```

```
End Function
```

```
Function GetSketchPoint(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchPt As SldWorks.SketchPoint) As Boolean
```

```
    Dim vSketchPtArr As Variant

    vSketchPtArr = swSketch.GetSketchPoints2
    If Not IsEmpty(vSketchPtArr) Then
        ' Use first point
        Set swSketchPt = vSketchPtArr(0)
        GetSketchPoint = True
        Exit Function
    End If
```

```
    GetSketchPoint = False
```

```
End Function
```

```
Function FindVerticalOrigin(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchSegVert As SldWorks.sketchSegment, swSketchPtVert As SldWorks.SketchPoint) As Boolean
```

```
    Dim vSketchLineArr As Variant
    Dim vSketchLine As Variant
    Dim swSketchCurrLine As SldWorks.SketchLine
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
```

```
    ' Try to get first vertical line
    vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
```

```
    If Not IsEmpty(vSketchLineArr) Then
        For Each vSketchLine In vSketchLineArr
            Set swSketchCurrLine = vSketchLine
            Set swStartPt = swSketchCurrLine.GetStartPoint2
            Set swEndPt = swSketchCurrLine.GetEndPoint2
```

```
            If Abs(swStartPt.X - swEndPt.X) < nTolerance Then
                Set swSketchSegVert = swSketchCurrLine
                FindVerticalOrigin = True
                Exit Function
            End If
        Next
    End If
```

```
    ' Try to get the first point
    FindVerticalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtVert)
```

```
End Function
```

```
Function FindHorizontalOrigin(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchSegHoriz As SldWorks.sketchSegment, swSketchPtHoriz As SldWorks.SketchPoint) As Boolean
```

```
    Dim vSketchLineArr As Variant
    Dim vSketchLine As Variant
    Dim swSketchCurrLine As SldWorks.SketchLine
    Dim swStartPt As SldWorks.SketchPoint
    Dim swEndPt As SldWorks.SketchPoint
```

```
    ' Try to get first horizontal line
    vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
```

```
    If Not IsEmpty(vSketchLineArr) Then
        For Each vSketchLine In vSketchLineArr
            Set swSketchCurrLine = vSketchLine
            Set swStartPt = swSketchCurrLine.GetStartPoint2
            Set swEndPt = swSketchCurrLine.GetEndPoint2
```

```
            If Abs(swStartPt.Y - swEndPt.Y) < nTolerance Then
                Set swSketchSegHoriz = swSketchCurrLine
                FindHorizontalOrigin = True
                Exit Function
            End If
        Next
    End If
```

```
    ' Try to get the first point
    FindHorizontalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtHoriz)
```

```
End Function
```

```
Function AutoDimensionSketch(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch) As Long
```

```
    Dim swFeat As SldWorks.Feature
    Dim swSketchSegHoriz As SldWorks.sketchSegment
    Dim swSketchPtHoriz As SldWorks.SketchPoint
    Dim swSketchSegVert As SldWorks.sketchSegment
    Dim swSketchPtVert As SldWorks.SketchPoint
    Dim swSketchMgr as SldWorks.SketchManager
    Dim bRet As Boolean
```

```
    If False = FindHorizontalOrigin(swApp, swModel, swSketch, swSketchSegHoriz, swSketchPtHoriz) Then
        AutoDimensionSketch = swAutodimStatusDatumLineNotHorizontal
        Exit Function
    End If
```

```
    If False = FindVerticalOrigin(swApp, swModel, swSketch, swSketchSegVert, swSketchPtVert) Then
        AutoDimensionSketch = swAutodimStatusDatumLineNotVertical
        Exit Function
    End If
```

```
    Set swFeat = swSketch
    bRet = swFeat.Select2(False, 0)
```

```
    ' Editing sketch clears selections
    swModel.EditSketch
```

```
    ' Reselect sketch segments for autodimensioning
    If Not swSketchSegVert Is Nothing Then
        ' Vertical line is for horizontal datum
        bRet = swSketchSegVert.Select4(True, Nothing)
    ElseIf Not swSketchPtHoriz Is Nothing Then
             bRet = swSketchPtHoriz.Select4(True, Nothing)
    ElseIf Not swSketchPtVert Is Nothing Then
            ' Use any sketch point for horizontal datum
             bRet = swSketchPtVert.Select4(True, Nothing)
    End If
```

```
    If Not swSketchSegHoriz Is Nothing Then
        ' Horizontal line is for vertical datum
        bRet = swSketchSegHoriz.Select4(True, Nothing)
    ElseIf Not swSketchPtVert Is Nothing Then
        bRet = swSketchPtVert.Select4(True, Nothing)
    ElseIf Not swSketchPtHoriz Is Nothing Then
            ' Use any sketch point for vertical datum
            bRet = swSketchPtHoriz.Select4(True, Nothing)
    End If
```

```
    ' No straight lines, probably contains circles,
    ' so use sketch points for datums
    If IsEmpty(GetAllSketchLines(swApp, swModel, swSketch)) Then
        If Not swSketchPtHoriz Is Nothing Then
            bRet = swSketchPtHoriz.Select4(False, Nothing)
        ElseIf Not swSketchPtVert Is Nothing Then
            bRet = swSketchPtVert.Select4(False, Nothing)
        End If
    End If
```

```
    AutoDimensionSketch = swSketch.AutoDimension2(swAutodimEntitiesAll, swAutodimSchemeBaseline, swAutodimHorizontalPlacementBelow, swAutodimSchemeBaseline, swAutodimVerticalPlacementLeft)
```

```
    ' Redraw so dimensions are displayed
    swModel.GraphicsRedraw2
```

```
    ' Exit sketch mode
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch False
```

```
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swPart As SldWorks.PartDoc
    Dim sketchLines As Variant
    Dim sSketchNameArr() As String
    Dim sSketchName As Variant
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim sketchSegment As SldWorks.sketchSegment
    Dim swSketchMgr As SldWorks.SketchManager
    Dim nRetVal As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Create new part document and sketch
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchMgr = swModel.SketchManager
    sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 7.11560575730914E-02, -4.80714437538268E-02, 0)
    swModel.ClearSelection2 True
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    sketchLines = swSketchMgr.CreateCornerRectangle(-0.100496797175254, 4.81170506199078E-02, 0, -5.06046179404507E-02, 1.00165849869995E-02, 0)
    swModel.ClearSelection2 True
    Set sketchSegment = swSketchMgr.CreateCircle(-0.06189, -0.041869, 0#, -0.066641, -0.077213, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    Set sketchSegment = swSketchMgr.CreateCircle(-0.032637, 0.106589, 0#, -0.021539, 0.095387, 0#)
    swModel.ClearSelection2 (True)
    Set sketchSegment = swSketchMgr.CreateCircle(0#, 0.083617, 0#, 0.01255, 0.067729, 0#)
    swModel.ClearSelection2 (True)
    swSketchMgr.InsertSketch (True)
    swModel.ClearSelection2 (True)
```

```
    Set swPart = swModel
```

```
    ReDim sSketchNameArr(0)
```

```
    ' Find all under-constrained sketches
    FindAllUnderConstrainedSketches swApp, swModel, sSketchNameArr
```

```
    ' Autodimension all under-constrained sketches
    For Each sSketchName In sSketchNameArr
        Set swFeat = swPart.FeatureByName(sSketchName)
        Set swSketch = swFeat.GetSpecificFeature2
```

```
        nRetVal = AutoDimensionSketch(swApp, swModel, swSketch)
```

```
        Debug.Print sSketchName & " autodimensioned (0 = success): " & nRetVal
    Next
```

```
End Sub
```

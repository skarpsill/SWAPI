---
title: "Find Outside Edges of Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Outside_Edges_of_Face_Example_VB.htm"
---

# Find Outside Edges of Face Example (VBA)

This example shows how to find the outside edges of the selected face.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part and select a face.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Finds the outside edges of the selected face
'    and creates a 3D sketch using the outside edges.
' 2. Examine the Immediate window, selected face,
'    FeatureManager design tree, and 3D sketch.
'---------------------------------------------------
```

```
Option Explicit
```

```
Sub CreateTessCurve(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swTrimCurve As SldWorks.Curve)
    Const nChordTol As Double = 0.001   ' Meters
    Const nLengthTol As Double = 0.001   ' Meters
    Dim nStartParam As Double
    Dim nEndParam As Double
    Dim bIsClosed As Boolean
    Dim bIsPeriodic As Boolean
    Dim vStartPt As Variant
    Dim vEndPt As Variant
    Dim vTessPts As Variant
    Dim swSketchSeg As SldWorks.SketchSegment
    Dim bRet As Boolean
    Dim i As Long
```

```
    ' Really not needed because curve is a trimmed curve,
    ' so could pass in trim points as parameters
    bRet = swTrimCurve.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
    vStartPt = swTrimCurve.Evaluate(nStartParam)
    vEndPt = swTrimCurve.Evaluate(nEndParam)
```

```
    vTessPts = swTrimCurve.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt))
```

```
    ' Disable VBA range checking because tessellation points
    ' might not be a multiple of 6
    On Error Resume Next
    For i = 0 To UBound(vTessPts) Step 3
        Set swSketchSeg = swModel.CreateLine2(vTessPts(i + 0), vTessPts(i + 1), vTessPts(i + 2), vTessPts(i + 3), vTessPts(i + 4), vTessPts(i + 5))
    Next i
```

```
    On Error GoTo 0
```

```
End Sub
```

```
Sub CreateTessLoop(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swLoop As SldWorks.Loop2)
    Dim vEdgeArr As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim swSketch As SldWorks.Sketch
    Dim bRet As Boolean
```

```
    swModel.Insert3DSketch2 False
    swModel.SetAddToDB True
    swModel.SetDisplayWhenAdded False
    Set swSketch = swModel.GetActiveSketch2
    vEdgeArr = swLoop.GetEdges
    For Each vEdge In vEdgeArr
        Set swEdge = vEdge
        Set swCurve = swEdge.GetCurve
        CreateTessCurve swApp, swModel, swSketch, swCurve
    Next vEdge
```

```
    swModel.SetDisplayWhenAdded True
    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
```

```
    bRet = swModel.EditRebuild3
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swLoop As SldWorks.Loop2
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "FaceArea  = " & swFace.GetArea * 1000000# & " mm^2"
    Debug.Print "  LoopCount    = " & swFace.GetLoopCount
    Debug.Print ""
```

```
    Set swLoop = swFace.GetFirstLoop
    Do While Not swLoop Is Nothing
        i = i + 1
        Debug.Print "  Loop(" & i & ")"
        Debug.Print "    IsOuter    = " & swLoop.IsOuter
        Debug.Print "    IsSingular = " & swLoop.IsSingular
        If swLoop.IsOuter Then
            CreateTessLoop swApp, swModel, swLoop
        End If
        Set swLoop = swLoop.GetNext
    Loop
```

```
End Sub
```

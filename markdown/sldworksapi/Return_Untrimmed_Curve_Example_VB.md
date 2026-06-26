---
title: "Create Trimmed Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Return_Untrimmed_Curve_Example_VB.htm"
---

# Create Trimmed Curve Example (VBA)

This example shows how to create a trimmed curve on a selected face.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part and select a face.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a trimmed curve.
 ' 2. Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFace                  As SldWorks.Face2
     Dim swSurf                  As SldWorks.Surface
     Dim vFaceUV                 As Variant
     Dim surfParam               As SldWorks.SurfaceParameterizationData
     Dim swCurveU                As SldWorks.Curve
     Dim vUIsoStartPt            As Variant
     Dim vUIsoEndPt              As Variant
     Const nChordTol             As Double = 0.001
     Const nLengthTol            As Double = 0.001
     Dim nStartParam             As Double
     Dim nEndParam               As Double
     Dim bIsClosed               As Boolean
     Dim bIsPeriodic             As Boolean
     Dim vStartPt                As Variant
     Dim vEndPt                  As Variant
     Dim vTessPts                As Variant
     Dim swSketchSeg             As SldWorks.SketchSegment
     Dim i                       As Long
     Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFace = swSelMgr.GetSelectedObject6(1, -1)
     Set swSurf = swFace.GetSurface

    vFaceUV = swFace.GetUVBounds
     Set surfParam = swSurf.Parameterization2
    vUIsoStartPt = swSurf.Evaluate((vFaceUV(0) + vFaceUV(1)) / 2#, vFaceUV(2), 0, 0)
     vUIsoEndPt = swSurf.Evaluate((vFaceUV(0) + vFaceUV(1)) / 2#, vFaceUV(3), 0, 0)
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Face:"
     Debug.Print "    uRange   = [" & vFaceUV(0) & " , " & vFaceUV(1) & "]"
     Debug.Print "    vRange   = [" & vFaceUV(2) & " , " & vFaceUV(3) & "]"
     Debug.Print "  Surface:"
     Debug.Print "    uRange   = [" & surfParam.UMin & " , " & surfParam.UMax & "]"
     Debug.Print "    vRange   = [" & surfParam.VMin & " , " & surfParam.VMax & "]"
     Debug.Print "  U Curve:"
     Debug.Print "    Start Pt = (" & vUIsoStartPt(0) * 1000 & ", " & vUIsoStartPt(1) * 1000 & ", " & vUIsoStartPt(2) * 1000 & ") mm"
     Debug.Print "    End   Pt = (" & vUIsoEndPt(0) * 1000 & ", " & vUIsoEndPt(1) * 1000 & ", " & vUIsoEndPt(2) * 1000 & ") mm"

    ' Create untrimmed U curve
     Set swCurveU = swSurf.MakeIsoCurve2(False, (vFaceUV(0) + vFaceUV(1)) / 2#)

    ' Trim U curve to start and end of U range
     Set swCurveU = swCurveU.CreateTrimmedCurve2(vUIsoStartPt(0), vUIsoStartPt(1), vUIsoStartPt(2), vUIsoEndPt(0), vUIsoEndPt(1), vUIsoEndPt(2))

    Debug.Print "  Trimmed U curve:"
     bRet = swCurveU.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
     Debug.Print "    Start parameter is " & nStartParam
     Debug.Print "    End parameter is " & nEndParam
     Debug.Print "    Is closed? " & bIsClosed
     Debug.Print "    Is periodic? " & bIsPeriodic

    vStartPt = swCurveU.Evaluate2(nStartParam, 0)
     vEndPt = swCurveU.Evaluate2(nEndParam, 0)
    vTessPts = swCurveU.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt))

     Dim swSketchMgr as SldWorks.SketchManager
     Set swSketchMgr = swModel.SketchManager
    swSketchMgr.Insert3DSketch False
     swModel.SetAddToDB True

    ' Disable VB range checking since tessellation points
     ' cannot be multiples of 6
    On Error Resume Next
    For i = 0 To UBound(vTessPts) Step 3
         Set swSketchSeg = swModel.CreateLine2(vTessPts(i + 0), vTessPts(i + 1), vTessPts(i + 2), vTessPts(i + 3), vTessPts(i + 4), vTessPts(i + 5))
     Next i
    On Error GoTo 0
     swModel.SetAddToDB False
     swSketchMgr.Insert3DSketch True
    bRet = swModel.EditRebuild3

End Sub
```

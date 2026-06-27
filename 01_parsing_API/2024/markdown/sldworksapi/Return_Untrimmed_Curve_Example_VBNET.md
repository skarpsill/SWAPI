---
title: "Create Trimmed Curve Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Return_Untrimmed_Curve_Example_VBNET.htm"
---

# Create Trimmed Curve Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swSketchMgr As SketchManager
         Dim swFace As Face2
         Dim swSurf As Surface
         Dim vFaceUV As Object
         Dim surfParam As SurfaceParameterizationData
         Dim swCurveU As Curve
         Dim vUIsoStartPt As Object
         Dim vUIsoEndPt As Object
         Const nChordTol As Double = 0.001
         Const nLengthTol As Double = 0.001
         Dim nStartParam As Double
         Dim nEndParam As Double
         Dim bIsClosed As Boolean
         Dim bIsPeriodic As Boolean
         Dim vStartPt As Object
         Dim vEndPt As Object
         Dim vTessPts As Object
         Dim swSketchSeg As SketchSegment
         Dim i As  Integer
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFace = swSelMgr.GetSelectedObject6(1, -1)
         swSurf = swFace.GetSurface

         vFaceUV = swFace.GetUVBounds
         surfParam = swSurf.Parameterization2

         vUIsoStartPt = swSurf.Evaluate((vFaceUV(0) + vFaceUV(1)) / 2.0#, vFaceUV(2), 0, 0)
         vUIsoEndPt = swSurf.Evaluate((vFaceUV(0) + vFaceUV(1)) / 2.0#, vFaceUV(3), 0, 0)

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Face:")
         Debug.Print("    uRange   = [" & vFaceUV(0) & " , " & vFaceUV(1) & "]")
         Debug.Print("    vRange   = [" & vFaceUV(2) & " , " & vFaceUV(3) & "]")
         Debug.Print("  Surface:")
         Debug.Print("    uRange   = [" & surfParam.UMin & " , " & surfParam.UMax & "]")
         Debug.Print("    vRange   = [" & surfParam.VMin & " , " & surfParam.VMax & "]")
         Debug.Print("  U Curve:")
         Debug.Print("    Start Pt = (" & vUIsoStartPt(0) * 1000 & ", " & vUIsoStartPt(1) * 1000 & ", " & vUIsoStartPt(2) * 1000 & ") mm")
         Debug.Print("    End   Pt = (" & vUIsoEndPt(0) * 1000 & ", " & vUIsoEndPt(1) * 1000 & ", " & vUIsoEndPt(2) * 1000 & ") mm")

         ' Create untrimmed U curve
         swCurveU = swSurf.MakeIsoCurve2(False, (vFaceUV(0) + vFaceUV(1)) / 2.0#)

         ' Trim U curve to start and end of U range
         swCurveU = swCurveU.CreateTrimmedCurve2(vUIsoStartPt(0), vUIsoStartPt(1), vUIsoStartPt(2), vUIsoEndPt(0), vUIsoEndPt(1), vUIsoEndPt(2))

         Debug.Print("  Trimmed U curve:")
         bRet = swCurveU.GetEndParams(nStartParam, nEndParam, bIsClosed, bIsPeriodic)
         Debug.Print("    Start parameter is " & nStartParam)
         Debug.Print("    End parameter is " & nEndParam)
         Debug.Print("    Is closed? " & bIsClosed)
         Debug.Print("    Is periodic? " & bIsPeriodic)

         vStartPt = swCurveU.Evaluate2(nStartParam, 0)
         vEndPt = swCurveU.Evaluate2(nEndParam, 0)

         vTessPts = swCurveU.GetTessPts(nChordTol, nLengthTol, (vStartPt), (vEndPt))

         swSketchMgr = swModel.SketchManager

         swSketchMgr  .Insert3DSketch(False)
         swModel.SetAddToDB(True)

         ' Disable VB range checking since tessellation points
         ' cannot be multiples of 6

         On Error Resume Next

         For i = 0 To (UBound(vTessPts) - 3) Step 3
             swSketchSeg = swModel.CreateLine2(vTessPts(i + 0), vTessPts(i + 1), vTessPts(i + 2), vTessPts(i + 3), vTessPts(i + 4), vTessPts(i + 5))
         Next i

         On Error GoTo 0

         swModel.SetAddToDB(False)
         swSketchMgr  .Insert3DSketch(True)

         bRet = swModel.EditRebuild3

     End Sub

     Public swApp As SldWorks

 End  Class
```

---
title: "Create Equation-driven Curve Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Equation-driven_Curve_Example_VBNET.htm"
---

# Create Equation-driven Curve Example (VB.NET)

This example shows how to create and modify an equation-driven curve.

```vb
'---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a new part document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a 2D sketch and creates an equation-driven spline of
 '    a sine curve.
 ' 2. Examine the graphics area, then Press F5.
 ' 3. Edits the curve and creates a cosine curve.
 ' 4. Reduces the number of points in the spline.
 ' 5. Examine the Immediate window and graphics area.
 '----------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim boolstatus As Boolean
     Dim y As  String
     Dim r1 As Double
     Dim r2 As Double
     Dim rad As Boolean
     Dim ang As Double
     Dim xOff As Double, yOff As Double
     Dim LockStart As Boolean, LockEnd As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         boolstatus = swExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  False, 0,  Nothing, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)

         Dim skSegment As SketchSegment
         skSegment = swModel.SketchManager.CreateEquationSpline2("", "sin(x)", "", "0", "6.28", False, 0, 0, 0, True, True)
         swModel.ViewZoomtofit2()

         Stop
         ' Examine graphics area, then press F5

         Dim skSpline As SketchSpline
         skSpline = skSegment
         Call skSpline.GetEquationParameters(y, r1, r2, rad, ang, xOff, yOff, LockStart, LockEnd)

         Debug.Print("y: " & y)
         Debug.Print("range start: " & r1)
         Debug.Print("range end: " & r2)
         Debug.Print("radian?: " & rad)
         Debug.Print("ang offset: " & ang)
         Debug.Print("x offset: " & xOff)
         Debug.Print("y offset: " & yOff)
         Debug.Print("lock start: " & LockStart)
         Debug.Print("lock end: " & LockEnd)

         ' Change spline to a cosine curve
         y =  "cos(x)"
         Call skSpline.SetEquationParameters(y, r1, r2, rad, ang, xOff, yOff, LockStart, LockEnd)

         ' Reduce the number of points in the spline
         skSpline.Simplify(0.0#)

         swModel.SketchManager.InsertSketch(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```

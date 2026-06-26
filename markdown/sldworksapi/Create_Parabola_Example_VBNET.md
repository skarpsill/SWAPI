---
title: "Create Parabola Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Parabola_Example_VBNET.htm"
---

# Create Parabola Example (VB.NET)

This example shows how to create a parabola and get its corresponding equation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Verify that the specified template exists.
 '
 ' Postconditions:
 ' 1. Inserts a sketch.
 ' 2. Creates a parabola.
 ' 3. Inspect the Immediate window for the parabolic equation.
 '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Math
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Const pi As Double = 3.14159265

     Sub main()

         Dim swModel As ModelDoc2
         swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)

         If swModel Is Nothing Then
             swApp.SendMsgToUser2("A part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)
             Exit Sub
         End If

         Dim modelType As Integer
         modelType = swModel.GetType

         If modelType <> swDocumentTypes_e.swDocPART  Then
             swApp.SendMsgToUser2("A part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)
             Exit Sub
         End If

         'Select a plane on which to sketch
         If SelectPlane(swModel) = False Then
             MsgBox("Could not select plane.")
             Exit Sub
         End If

         'Get point data
         Dim pFocal As SketchPoint
         Dim pApex As SketchPoint
         Dim pStart As SketchPoint
         Dim pEnd As SketchPoint
         Dim swSkMgr As SketchManager
         swSkMgr = swModel.SketchManager

         Dim swSelMgr As SelectionMgr
         swSelMgr = swModel.SelectionManager

         Dim swSketch As Sketch
         swSkMgr.InsertSketch(True)
         swSketch = swSkMgr.ActiveSketch

         ' Focal point
         pFocal = swSkMgr.CreatePoint(0, -0.025930732990048, 0)
         ' Apex point
         pApex = swSkMgr.CreatePoint(0.0110754938634727, -0.0485199777778575, 0)
         ' Start point
         pStart = swSkMgr.CreatePoint(0.057136404168939, 0.0869770346454566, 0)
         ' End point
         pEnd = swSkMgr.CreatePoint(-0.120690397734139, -0.00465528735997846, 0)

         Dim vPoint As Object

         ' Make sure a sketch is active
         If swSketch Is Nothing Then
             MsgBox("Please sketch a focal point, apex point, start point, and end point.")
             Exit Sub
         End If

         vPoint = swSketch.GetSketchPoints2

         ' Make sure the sketch has the necessary points
         If UBound(vPoint) <= 2 Then
             MsgBox("                            You did not sketch enough points to define the parabola." & vbNewLine & " Please sketch a focal point, apex point, start point, and end point.")
             Exit Sub
         End If

         Dim SkParabola As SketchParabola
         SkParabola = swModel.SketchManager.CreateParabola(pFocal.X, pFocal.Y, 0, pApex.X, pApex.Y, 0, pStart.X, pStart.Y, 0, pEnd.X, pEnd.Y, 0)

         swModel.ViewZoomtofit2()

         'Extract information about the parabola
         pApex = SkParabola.GetApexPoint2
         pStart = SkParabola.GetStartPoint2
         pEnd = SkParabola.GetEndPoint2
         pFocal = SkParabola.GetFocalPoint2

         Debug.Print("      Apex  Point   = (" & pApex.X * 1000   ", " & pApex.Y * 1000 & ", " & pApex.Z * 1000 & ") mm")
         Debug.Print("      Start Point   = (" & pStart.X * 1000   ", " & pStart.Y * 1000 & ", " & pStart.Z * 1000 & ") mm")
         Debug.Print("      End Point   = (" & pEnd.X * 1000   ", " & pEnd.Y * 1000 & ", " & pEnd.Z * 1000 & ") mm")
         Debug.Print("      Focal Point   = (" & pFocal.X * 1000   ", " & pFocal.Y * 1000 & ", " & pFocal.Z * 1000 & ") mm")

         ' Define point parameters
         If Not pFocal.Z = 0 Or Not pApex.Z = 0 Or Not pStart.Z = 0 Or Not pEnd.Z = 0 Then
             MsgBox("Need a 2D sketch.")
             Exit Sub
         End If

         ' Algebraic equation of parabola
         Dim h As  Double
         Dim p As  Double
         Dim k As  Double

         h = pApex.X
         k = pApex.Y

         ' Correct anomalies when the parabola is aligned with the x and y axes
         If pFocal.Y = pApex.Y Then
             If pFocal.X > pApex.X Then
                 p = Sqrt((pFocal.Y - pApex.Y) ^ 2 + (pFocal.X - pApex.X) ^ 2)
             Else
                 p = -(Sqrt((pFocal.Y - pApex.Y) ^ 2 + (pFocal.X - pApex.X) ^ 2))
             End If
         End If

         If pFocal.X = pApex.X Then
             If pFocal.Y > pApex.Y Then
                 p = Sqrt((pFocal.Y - pApex.Y) ^ 2 + (pFocal.X - pApex.X) ^ 2)
             Else
                 p = -(Sqrt((pFocal.Y - pApex.Y) ^ 2 + (pFocal.X - pApex.X) ^ 2))
             End If
         End If

         If pFocal.X <> pApex.X And pFocal.Y <> pApex.Y Then
             p = (Sqrt((pFocal.Y - pApex.Y) ^ 2 + (pFocal.X - pApex.X) ^ 2))
         End If

         Dim a As  Double
         Dim b As  Double
         Dim c As  Double
         Dim c1 As Double
         Dim c2 As Double
         Dim c3 As Double
         Dim c4 As Double
         Dim c5 As Double
         Dim c6 As Double
         Dim theta As Double

         ' Obtain the correct value for theta as the parabola rotates
         If pFocal.X <> pApex.X And pFocal.Y <> pApex.Y Then
             a = 1 / (4 * p)
             b = -k / (2 * p)
             c = (k * k / (4 * p)) + h

             ' Theta in first quadrant
             If pFocal.Y > pApex.Y And pFocal.X > pApex.X Then
                 theta = Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))
             End If

             ' Theta in second quadrant
             If pFocal.Y > pApex.Y And pFocal.X < pApex.X Then
                 theta = (Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + pi
             End If

             ' Theta in the third quadrant
             If pFocal.Y < pApex.Y And pFocal.X < pApex.X Then
                 theta = (Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + pi
             End If

             ' Theta in the fourth quadrant
             If pFocal.Y < pApex.Y And pFocal.X > pApex.X Then
                 theta = (Atan((pFocal.Y - pApex.Y) / (pFocal.X - pApex.X))) + (2 * pi)
             End If

             c1 = Round(a * (Sin(theta)) ^ 2, 2)
             c2 = Round(-a * Sin(2 * theta), 2)
             c3 = Round(a * (Cos(theta)) ^ 2, 2)
             c4 = Round((-b * Sin(theta)) - Cos(theta), 2)
             c5 = Round((b * Cos(theta)) - Sin(theta), 2)
             c6 = Round(c, 2)

             Debug.Print("Equation of the parabola: " & c1   "x^2 + " & c2 & "xy + " & c3 & "y^2 + " & c4 & "x + " & c5 & "y + " & c6 & " = 0")

         End If

         ' If the parabola has a vertical axis of symmetry
         If pFocal.X = pApex.X Then
             a = 1 / (4 * p)
             b = -h / (2 * p)
             c = (h ^ 2 / (4 * p)) + k
             c1 = Round(a, 2)
             c4 = Round(b, 2)
             c6 = Round(c, 2)
             Debug.Print("Equation of the parabola: y = " & c1   "x^2 + " & c4 & "x + " & c6)
         End If

         ' If the parabola has a horizontal axis of symmetry
         If pFocal.Y = pApex.Y Then
             a = 1 / (4 * p)
             b = -k / (2 * p)
             c = (k * k / (4 * p)) + h
             c3 = Round(a, 2)
             c5 = Round(b, 2)
             c6 = Round(c, 2)
             Debug.Print("Equation of the parabola: x =" & c3   "y^2 + " & c5 & "y + " & c6)
         End If

         swSkMgr.InsertSketch(True)

     End Sub

     Public Function SelectPlane(ByVal Plane As ModelDoc2) As Boolean

         Dim featureTemp As Feature
         featureTemp = Plane.FirstFeature

         While Not featureTemp Is Nothing
             Dim sFeatureName As String
             sFeatureName = featureTemp.GetTypeName2

             If sFeatureName = "RefPlane" Then
                 featureTemp.Select2(True, 0)
                 SelectPlane = True
                 Exit Function
             End If

             featureTemp = featureTemp.GetNextFeature

         End While

     End Function

     Public swApp As SldWorks

 End  Class
```

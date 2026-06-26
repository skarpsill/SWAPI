---
title: "Create Ellipse Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ellipse_Example_VBNET.htm"
---

# Create Ellipse Example (VB.NET)

This example shows how to create an ellipse circumscribing two sketch points.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Open a a part document that contains
 ' an active sketch that has two sketch points.
 '
 ' Postconditions:
 ' 1. Creates an ellipse circumscribing the two sketch points.
 ' 2. Inspect Immediate window for ellipse point data, theta, and equation.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics
 Imports System.Math

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swMath As MathUtility

         swModel = swApp.ActiveDoc
         swMath = swApp.GetMathUtility

         ' Check whether document is active
         If swModel Is Nothing Then
             swApp.SendMsgToUser2("A part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)
             Exit Sub
         End If

         ' Check whether document is a part
         Dim modelType As Long
         modelType = swModel.GetType

         If modelType <> swDocumentTypes_e.swDocPART  Then
             swApp.SendMsgToUser2("A part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)
             Exit Sub
         End If

         ' Select a plane on which to sketch
         If SelectPlane(swModel) = False Then
             MsgBox("Could not select plane.")
             Exit Sub
         End If

         Dim swSkMgr As SketchManager
         swSkMgr = swModel.SketchManager

         Dim swSketch As Sketch
         swSketch = swSkMgr.ActiveSketch

         ' Check whether a sketch is active
         If swSketch Is Nothing Then
             MsgBox("Please sketch a point for the center point, sketch another point to define the major axis, and run the macro again.")
             Exit Sub
         End If

         Const pi As Double = 3.1415926

         ' Get data from the points
         Dim CtrPt As SketchPoint = Nothing
         Dim MajPt As SketchPoint = Nothing

         swSkMgr = swModel.SketchManager
         swSketch = swSkMgr.ActiveSketch

         Dim vPoint As Object

         Dim i As  Integer

         ' Make sure the sketch is active
         If swSketch Is Nothing Then
             MsgBox("Please sketch a point for the center point, sketch another point to define the  major axis, and run the macro again.")
             Exit Sub
         End If

         ' Make sure that at least two sketch points exist to define the position of the ellipse and its major axis
         vPoint = swSketch.GetSketchPoints2
         If UBound(vPoint) = 0 Then
             MsgBox("Please sketch a point for the center point, sketch another point to define the major axis, and run the macro again.")
             Exit Sub
         End If

         For i = 0 To UBound(vPoint)
             If i = 0 Then
                 CtrPt = vPoint(i)
             End If

             If i = 1 Then
                 MajPt = vPoint(i)
             End If
         Next i

         Dim MajVec As MathVector
         Dim dirArr(2) As Double

         dirArr(0) = MajPt.X - CtrPt.X
         dirArr(1) = MajPt.Y - CtrPt.Y
         dirArr(2) = 0

         MajVec = swMath.CreateVector((dirArr))
         Dim MajVecunit As MathVector

         MajVecunit = MajVec.Normalise
         Dim normVec As MathVector

         dirArr(0) = 0
         dirArr(1) = 0
         dirArr(2) = 1

         normVec = swMath.CreateVector((dirArr))

         Dim MinVecunit As MathVector
         Dim MinVec As MathVector
         Dim u As  Double

         MinVecunit = normVec.Cross(MajVecunit)

         Dim minlength As Integer
         minlength = 50
         u = minlength / 1000

         MinVec = MinVecunit.Scale(u)

         ' Ensure that the minor axis is less than the major axis so that
         ' the equation returned is correct
         If MajVec.GetLength < MinVec.GetLength  Then
             MsgBox("The length of the minor axis must be less than that of the major axis.")
             Exit Sub
         End If

         If Not CtrPt.Z = 0 Or Not MajPt.Z = 0 Or Not MinVec.ArrayData(2) = 0 Then
             MsgBox("2D sketch only.")
             Exit Sub
         End If

         ' Sketch the ellipse
         Dim SkEllipse As SketchEllipse
         SkEllipse = swModel.SketchManager.CreateEllipse(CtrPt.X, CtrPt.Y, 0, MajPt.X, MajPt.Y, 0, CtrPt.X + MinVec.ArrayData(0), CtrPt.Y + MinVec.ArrayData(1), 0)

         swModel.ViewZoomtofit2()

         ' Check that the sketch is an ellipse
         Dim vEllipse As Object
         vEllipse = swSketch.GetEllipses3

         If swSketch.GetEllipseCount = 0 Then
             MsgBox("An ellipse was not created. Please make sure that the sketch contains at least one ellipse.")
             Exit Sub
         End If

         ' Extract information about the ellipse
         Dim swStartPt As SketchPoint
         Dim swEndPt As SketchPoint
         Dim swCtrPt As SketchPoint
         Dim swMajPt As SketchPoint
         Dim swMinPt As SketchPoint

         swStartPt = SkEllipse.GetStartPoint2
         swEndPt = SkEllipse.GetEndPoint2
         swCtrPt = SkEllipse.GetCenterPoint2
         swMajPt = SkEllipse.GetMajorPoint2
         swMinPt = SkEllipse.GetMinorPoint2

         Debug.Print("Sketch points")
         Debug.Print("      Start Point   = (" & swStartPt.X * 1000.0# & ", " & swStartPt.Y * 1000.0# & ", " & swStartPt.Z * 1000.0# & ") mm")
         Debug.Print("      End Point     = (" & swEndPt.X * 1000.0#   ", " & swEndPt.Y * 1000.0# & ", " & swEndPt.Z * 1000.0# & ") mm")
         Debug.Print("      Center Point  = (" & swCtrPt.X * 1000.0# & ", " & swCtrPt.Y * 1000.0# & ", " & swCtrPt.Z * 1000.0# & ") mm")
         Debug.Print("      Major Point   = (" & swMajPt.X * 1000.0#   ", " & swMajPt.Y * 1000.0# & ", " & swMajPt.Z * 1000.0# & ") mm")
         Debug.Print("      Minor Point   = (" & swMinPt.X * 1000.0#   ", " & swMinPt.Y * 1000.0# & ", " & swMinPt.Z * 1000.0# & ") mm")

         ' Algebraic equation for the ellipse
         Dim h As  Double
         Dim k As  Double
         Dim a As  Double
         Dim b As  Double
         Dim theta As Double

         h = swCtrPt.X
         k = swCtrPt.Y
         a = 1 / ((swMajPt.X - swCtrPt.X) ^ 2 + (swMajPt.Y - swCtrPt.Y) ^ 2)
         b = 1 / ((swMinPt.X - swCtrPt.X) ^ 2 + (swMinPt.Y - swCtrPt.Y) ^ 2)

         ' Return the tipping angle, theta; avoid divide by zero
         If swMajPt.X <> swCtrPt.X Then
             theta = Atan((swMajPt.Y - swCtrPt.Y) / (swMajPt.X - swCtrPt.X))
         Else
             theta = pi / 2
         End If

         Debug.Print("Theta of ellipse: " & theta)

         Dim c1 As Double
         Dim c2 As Double
         Dim c3 As Double
         Dim c4 As Double
         Dim c5 As Double
         Dim c6 As Double

         c1 = Round((a * (Cos(theta)) ^ 2) + (b * (Sin(theta)) ^ 2), 2)
         c2 = Round((a - b) * Sin(2 * theta), 2)
         c3 = Round((b * (Cos(theta)) ^ 2) + (a * (Sin(theta)) ^ 2), 2)
         c4 = Round((-2 * a * h * Cos(theta)) + (2 * b * k * Sin(theta)), 2)
         c5 = Round((-2 * a * h * Sin(theta)) - (2 * b * k * Cos(theta)), 2)
         c6 = Round(1 - (b * (k ^ 2)) - (a * (h ^ 2)), 2)

         Debug.Print("Equation of the ellipse: " & c1   "x^2 + " & c2 & "xy + " & c3 & "y^2 + " & c4 & "x + " & c5 & "y = " & c6)

         ' NOTE: The coefficients of x and y in this
         '       equation represent a translation in the x-y plane.
         '       If they are 0, then the ellipse was not translated.
         '       Similarly the coefficient of xy represents
         '       a rotation. If it is 0, then the ellipse
         '       was not rotated.
         '
         '       The units on each axis are in meters.

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

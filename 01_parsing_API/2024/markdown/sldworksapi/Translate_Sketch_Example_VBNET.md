---
title: "Translate Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Translate_Sketch_Example_VBNET.htm"
---

# Translate Sketch Example (VB.NET)

This example shows how to move a sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Creates a sketch.
' 2. Creates a parabola.
' 3. While observing the graphics area, press F5 at Stop
'    to move the sketch.
'----------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Sub main()

	        Dim swModel As ModelDoc2

	        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS
	2012\templates\Part.prtdot", 0, 0, 0)

	        If swModel Is Nothing Then

	            swApp.SendMsgToUser2("A
	part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)

	            Exit Sub

	        End If

	        Dim modelType As Integer

	        modelType = swModel.GetType

	        If modelType <> swDocumentTypes_e.swDocPART Then

	            swApp.SendMsgToUser2("A
	part document must be active.", swMessageBoxIcon_e.swMbWarning, swMessageBoxBtn_e.swMbOk)

	            Exit Sub

	        End If

	        'Select
	a plane on which to sketch

	        If SelectPlane(swModel) = False Then

	            MsgBox("Could not select plane.")

	            Exit Sub

	        End If

	        'Get
	point data

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

	        pFocal = swSkMgr.CreatePoint(0,
	-0.025930732990048, 0)

	        ' Apex point

	        pApex = swSkMgr.CreatePoint(0.0110754938634727,
	-0.0485199777778575, 0)

	        ' Start point

	        pStart = swSkMgr.CreatePoint(0.057136404168939,
	0.0869770346454566, 0)

	        ' End point

	        pEnd = swSkMgr.CreatePoint(-0.120690397734139,
	-0.00465528735997846, 0)

	        Dim vPoint As Object

	        '
	Make sure a sketch is active

	        If swSketch Is Nothing Then

	            MsgBox("Please sketch a focal point, apex point, start point, and end point.")

	            Exit Sub

	        End If

	        vPoint = swSketch.GetSketchPoints2

	        Dim SkParabola As SketchParabola

	        SkParabola = swModel.SketchManager.CreateParabola(pFocal.X, pFocal.Y, 0, pApex.X, pApex.Y, 0, pStart.X, pStart.Y, 0, pEnd.X, pEnd.Y, 0)

	        swModel.ViewZoomtofit2()

	        swSkMgr.InsertSketch(True)

	        Stop

	        swModel.SketchModifyTranslate(pApex.X, pApex.Y, 0.06, -0.01)

	    End Sub

	    Public Function SelectPlane(ByVal Plane As ModelDoc2) As Boolean

	        Dim featureTemp As Feature

	        featureTemp = Plane.FirstFeature

	        While Not featureTemp Is Nothing

	            Dim sFeatureName As String

	            sFeatureName = featureTemp.GetTypeName2

	            If sFeatureName = "RefPlane" Then

	                featureTemp.Select2(True,
	0)

	                SelectPlane = True

	                Exit Function

	            End If

	            featureTemp = featureTemp.GetNextFeature

	        End While

	    End Function

	    Public swApp As SldWorks

	End Class
```

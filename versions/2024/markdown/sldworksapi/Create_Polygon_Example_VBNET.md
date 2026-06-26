---
title: "Create Polygon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Polygon_Example_VBNET.htm"
---

# Create Polygon Example (VB.NET)

This example shows how to create a polygon.

```
'-------------------------------------------------------------------
' Preconditions: Open a part document.
'
' Postconditions:
' 1. Inserts a sketch.
' 2. Creates a six-sided polygon, circumscribed with a
'    construction circle.
' 3. Examine the graphics area.
'-------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swModelDocExt As ModelDocExtension

	    Dim swSketchMgr As SketchManager

	    Dim polygon() As Object

	    Sub main()

	        swModel = swApp.ActiveDoc

	        swModelDocExt = swModel.Extension

	        swSketchMgr = swModel.SketchManager

	        swSketchMgr.InsertSketch(False)

	        polygon = swSketchMgr.CreatePolygon(-2.5, 0.88, 0.0#, -2.21,
	-2.13, 0.0#, 6, False)

	        swModel.ViewZoomtofit2()

	        ' Set the selection mode to default

	        swModel.SetPickMode()

	        swSketchMgr.InsertSketch(True)

	    End Sub

	    Public swApp As SldWorks

	End Class
```

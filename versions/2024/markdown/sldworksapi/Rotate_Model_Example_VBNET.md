---
title: "Rotate Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Model_Example_VBNET.htm"
---

# Rotate Model Example (VB.NET)

This example shows how to rotate a model in the graphics area.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Watch the graphics while the macro runs.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Inserts and extrudes a rectangular sketch.
' 3. Rotates the sketch multiple times.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim myFeature As Feature

	    Dim vSkLines As Object

	    Dim boolstatus As Boolean

	    Sub main()

	        Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS
	2016\templates\Part.prtdot", 0, 0, 0)

	        boolstatus = Part.Extension.SelectByID2("Top
	Plane", "PLANE", -0.0567254111166863,
	0.00753958008310182, 0.0248109468921342, False, 0, Nothing, 0)

	        Part.SketchManager.InsertSketch(True)

	        vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0493169981371904,
	0.0173783707721528, 0, 0.0558925978888158, -0.0455595125648331, 0)

	        Part.ShowNamedView2("*Trimetric",
	8)

	        boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT",
	0, 0, 0, False,
	0, Nothing,
	0)

	        boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT",
	0, 0, 0, True,
	0, Nothing,
	0)

	        myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0,
	0, 0.016256, 0.00254, False, False, False, False,
	0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

	        Part.SelectionManager.EnableContourSelection = False

	        Part.ViewRotate()

	        Part.ViewRotateminusx()

	        Part.ViewRotateminusy()

	        Part.ViewRotateminusz()

	        Part.ViewRotateplusx()

	        Part.ViewRotateplusy()

	        Part.ViewRotateplusz()

	        Part.ViewRotXMinusNinety()

	        Part.ViewRotXPlusNinety()

	        Part.ViewRotYMinusNinety()

	        Part.ViewRotYPlusNinety()

	    End Sub

	    Public swApp As SldWorks

	End Class
```

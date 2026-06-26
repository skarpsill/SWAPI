---
title: "Insert Spline Point Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Spline_Point_Example_VBNET.htm"
---

# Insert Spline Point Example (VB.NET)

This example shows how to insert a spline point in a spline sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Sketches a spline containing four spline points.
' 2. Inserts a fifth spline point.
' 3. Examine the graphics area.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim skSegment As SketchSegment

	    Sub main()

	        Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS
	2017\templates\Part.prtdot", 0, 0, 0)

	        Dim pointArray As Object

	        Dim points(11) As Double

	        points(0) = -0.0625070182577474

	        points(1) = 0.00739156869269664

	        points(2) = 0

	        points(3) = -0.0420233044773113

	        points(4) = 0.0350529989729012

	        points(5) = 0

	        points(6) = 0.0278754181857153

	        points(7) = -0.0165377796333246

	        points(8) = 0

	        points(9) = 0.0403878396197683

	        points(10) = 0.0406222157061507

	        points(11) = 0

	        pointArray = points

	        skSegment = Part.SketchManager.CreateSpline((pointArray))

	        Part.InsertSplinePoint(0.0382447809668287,
	0.00781095184375528, 0)

	        Part.SketchManager.InsertSketch(True)

	    End Sub

	    Public swApp As SldWorks

	End Class
```

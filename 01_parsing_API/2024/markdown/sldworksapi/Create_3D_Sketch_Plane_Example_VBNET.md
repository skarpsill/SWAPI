---
title: "Create 3D Sketch Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Sketch_Plane_Example_VBNET.htm"
---

# Create 3D Sketch Plane Example (VB.NET)

This example shows how to create a 3D sketch plane.

```
'------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Inserts a 3D sketch of two lines.
' 2. Inserts a 2D sketch of a circle.
' 3. Selects a line in the 3D sketch and the center of the circle
'    in the 2D sketch.
' 4. Inserts a 3D sketch plane.
' 5. Examine the graphics area and the FeatureManager design tree.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swSketch As Sketch
        Dim status As Boolean

        'Open new part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

        'Insert 3D sketch of two lines
        swSketchManager = swModel.SketchManager
        swSketchManager.Insert3DSketch(True)
        swSketchSegment = swSketchManager.CreateCenterLine(-0.082642, 0.005659, 0.0#, -0.049926, 0.045073, 0.0#)
        swSketch = swSketchManager.ActiveSketch
        status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0)
        swSketchSegment = swSketchManager.CreateCenterLine(-0.049926, 0.045073, 0.0#, -0.049926, -0.022634, -0.065874)
        swSketch = swSketchManager.ActiveSketch
        status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Insert 2D sketch of a circle
        swModel.ActivateSelectedFeature()
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateCircle(-0.056401, 0.005985, 0.0#, -0.054697, -0.005141, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Insert a 3D sketch plane
        swSketchManager.Insert3DSketch(True)
        status = swModelDocExt.SelectByID2("Line1@3DSketch1", "EXTSKETCHSEGMENT", -0.0565609614209999, 0.0370796232466087, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", -0.0564010297276809, 0.00598490302365917, 0, True, 0, Nothing, 0)
        status = swSketchManager.CreateSketchPlane(9, 9, 0)
        status = swModelDocExt.SelectByID2("Plane1", "SKETCHSURFACES", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ActivateSelectedFeature()
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Create Surface-sweep Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Surface-sweep_Feature_Example_VBNET.htm"
---

# Create Surface-sweep Feature Example (VB.NET)

This example shows how to create a surface-sweep feature.

```
'---------------------------------------------------
' Preconditions: Verify that the part template exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates two sketches.
' 3. Inserts a surface-sweep feature.
' 4. Examine the FeatureManager design tree and
'    graphics area.
'---------------------------------------------------
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
        Dim swFeature As Feature
        Dim swFeatureManager As FeatureManager
        Dim status As Boolean

        'Open new part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Create a sketch
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchSegment = swSketchManager.CreateLine(0.0#, 0.0#, 0.0#, 0.068491, 0.049604, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.068491, 0.049604, 0.0#, 0.10923, 0.112837, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.10923, 0.112837, 0.0#, 0.194652, 0.154023, 0.0#)
        swSketchManager.InsertSketch(True)

        swModel.ViewZoomtofit2()
        swModel.ShowNamedView2("*Isometric", 7)
        swModel.ClearSelection2(True)

        'Create another sketch
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateLine(-0.0#, 0.0#, 0.0#, 0.021042, 0.091756, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.021042, 0.091756, 0.0#, 0.098366, 0.085093, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.098366, 0.085093, 0.0#, 0.143062, 0.122696, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Insert surface sweep
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.InsertSweepSurface3(False, 0, False, False, 0, 0, 0, True, True, 0, True, False, 0, 0)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

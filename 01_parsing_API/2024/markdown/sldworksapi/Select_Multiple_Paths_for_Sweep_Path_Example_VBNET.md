---
title: "Select Multiple Sketch Segments for Sweep Path Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Paths_for_Sweep_Path_Example_VBNET.htm"
---

# Select Multiple Sketch Segments for Sweep Path Example (VB.NET)

This example shows how to select multiple sketch segments for the path for a sweep feature.

```
'--------------------------------------------------------
' Preconditions: Verify that the part template exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates:
'    * sketch of a circle.
'    * sketch of a line.
'    * another sketch of a line.
' 3. Selects the sketch of the circle for the sweep profile.
' 4. Selects the sketches of the lines for the sweep path
'    and groups them as an object.
' 5. Creates a sweep feature.
' 6. Examine the FeatureManager design tree and graphics
'    area.
'---------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchManager = swModel.SketchManager
        swFeatureManager = swModel.FeatureManager

        'Create sketch of circle for the sweep profile
        swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.002394, -0.006333, 0.0#)
        swSketchManager.InsertSketch(True)

        'Create sketches of lines for the sweep path
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateLine(-0.0#, 0.0#, 0.0#, 0.088481, 0.035691, 0.0#)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateLine(0.088481, 0.035691, 0.0#, 0.079214, 0.076295, 0.0#)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Select the sketch of the circle for the sweep profile
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -0.00586834883582351, -0.00337646707201764, 0, False, 1, Nothing, 0)

        'Select the sketches of the lines for the sweep path and group them as an object
        status = swModelDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 0.0379259971310087, 0.0152983890733924, 0, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1@Sketch3", "EXTSKETCHSEGMENT", 0.0848435978763939, 0.0516285284155501, 0, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("Unknown", "SELOBJGROUP", 0, 0, 0, True, 4, Nothing, 0)

        'Create the sweep feature
        swFeature = swFeatureManager.InsertProtrusionSwept4(False, False, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, True, True, 0, True, False, 0, 0)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

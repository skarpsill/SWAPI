---
title: "Select Multiple Sketch Segments for Sweep Path Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Paths_for_Sweep_Path_Example_VB.htm"
---

# Select Multiple Sketch Segments for Sweep Path Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    Set swSketchManager = swModel.SketchManager
    Set swFeatureManager = swModel.FeatureManager
```

```
    'Create sketch of circle for the sweep profile
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.002394, -0.006333, 0#)
    swSketchManager.InsertSketch True
```

```
    'Create sketches of lines for the sweep path
    status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateLine(-0#, 0#, 0#, 0.088481, 0.035691, 0#)
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateLine(0.088481, 0.035691, 0#, 0.079214, 0.076295, 0#)
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True

    'Select the sketch of the circle for the sweep profile
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -5.86834883582351E-03, -3.37646707201764E-03, 0, False, 1, Nothing, 0)
```

```
    'Select the sketches of the lines for the sweep path and group them as an object
    status = swModelDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 3.79259971310087E-02, 1.52983890733924E-02, 0, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1@Sketch3", "EXTSKETCHSEGMENT", 8.48435978763939E-02, 5.16285284155501E-02, 0, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("Unknown", "SELOBJGROUP", 0, 0, 0, True, 4, Nothing, 0)
```

```
    'Create the sweep feature
    Set swFeature = swFeatureManager.InsertProtrusionSwept4(False, False, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, True, True, 0, True, False, 0, 0)
```

```
End Sub
```

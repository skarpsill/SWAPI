---
title: "Create 3D Sketch Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Sketch_Plane_Example_VB.htm"
---

# Create 3D Sketch Plane Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketch As SldWorks.Sketch
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    'Insert 3D sketch of two lines
    Set swSketchManager = swModel.SketchManager
    swSketchManager.Insert3DSketch True
    Set swSketchSegment = swSketchManager.CreateCenterLine(-0.082642, 0.005659, 0#, -0.049926, 0.045073, 0#)
    Set swSketch = swSketchManager.ActiveSketch
    status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0)
    Set swSketchSegment = swSketchManager.CreateCenterLine(-0.049926, 0.045073, 0#, -0.049926, -0.022634, -0.065874)
    Set swSketch = swSketchManager.ActiveSketch
    status = swSketch.SetWorkingPlaneOrientation(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Insert 2D sketch of a circle
    swModel.ActivateSelectedFeature
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchManager.CreateCircle(-0.056401, 0.005985, 0#, -0.054697, -0.005141, 0#)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    'Insert a 3D sketch plane
    swSketchManager.Insert3DSketch True
    status = swModelDocExt.SelectByID2("Line1@3DSketch1", "EXTSKETCHSEGMENT", -5.65609614209999E-02, 3.70796232466087E-02, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", -5.64010297276809E-02, 5.98490302365917E-03, 0, True, 0, Nothing, 0)
    status = swSketchManager.CreateSketchPlane(9, 9, 0)
    status = swModelDocExt.SelectByID2("Plane1", "SKETCHSURFACES", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ActivateSelectedFeature
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
End Sub
```

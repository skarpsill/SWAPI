---
title: "Insert Swept-surface Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Swept-surface_Feature_Example_VB.htm"
---

# Insert Swept-surface Feature Example (VBA)

This example shows how to create a swept-surface feature.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the part template exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates two sketches.
' 3. Inserts a swept-surface feature.
' 4. Examine the FeatureManager design tree and
'    graphics area.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swPathFeat As SldWorks.Feature
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSweep As SldWorks.SweepFeatureData
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
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    'Create a sketch
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0#, 0#, 0.068491, 0.049604, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.068491, 0.049604, 0#, 0.10923, 0.112837, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.10923, 0.112837, 0#, 0.194652, 0.154023, 0#)
    swSketchManager.InsertSketch True
```

```
    swModel.ViewZoomtofit2
    swModel.ShowNamedView2 "*Isometric", 7
    swModel.ClearSelection2 True
```

```
    'Create another sketch
    status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateLine(-0#, 0#, 0#, 0.021042, 0.091756, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.021042, 0.091756, 0#, 0.098366, 0.085093, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.098366, 0.085093, 0#, 0.143062, 0.122696, 0#)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Insert surface sweep
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
```

```vb
    Set swFeatureMgr = swModel.FeatureManager
    Set swSweep = swFeatureMgr.CreateDefinition(swFmRefSurface)
    swSweep.TangentPropagation = False
     swSweep.TwistControlType = 0
     swSweep.MaintainTangency = False
     swSweep.AdvancedSmoothing = False
     swSweep.StartTangencyType = 0
     swSweep.EndTangencyType = 0
     swSweep.PathAlignmentType = 0
     swSweep.FeatureScope = True
     swSweep.AutoSelect = True
     swSweep.SetTwistAngle 0#
     swSweep.MergeSmoothFaces = True
     swSweep.CircularProfile = False
     swSweep.CircularProfileDiameter = 0#
     swSweep.Direction = 0

    Set swPathFeat = swFeatureMgr.CreateFeature(swSweep)
```

```
End Sub
```

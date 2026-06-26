---
title: "Select Multiple Splines for Loft Guide Curves Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VB.htm"
---

# Select Multiple Splines for Loft Guide Curves Example (VBA)

This example shows how to select multiple splines for the guide curves for a loft feature.

```
'---------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates a new part.
' 2. Creates a profile sketch.
' 3. Creates a reference plane and another profile sketch on that
'    reference plane.
' 4. Creates two splines for the guide curves.
' 5. Selects the profile sketches.
' 6. Selects the splines and groups them as an object.
' 7. Creates a loft feature.
' 8. Examine the FeatureManager design tree and graphics area.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swRefPlane As SldWorks.RefPlane
Dim swFeatureManager As SldWorks.FeatureManager
Dim status As Boolean
```

```
Sub main()
    Set swApp = Application.SldWorks
```

```
    'Create a new part
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
```

```
    'Create a profile sketch
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 7.06113079019074E-02, 0, 0, 0, 3.74944141689373E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Create a reference plane and another profile sketch
    'on that reference plane
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swRefPlane = swFeatureManager.InsertRefPlane(8, 0.07, 0, 0, 0, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 5.27205722070845E-02, 0, 0, 0, 1.54164850136235E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Create a spline
    status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Dim pointArray As Variant
    Dim points() As Double
    ReDim points(0 To 14) As Double
    points(0) = -0.07
    points(1) = 1.54164850136235E-02
    points(2) = 0
    points(3) = -5.31092941649547E-02
    points(4) = 2.80386111480766E-02
    points(5) = 0
    points(6) = -2.96934467839947E-02
    points(7) = 2.29795168190776E-02
    points(8) = 0
    points(9) = -1.12921067380967E-02
    points(10) = 0.026354325474415
    points(11) = 0
    points(12) = 0
    points(13) = 3.74944141689373E-02
    points(14) = 0
    pointArray = points
    Set swSketchSegment = swSketchManager.CreateSpline((pointArray))
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    'Create another spline
    status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    ReDim points(0 To 8) As Double
    points(0) = -0.07
    points(1) = -1.54164850136235E-02
    points(2) = 0
    points(3) = -3.07689275649068E-02
    points(4) = -2.33694015292372E-02
    points(5) = 0
    points(6) = 0
    points(7) = -3.74944141689373E-02
    points(8) = 0
    pointArray = points
    Set swSketchSegment = swSketchManager.CreateSpline((pointArray))
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    'Select the profile sketches
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -5.85496337278505E-02, 2.09585732143712E-02, 1, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -3.79093739088495E-02, 1.07136192740755E-02, 1, True, 0, Nothing, 0)

    'Select the splines for the guide curves
    status = swModelDocExt.SelectByID2("Spline1@Sketch3", "EXTSKETCHSEGMENT", -6.20659823337474E-03, 3.04187689522769E-02, 2, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Spline1@Sketch4", "EXTSKETCHSEGMENT", -4.02947949143199E-02, -2.06106896601265E-02, 2, True, 0, Nothing, 0)
    'Group the selected splines as an object
    status = swModelDocExt.SelectByID2("Unknown", "SELOBJGROUP", 0, 0, 0, True, 2, Nothing, 0)

    'Create a loft
    swFeatureManager.InsertProtrusionBlend2 False, True, False, 1, 0, 0, 1, 1, True, True, False, 0, 0, 0, True, True, True, 0
```

```
End Sub
```

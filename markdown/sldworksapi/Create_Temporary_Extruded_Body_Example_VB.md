---
title: "Create Temporary Extruded Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Extruded_Body_Example_VB.htm"
---

# Create Temporary Extruded Body Example (VBA)

This example shows how to create a temporary extruded body.

```
'------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
'
' Postconditions.
' 1. Opens a new part document.
' 2. Creates and selects a sheet (also called a surface) body.
' 3. Creates a temporary extruded body.
' 4. Examine the graphics area.
'------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSketchManager As SldWorks.SketchManager
Dim swSelectionManager As SldWorks.SelectionMgr
Dim sketchSegment As SldWorks.sketchSegment
Dim swModeler As SldWorks.Modeler
Dim swMath As SldWorks.MathUtility
Dim profileBody As SldWorks.Body2
Dim extrudedBody As SldWorks.Body2
Dim dirVector As SldWorks.MathVector
Dim planeSurf As SldWorks.Surface
Dim trimCurves(3) As SldWorks.Curve
Dim points(11) As Double
Dim pointArray As Variant
Dim halfWidth As Double
Dim halfLength As Double
Dim startArr(2) As Double
Dim endArr(2) As Double
Dim ptArr(2) As Double
Dim dirArr(2) As Double
Dim slotWidth As Double
Dim slotLength As Double
Dim slotDepth As Double
Dim slotThruAll As Boolean
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler
    Set swMath = swApp.GetMathUtility
```

```
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swSketchManager = swModel.SketchManager
    Set swModelDocExt = swModel.Extension
    Set swSelectionManager = swModel.SelectionManager
```

```
    'Create and select extruded surface body
    points(0) = -7.20746414289124E-02
    points(1) = -2.83600245263074E-02
    points(2) = 0
    points(3) = -0.0514715593755
    points(4) = -3.45025084396866E-03
    points(5) = 0
    points(6) = 0
    points(7) = 0
    points(8) = 0
    points(9) = 8.72558597840225E-02
    points(10) = 5.21037067517796E-02
    points(11) = 0
    pointArray = points
    Set sketchSegment = swSketchManager.CreateSpline((pointArray))
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    swFeatureManager.FeatureExtruRefSurface2 True, False, False, 0, 0, 0.0508, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, False, False, False
    swSelectionManager.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
```

```
    slotDepth = 0.01
    slotWidth = 0.04
    slotLength = 0.09
    slotThruAll = False
```

```
    halfWidth = slotWidth / 2
    halfLength = slotLength / 2
```

```
    ptArr(0) = 0#
    ptArr(1) = 0#
    ptArr(2) = 0#
    dirArr(0) = 0#
    dirArr(1) = 0#
    dirArr(2) = 1#
    startArr(0) = 1#
    startArr(1) = 0#
    startArr(2) = 0#
    Set planeSurf = swModeler.CreatePlanarSurface2((ptArr), (dirArr), (startArr))
```

```
    ptArr(0) = -halfLength
    ptArr(1) = halfWidth
    ptArr(2) = 0#
    dirArr(0) = 1#
    dirArr(1) = 0#
    dirArr(2) = 0#
    Set trimCurves(0) = swModeler.CreateLine((ptArr), (dirArr))
    Set trimCurves(0) = trimCurves(0).CreateTrimmedCurve2(-halfLength, halfWidth, 0#, halfLength, halfWidth, 0#)
```

```
    ptArr(0) = halfLength
    ptArr(1) = 0#
    ptArr(2) = 0#
    startArr(0) = halfLength
    startArr(1) = halfWidth
    startArr(2) = 0#
    endArr(0) = halfLength
    endArr(1) = -halfWidth
    endArr(2) = 0#
    dirArr(0) = 0#
    dirArr(1) = 0#
    dirArr(2) = -1#
    Set trimCurves(1) = swModeler.CreateArc((ptArr), (dirArr), halfWidth, (startArr), (endArr))
    Set trimCurves(1) = trimCurves(1).CreateTrimmedCurve2(halfLength, halfWidth, 0#, halfLength, -halfWidth, 0#)
```

```
    ptArr(0) = halfLength
    ptArr(1) = -halfWidth
    ptArr(2) = 0#
    dirArr(0) = -1#
    dirArr(1) = 0#
    dirArr(2) = 0#
    Set trimCurves(2) = swModeler.CreateLine((ptArr), (dirArr))
    Set trimCurves(2) = trimCurves(2).CreateTrimmedCurve2(halfLength, -halfWidth, 0#, -halfLength, -halfWidth, 0#)
```

```
    ptArr(0) = -halfLength
    ptArr(1) = 0#
    ptArr(2) = 0#
    startArr(0) = -halfLength
    startArr(1) = -halfWidth
    startArr(2) = 0#
    endArr(0) = -halfLength
    endArr(1) = halfWidth
    endArr(2) = 0#
    dirArr(0) = 0#
    dirArr(1) = 0#
    dirArr(2) = -1#
    Set trimCurves(3) = swModeler.CreateArc((ptArr), (dirArr), halfWidth, (startArr), (endArr))
    Set trimCurves(3) = trimCurves(3).CreateTrimmedCurve2(-halfLength, -halfWidth, 0#, -halfLength, halfWidth, 0#)
```

```
    Set profileBody = planeSurf.CreateTrimmedSheet((trimCurves))
```

```
    dirArr(0) = 0#
    dirArr(1) = 0#
    dirArr(2) = -1#
    Set dirVector = swMath.CreateVector((dirArr))
    Set extrudedBody = swModeler.CreateExtrudedBody(profileBody, dirVector, slotDepth)
    extrudedBody.Display3 swModel, RGB(1, 0, 0), swTempBodySelectOptions_e.swTempBodySelectOptionNone
```

```
End Sub
```

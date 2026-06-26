---
title: "Create Curvature Continuous Variable Fillet Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VB.htm"
---

# Create Curvature Continuous Variable Fillet Feature Example (VBA)

This example shows how to create a curvature continuous variable fillet feature.

```
'-------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a part with a variable fillet feature with curvature continuous.
' 2. Gets whether the variable fillet feature has curvature continuous set.
' 3. Examine the graphics area and the Immediate window.
'-------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swVariableFilletFeatureData As SldWorks.VariableFilletFeatureData2
Dim status As Boolean
Dim radiiArray2 As Variant
Dim radiis2() As Double
Dim dist2Array2 As Variant
Dim dists22() As Double
Dim conicRhosArray2 As Variant
Dim coniRhos2() As Double
Dim setBackArray2 As Variant
Dim setBacks2 As Double
Dim pointArray2 As Variant
Dim points2 As Double
Dim pointDist2Array2 As Variant
Dim pointsDist22 As Double
Dim pointRhoArray2 As Variant
Dim pointsRhos2 As Double
Dim filletOptions As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    Set swSketchManager = swModel.SketchManager
    Set swFeatureManager = swModel.FeatureManager
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Create part with variable feature fillet with curvature continuous
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchManager.CreateLine(-0.070405, 0.03105, 0#, -0.070405, -0.033217, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.070405, -0.033217, 0#, 0.01733, -0.033217, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.01733, -0.033217, 0#, 0.01733, -0.016247, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.01733, -0.016247, 0#, -0.026537, -0.009748, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.026537, -0.009748, 0#, -0.04116, 0.024552, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.04116, 0.024552, 0#, -0.070405, 0.03105, 0#)
    swModel.ShowNamedView2 "*Trimetric", 8
    swModel.ClearSelection2 True
    Set swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.04064, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    swSelectionMgr.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 2.43713283917941E-02, 0.023466279649881, True, 1, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 2.43713283917941E-02, 0.023466279649881, False, 1, Nothing, 0)
```

```
    ReDim radiis2(0 To 1) As Double
    radiis2(0) = 0.00508
    radiis2(1) = 0.01778
```

```
    ReDim dists22(0 To 1) As Double
    ReDim coniRhos2(0 To 1) As Double
    radiiArray2 = radiis2
    dist2Array2 = dists22
    conicRhosArray2 = coniRhos2
    setBackArray2 = setBacks2
    pointArray2 = points2
    pointDist2Array2 = pointsDist22
    pointRhoArray2 = pointsRhos2

    filletOptions = swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous + swFeatureFilletOptions_e.swFeatureFilletKeepFeatures + swFeatureFilletOptions_e.swFeatureFilletPropagateFeatToParts
    Set swFeature = swFeatureManager.FeatureFillet3(filletOptions, 0.00254, 0.0000001, 0, 1, 0, 0, (radiiArray2), (dist2Array2), (conicRhosArray2), (setBackArray2), (pointArray2), (pointDist2Array2), (pointRhoArray2))
```

```
    'Verify variable fillet feature has curvature continuous set
    Set swVariableFilletFeatureData = swFeature.GetDefinition
    status = swVariableFilletFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print "Variable fillet feature has curvature continuous set: " & swVariableFilletFeatureData.CurvatureContinuous
    swVariableFilletFeatureData.ReleaseSelectionAccess
```

```
End Sub
```

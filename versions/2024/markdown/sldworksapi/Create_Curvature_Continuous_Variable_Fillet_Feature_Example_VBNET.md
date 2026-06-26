---
title: "Create Curvature Continuous Variable Fillet Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VBNET.htm"
---

# Create Curvature Continuous Variable Fillet Feature Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swFeatureManager As FeatureManager
        Dim swSelectionMgr As SelectionMgr
        Dim swVariableFilletFeatureData As VariableFilletFeatureData2
        Dim status As Boolean
        Dim radiiArray2 As Object
        Dim radiis2() As Double
        Dim dist2Array2 As Object
        Dim dists22() As Double
        Dim conicRhosArray2 As Object
        Dim coniRhos2() As Double
        Dim setBackArray2 As Object
        Dim setBacks2 As Double
        Dim pointArray2 As Object
        Dim points2 As Double
        Dim pointDist2Array2 As Object
        Dim pointsDist22 As Double
        Dim pointRhoArray2 As Object
        Dim pointsRhos2 As Double
        Dim filletOptions As Integer

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchManager = swModel.SketchManager
        swFeatureManager = swModel.FeatureManager
        swSelectionMgr = swModel.SelectionManager

        'Create part with variable feature fillet with curvature continuous
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateLine(-0.070405, 0.03105, 0.0#, -0.070405, -0.033217, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.070405, -0.033217, 0.0#, 0.01733, -0.033217, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.01733, -0.033217, 0.0#, 0.01733, -0.016247, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.01733, -0.016247, 0.0#, -0.026537, -0.009748, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.026537, -0.009748, 0.0#, -0.04116, 0.024552, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.04116, 0.024552, 0.0#, -0.070405, 0.03105, 0.0#)
        swModel.ShowNamedView2("*Trimetric", 8)
        swModel.ClearSelection2(True)
        swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.04064, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionMgr.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 0.0243713283917941, 0.023466279649881, True, 1, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "EDGE", -0.040927911364804, 0.0243713283917941, 0.023466279649881, False, 1, Nothing, 0)
        ReDim radiis2(1)
        radiis2(0) = 0.00508
        radiis2(1) = 0.01778
        ReDim dists22(1)
        ReDim coniRhos2(1)
        radiiArray2 = radiis2
        dist2Array2 = dists22
        conicRhosArray2 = coniRhos2
        setBackArray2 = setBacks2
        pointArray2 = points2
        pointDist2Array2 = pointsDist22
        pointRhoArray2 = pointsRhos2

        filletOptions = swFeatureFilletOptions_e.swFeatureFilletCurvatureContinuous + swFeatureFilletOptions_e.swFeatureFilletKeepFeatures + swFeatureFilletOptions_e.swFeatureFilletPropagateFeatToParts
        swFeature = swFeatureManager.FeatureFillet3(filletOptions, 0.00254, 0.0000001, 0, 1, 0, 0, (radiiArray2), (dist2Array2), (conicRhosArray2), (setBackArray2), (pointArray2), (pointDist2Array2), (pointRhoArray2))

        'Verify variable fillet feature has curvature continuous set
        swVariableFilletFeatureData = swFeature.GetDefinition
        status = swVariableFilletFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Variable fillet feature has curvature continuous set: " & swVariableFilletFeatureData.CurvatureContinuous)
        swVariableFilletFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Insert Fill-surface Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Fill-surface_Feature_Example_VB.htm"
---

# Insert Fill-surface Feature Example (VBA)

This example shows how to insert a fill-surface feature.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sketches a circle on the Front Plane.
' 2. Offsets the Front Plane to create Plane1.
' 3. Sketches a circle on Plane1.
' 4. Creates a thin-feature loft using the circles
'    created in steps 1 and 3.
' 5. Selects one of the sketches to use for
'    the fill-surface feature.
' 6. Creates a fill-surface feature named Surface-Fill1.
' 7. Gets, sets, and prints some properties of the fill-surface feature
'    to the Immediate window.
' 8. Examine the FeatureManager design, graphics area, and the
'    the Immediate window.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatMgr As SldWorks.FeatureManager
Dim swRefPlane As SldWorks.RefPlane
Dim swFeat As SldWorks.Feature
Dim swFillSurfaceFeatureData as SldWorks.FillSurfaceFeatureData
Dim selObj As Object
Dim status As Boolean
Dim nbrPatchEntities As Long
Dim patchEntities As Variant
Dim entTypes As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open a new model document
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", swDwgPaperAsize, 0, 0)
```

```
    'Select the front plane and sketch a circle
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    swModel.ClearSelection2 True
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.018863, -0.048015, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Offset the front plane to create Plane1
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatMgr = swModel.FeatureManager
    Set swRefPlane = swFeatMgr.InsertRefPlane(8, 0.0762, 0, 0, 0, 0)
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swSketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.005144, -0.017148, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Create a loft as a thin feature
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -1.20997659765269E-02, 1.31954647737917E-02, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -1.37458916138411E-02, 4.97220981864567E-02, 0, True, 1, Nothing, 0)
    swFeatMgr.InsertProtrusionBlend2 False, True, False, 1, 0, 0, 1, 1, True, True, True, 0.000254, 0.000254, 0, True, True, True, swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge
```

```
    'Get the sketch for the fill-surface feature
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -3.09259362651374E-02, -1.50632202505945E-02, 2.65529245975468E-02, True, 257, Nothing, swSelectOptionDefault)
    Set swSelMgr = swModel.SelectionManager
    Set selObj = swSelMgr.GetSelectedObject6(1, 257)
```

```
    'Insert the fill-surface feature
    Set swFeat = swFeatMgr.InsertFillSurface2(2, swOptimizeSurface, selObj, swContact, Nothing, Nothing)
```

```
    'Access the fill-surface feature
    Set swFillSurfaceFeatureData = swFeat.GetDefinition
    status = swFillSurfaceFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print "Fill-surface feature: "
    Debug.Print "  Number of constraint curves: " & swFillSurfaceFeatureData.GetConstraintCurvesCount
    nbrPatchEntities = swFillSurfaceFeatureData.GetPatchBoundaryCount
    Debug.Print "  Number of entities used to define the patch boundary: " & nbrPatchEntities
    If nbrPatchEntities > 0 Then
        'Get the type of patch boundary entities
        patchEntities = swFillSurfaceFeatureData.GetPatchBoundary(entTypes)
        For i = 0 To nbrPatchEntities - 1
            Debug.Print ("  Type of entity for patch boundary " & (i + 1) & " (1 = edge; 9 = sketch) : " & entTypes(i))
        Next i
        Debug.Print "  Results merged? " & swFillSurfaceFeatureData.Merge
        swFillSurfaceFeatureData.OptimizeSurface = False
        Debug.Print "  Patch optimized? " & swFillSurfaceFeatureData.OptimizeSurface
        Debug.Print "  Original resolution control: " & swFillSurfaceFeatureData.ResolutionControl
        If swFillSurfaceFeatureData.OptimizeSurface = False Then
            swFillSurfaceFeatureData.ResolutionControl = 1
        End If
        Debug.Print "  Updated resolution control (valid values 1, 2 and 3; setting this value only valid if patch is not optimized): " & swFillSurfaceFeatureData.ResolutionControl
    End If
    status = swFeat.ModifyDefinition(swFillSurfaceFeatureData, swModel, Nothing)
```

```
End Sub
```

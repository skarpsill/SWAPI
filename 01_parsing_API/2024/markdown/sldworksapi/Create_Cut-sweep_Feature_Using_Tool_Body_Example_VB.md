---
title: "Create Cut-sweep Feature Using Tool Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Tool_Body_Example_VB.htm"
---

# Create Cut-sweep Feature Using Tool Body Example (VBA)

This example shows how to create a cut-sweep feature using a tool body.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a boss-extrude feature.
' 2. Creates a sketch.
' 3. Creates a revolve feature.
' 4. Selects the revolve feature, sketch, and extrude feature and
'    creates a cut-sweep feature.
' 5. Accesses the cut-sweep feature.
' 6. Gets the names of the cut-sweep feature's tool body and path.
' 7. Releases access of the cut-sweep feature.
' 8. Examine the Immediate window, FeatureManager design tree,
'    and graphics area.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swSweepFeatureData As SldWorks.SweepFeatureData
Dim swProfileObj As Object
Dim swProfileBody As SldWorks.Body2
Dim swPathFeature As SldWorks.Feature
Dim sketchLines As Variant
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    'Create extrude feature
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.000361, 0.001416, 0#, 0.024462, -0.045092, 0#)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.FeatureExtrusion3(True, False, True, 0, 0, 0.09, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
```

```
    'Create sketch
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    swSelectionMgr.EnableContourSelection = False
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.000019, 0.00051, 0#, 0.026716, -0.0401, 0#)
    swSketchMgr.InsertSketch True
```

```
    swModel.ClearSelection2 True
```

```
    'Create revolve feature
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    sketchLines = swSketchMgr.CreateCornerRectangle(-2.66210577384013E-02, -2.48555003438298E-02, 0, -3.78465609175683E-02, -4.75106067599669E-02, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", -2.64169576805983E-02, -4.49999999999998E-02, 2.93457016154969E-02, False, 16, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureRevolve2(True, True, False, False, False, False, 0, 0, 6.2831853071796, 0, False, False, 0.01, 0.01, 0, 0, 0, False, True, True)
    swSelectionMgr.EnableContourSelection = False
```

```
    swModel.ClearSelection2 True
```

```
    'Create cut-sweep feature
    status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 2048, Nothing, 0)
    Set swFeature = swFeatureMgr.InsertCutSwept5(False, True, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, False, 0, True, True, True, False, False, 0, 0)
    Debug.Print "Feature name = " & swFeature.Name
    Set swSweepFeatureData = swFeature.GetDefinition
```

```
    ' Roll back to access selections
    status = swSweepFeatureData.AccessSelections(swModel, Nothing)
```

```
    Set swProfileObj = swSweepFeatureData.Profile
    Set swProfileBody = swProfileObj
    Debug.Print "  Tool body = " & swProfileBody.Name
```

```
    Set swPathFeature = swSweepFeatureData.Path
    Debug.Print "  Path = " & swPathFeature.Name
```

```
    ' Roll forward
    swSweepFeatureData.ReleaseSelectionAccess

End Sub
```

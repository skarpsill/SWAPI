---
title: "Create Extrude Feature Using Sketch Contours Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm"
---

# Create Extrude Feature Using Sketch Contours Example (VBA)

This example shows how to create an extrude feature using sketch contours.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a sketch containing sketch contours.
' 3. Creates a boss extrude feature using the sketch of sketch
'    contours.
' 4. Selects the boss extrude feature and accesses
'    its data.
' 5. Gets the sketch contours.
' 6. Get whether each sketch contour is open or closed.
' 7. Examine the FeatureManager design tree, graphics area, and
'    the Immediate window.
'--------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swExtrudeFeatureData As SldWorks.ExtrudeFeatureData2
Dim status As Boolean
Dim skcontours As Variant
Dim skcontour As SldWorks.SketchContour
Dim nbrContours As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExtension = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeatureMgr = swModel.FeatureManager
```

```
    'Create sketch containing sketch contours
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.010564, -0.041843, 0#)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchMgr.CreateCircle(0.043155, 0#, 0#, 0.048428, -0.01221, 0#)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.043155, 0#, 0#, -0.043214, -0.014954, 0#)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Create boss extrude feature from sketch of sketch contours
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.047096875714166, 7.24922083273226E-03, 0.018531938896921, True, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", 4.73122625955432E-02, -0.015948285832011, -1.55264330079864E-02, True, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -8.80361157802517E-03, -2.46473508312897E-02, 1.99951653548178E-02, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    swSelectionMgr.EnableContourSelection = True
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.047096875714166, 7.24922083273226E-03, 0.018531938896921, True, 4, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", 4.73122625955432E-02, -0.015948285832011, -1.55264330079864E-02, True, 4, Nothing, 0)
    status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -8.80361157802517E-03, -2.46473508312897E-02, 1.99951653548178E-02, True, 4, Nothing, 0)
    Set swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01016, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    swSelectionMgr.EnableContourSelection = False
```

```
    'Select the boss extrude feature
    status = swModelDocExtension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swExtrudeFeatureData = swFeature.GetDefinition
```

```
    'Access the boss extrude feature data
    swExtrudeFeatureData.AccessSelections swModel, Nothing
```

```
    'Get the number of sketch contours in the extrude feature
    nbrContours = swExtrudeFeatureData.GetContoursCount
    Debug.Print "Number of sketch contours in the extrude feature: " & nbrContours
```

```
    'Get the sketch contours in the extrude feature
    skcontours = swExtrudeFeatureData.contours
```

```
    'Get each sketch contour and whether it is open or closed
    For i = 0 To (nbrContours - 1)
            Set skcontour = skcontours(i)
            Debug.Print "  Sketch contour " & i & " is closed? " & skcontour.IsClosed
    Next i
```

```
    'Release selection access
    swExtrudeFeatureData.ReleaseSelectionAccess
```

```
End Sub
```

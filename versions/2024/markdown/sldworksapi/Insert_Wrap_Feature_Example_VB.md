---
title: "Insert Wrap Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Wrap_Feature_Example_VB.htm"
---

# Insert Wrap Feature Example (VBA)

This example shows how to insert a wrap feature.

```
'-----------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\cylinder20.sldprt.
'
' Postconditions:
' 1. Selects the Front plane and creates a sketch of a circle.
' 2. Selects the sketch and nonplanar face.
' 3. Inserts a wrap feature on the selected nonplanar face.
' 4. Examine the graphics area and FeataureManager design
'    tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
Dim swFeatMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSketchManager = swModel.SketchManager
```

```
    'Create sketch for wrap feature
    swSketchManager.InsertSketch True
    boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSketchManager.CreateCircle(-0.006377, 0.026536, 0#, 0.004153, 0.006985, 0#)
    swSketchManager.InsertSketch True
```

```
    swModel.ClearSelection2 True
```

```
    ' Mark the sketch to use for wrap feature as 4
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 4, Nothing, swSelectOptionDefault)
```

```
    ' Mark the nonplanar face on which to place wrap feature as 1
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -2.01300616999447E-02, 2.48040612188447E-02, 5.80282618765864E-02, True, 1, Nothing, 0)
    Set swFeatMgr = swModel.FeatureManager
```

```
    ' Create a wrap feature of type emboss
    swFeatMgr.InsertWrapFeature 0, 0.005, False
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```

---
title: "Insert Cut Extrude Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_Extrude_Example_VB.htm"
---

# Insert Cut Extrude Example (VBA)

This example shows how to insert a cut extrude feature.

```
'-------------------------------------------------------------
' Preconditions: Verify that the specified file to open exists.
'
' Postconditions:
' 1. Inserts a cut extrude feature in the model.
' 2. Examine the graphics area.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim boolstatus As Boolean
Dim fileerror As Long, filewarning As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open document
    swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    ' Select the face where to sketch a circle
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02031412853728, 0.006977746007294, -0.008053400767039, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True

    ' Sketch a circle
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.01708, -0.030458, 0#)
    boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
```

```
    ' Create a cut-extrude feature using the circle
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureCut3(True, False, False, swEndCondThroughAll, swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True, False, False, False, swStartSketchPlane, 0, False)
```

```
End Sub
```

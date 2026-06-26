---
title: "Insert Thin Cut Extrude Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Thin_cut_Extrude_Example_VB.htm"
---

# Insert Thin Cut Extrude Example (VBA)

This example shows how to insert a thin cut extrude feature.

```
'------------------------------------------------------
' Preconditions: Verify that the specified part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a thin cut extrude feature in the part.
' 3. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'-----------------------------------------------------
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
Dim longstatus As Long, longwarnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open part
    swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\water.sldprt", 1, 0, "", longstatus, longwarnings
    Set swModel = swApp.ActiveDoc
```

```
    ' Select face on which to sketch a circle
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 1.655362220845E-04, -0.0477671348753, 0.072, False, 0, Nothing, 0)
    swModel.ShowNamedView2 "*Normal To", swBackView
    swModel.ClearSelection2 True
```

```
    ' Sketch a circle
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.030255, -0.042492, 0#)
    swModel.ClearSelection2 True
```

```
    ' Create the thin cut extrude
    boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureCutThin2(True, False, False, swEndCondBlind, swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, 0.01, 0.01, 0.01, 0, 0, False, 0.005, True, True, swStartSketchPlane, 0, False)
    swModel.ShowNamedView2 "*Isometric", swIsometricView
```

```
End Sub
```

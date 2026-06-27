---
title: "Rename Active Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Active_Sketch_Example_VB.htm"
---

# Rename Active Sketch Example (VBA)

This example shows how to rename the active sketch.

```
'------------------------------------------------
' Preconditions: Open the sketch that you want to rename.
'
' Postconditions:
' 1. Changes the name of the open sketch to MySketch.
' 2. Examine the FeatureManager design tree.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSketch As SldWorks.Sketch
    Dim swFeat As SldWorks.Feature
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Get the open sketch
    Set swSketch = swModel.GetActiveSketch2
    Set swFeat = swSketch
```

```
    ' Change the name of the open sketch to MySketch
    swFeat.Name = "MySketch"
```

```
End Sub
```

---
title: "Create 3D Spline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Spline_Example_VB.htm"
---

# Create 3D Spline Example (VBA)

This example shows how to create a 3D spline.

```
'----------------------------------------------
' Preconditions: Open a new part.
'
' Postconditions:
' 1. Creates a 3D sketch of a spline as per the
'    specified data points.
' 2. Examine the graphics area and FeatureManager
'    design tree.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim nPtData(11)             As Double
    Dim vPtData                 As Variant
    Dim swSketchSeg             As SldWorks.SketchSegment
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    nPtData(0) = -0.1163867779204: nPtData(1) = -0.01327060333761: nPtData(2) = 0#
    nPtData(3) = -0.08195494223363: nPtData(4) = 0.060973042362: nPtData(5) = 0.1
    nPtData(6) = -0.03568716302953: nPtData(7) = 0.01004261874198: nPtData(8) = 0.2
    nPtData(9) = 0.02779653401797: nPtData(10) = 0.04160513478819: nPtData(11) = 0.3
    vPtData = nPtData
    swModel.Insert3DSketch2 True
    Set swSketchSeg = swModel.CreateSpline(vPtData)
    Debug.Assert Not swSketchSeg Is Nothing
    swModel.Insert3DSketch2 True
```

```
End Sub
```

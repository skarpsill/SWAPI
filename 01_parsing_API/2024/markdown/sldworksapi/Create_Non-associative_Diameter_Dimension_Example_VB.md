---
title: "Create Non-associative Diameter Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Non-associative_Diameter_Dimension_Example_VB.htm"
---

# Create Non-associative Diameter Dimension Example (VBA)

This example shows how to create a non-associative diameter dimension.

```
'---------------------------------------
' Preconditions: Open a drawing.
'
' Postconditions:
' 1. Creates a non-associative diameter
'    dimension in the drawing.
' 2. Examine the drawing.
'---------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDispDim As SldWorks.DisplayDimension
    Dim nDimLoc(2) As Double
    Dim nCircPt1(2) As Double
    Dim nCircPt2(2) As Double
    Dim nPlaneNorm(2) As Double
    Dim nTextPt(2) As Double
    Dim vDimLoc As Variant
    Dim vCircPt1 As Variant
    Dim vCircPt2 As Variant
    Dim vPlaneNorm As Variant
    Dim vTextPt As Variant
    Dim nDimVal As Double
    Dim nTextHt As Double
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swDraw = swModel
```

```
    nDimLoc(0) = 0.1
    nDimLoc(1) = 0.1
    nDimLoc(2) = 0.1
    vDimLoc = nDimLoc
```

```
    nCircPt1(0) = 0.64
    nCircPt1(1) = 0.112
    nCircPt1(2) = 0#
    vCircPt1 = nCircPt1
```

```
    nCircPt2(0) = 0.125
    nCircPt2(1) = 0.14
    nCircPt2(2) = 0#
    vCircPt2 = nCircPt2
```

```
    nPlaneNorm(0) = 0#
    nPlaneNorm(1) = 0#
    nPlaneNorm(2) = 1#
    vPlaneNorm = nPlaneNorm
```

```
    nTextPt(2) = 0.2
    nTextPt(2) = 0.2
    nTextPt(2) = 0.2
    vTextPt = nTextPt
```

```
    nDimVal = 0.1255
    nTextHt = 0.01
```

```
    Set swDispDim = swDraw.CreateDiamDim4(vDimLoc, vCircPt1, vCircPt2, vPlaneNorm, vTextPt, nDimVal, nTextHt)
    swDispDim.Diametric = False
```

```
    swModel.GraphicsRedraw2
```

```
End Sub
```

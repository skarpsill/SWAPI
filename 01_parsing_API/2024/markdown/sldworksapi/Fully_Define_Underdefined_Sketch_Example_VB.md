---
title: "Fully Define Under Defined Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fully_Define_Underdefined_Sketch_Example_VB.htm"
---

# Fully Define Under Defined Sketch Example (VBA)

This example shows how to fully define an under defined sketch.

```
'---------------------------------------------------------------------------
' Preconditions: Open a part document containing an under defined sketch.
'
' Postconditions:
' 1. Fully defines the under defined sketch.
' 2. Open the sketch to verify.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeature As SldWorks.Feature
    Dim bValue As Boolean
    Dim swSketchManager As SldWorks.SketchManager
    Dim swModelExtension As SldWorks.ModelDocExtension
    Dim lStatus  As Long
    Dim lMarkHorizontal As Long
    Dim lMarkVertical As Long
    Dim swSelectionManager As SldWorks.SelectionMgr
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelExtension = swModel.Extension
    Set swSketchManager = swModel.SketchManager
    Set swSelectionManager = swModel.SelectionManager
```

```
    swModel.ClearSelection2 True
```

```
    ' These are the marks expected for the dimension datums
    lMarkHorizontal = 2
    lMarkVertical = 4
```

```
    Set swFeature = swModel.FirstFeature
    Do While (Not (swFeature Is Nothing))
        If (swFeature.GetTypeName = "ProfileFeature") Then
            Exit Do
        End If
        Set swFeature = swFeature.GetNextFeature
    Loop
```

```
    If (Not (swFeature Is Nothing)) Then
        bValue = swFeature.Select2(False, 0)
        swSketchManager.InsertSketch False
        ' OR together the marks for the vertical and horizontal datums;
        ' You cannot select the same point twice with different marks
        bValue = swModelExtension.SelectByID2("Point1@Origin", "EXTSKETCHPOINT", 0, 0, 0, False, lMarkHorizontal Or lMarkVertical, Nothing, 0)
        lStatus = swSketchManager.FullyDefineSketch(True, True, swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Vertical Or swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Horizontal, True, 1, Nothing, 1, Nothing, 1, 1)
        swSketchManager.InsertSketch True
    End If
```

```
End Sub
```

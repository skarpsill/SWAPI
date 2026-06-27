---
title: "Scale Hatch Pattern to Section View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Scale_Hatch_Pattern_With_Section_View_Example_VB.htm"
---

# Scale Hatch Pattern to Section View Example (VBA)

This example shows how to scale a hatch pattern to a section view.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Scales the hatch pattern to the section view.
' 2. Examine the Immediate window.
'
' NOTE: Because this drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swSectionView As SldWorks.DrSection

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
```

```
    swDrawing.ActivateView("Drawing View5")
    Set swView = swDrawing.ActiveDrawingView
    Set swSectionView = swView.GetSection
    swSectionView.ScaleHatchPattern = True
    Debug.Print "  Scale hatch pattern to section view? " & swSectionView.ScaleHatchPattern
```

```
End Sub
```

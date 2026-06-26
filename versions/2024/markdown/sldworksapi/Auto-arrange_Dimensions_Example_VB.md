---
title: "Auto-arrange Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Auto-arrange_Dimensions_Example_VB.htm"
---

# Auto-arrange Dimensions Example (VBA)

This example shows how to auto-arrange the selected dimensions.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Box-select the dimensions in Drawing View1.
'
' Postconditions:
' 1. Auto-arranges the selected dimensions.
' 2. Examine Drawing View1.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim status As Boolean
Dim errors As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swDrawingDoc = swModel
    status = swModelDocExt.AlignDimensions(swAlignDimensionType_e.swAlignDimensionType_AutoArrange, 0.001)
```

```
End Sub
```

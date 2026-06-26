---
title: "Align Drawing Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Drawing_Views_Example_VB.htm"
---

# Align Drawing Views Example (VBA)

This example shows how to align drawing views.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Horizontally aligns Drawing View6 with
'    the center of Drawing View3.
' 3. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swViewAlignWith As SldWorks.View
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim status As Boolean
Dim errors As Long, warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
        Set swApp = Application.SldWorks
```

```
        ' Open drawing
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
        Set swDrawingDoc = swModel
```

```
        ' Activate Sheet2
        status = swDrawingDoc.ActivateSheet("Sheet2")
        swModel.ClearSelection2 True
```

```
        ' Activate Drawing View6 and make it the active
        ' drawing view
        status = swDrawingDoc.ActivateView("Drawing View6")
        Set swView = swDrawingDoc.ActiveDrawingView
        Set swModelDocExtension = swModel.Extension
```

```
        ' Select Drawing View3 and select it to be
        ' the base view
        status = swModelDocExtension.SelectByID2("Drawing View3", "DRAWINGVIEW", 0.166130896593432, 0.265618781363279, 0, False, 0, Nothing, 0)
        Set swSelectionMgr = swModel.SelectionManager
        Set swViewAlignWith = swSelectionMgr.GetSelectedObject6(1, -1)
```

```
        ' Drawing View6 aligns horizontally
        ' with the center of Drawing View3
        status = swView.AlignWithView(swAlignViewHorizontalCenter, swViewAlignWith)
```

```
        Debug.Print ("Did the specified drawing views align? " & status)
```

```
End Sub
```

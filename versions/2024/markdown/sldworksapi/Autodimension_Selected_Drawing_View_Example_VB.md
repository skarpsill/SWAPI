---
title: "Autodimension Selected Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_Selected_Drawing_View_Example_VB.htm"
---

# Autodimension Selected Drawing View Example (VBA)

This example shows how to autodimension a selected drawing view.

```
'-----------------------------------------------------------------
' Preconditions: Verify that the specified drawing document to
' open exists.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Activates Drawing View1.
' 3. Selects a vertex.
' 4. Autodimensions the drawing view based on the
'    selected vertex.
' 5. Examine the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim status As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim selmark As Long
Dim ret as Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open drawing document of part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
    status = swDrawing.ActivateView("Drawing View1")
    Set swModelDocExt = swModel.Extension
    ' Select drawing view
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Horizontal and vertical datum, or a vertex datum, baselines for
    ' dimension creation
    ' These are optional; if not selected, autodimension uses default datums,
    ' the leftmost and bottommost edges
    selmark = swAutodimMark_e.swAutodimMarkHorizontalDatum
    selmark = swAutodimMark_e.swAutodimMarkVerticalDatum
    selmark = swAutodimMark_e.swAutodimMarkOriginDatum
```

```
    ' Select a vertex
    status = swModelDocExt.SelectByID2("", "VERTEX", 0.20215546544586, 0.2496899375, 4.79999999998881E-03, True, selmark, Nothing, 0)
```

```
    ' Autodimensions the drawing view based on the selected vertex
    ret = swDrawing.AutoDimension(swAutodimEntities_e.swAutodimEntitiesBasedOnPreselect, swAutodimScheme_e.swAutodimSchemeBaseline, swAutodimHorizontalPlacement_e.swAutodimHorizontalPlacementAbove, swAutodimScheme_e.swAutodimSchemeBaseline, swAutodimVerticalPlacement_e.swAutodimVerticalPlacementRight)
```

```
End Sub
```

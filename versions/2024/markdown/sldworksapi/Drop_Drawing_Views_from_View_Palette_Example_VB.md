---
title: "Drop Drawing Views from View Palette Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Drop_Drawing_Views_from_View_Palette_Example_VB.htm"
---

# Drop Drawing Views from View Palette Example (VBA)

This example shows how to drop drawing views from the View Palette.

```
'-----------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\blade shaft.sldasm.
' 2. Click File > Make Drawing from Assembly > OK.
' 3. Click a blank area of the FeatureManager design tree.
'
' Postconditions:
' 1. Drops the Current, Isometric, and Front views onto
'    the drawing sheet.
' 2. Examine the drawing and Immediate window.
'-----------------------------------------------------------------------
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
    Dim swDrawing As SldWorks.DrawingDoc
    Dim swFeature As SldWorks.Feature
    Dim swSubFeature As SldWorks.Feature
    Dim swSheet As SldWorks.Sheet
    Dim swView As SldWorks.View
    Dim bFound As Boolean
    Dim vViewNames As Variant
    Dim vViewName As Variant
    Dim strViewName As String
    Dim lNumViews As Long
    Dim dSheetScale As Double
    Dim vSheetProperties As Variant
    Dim nPaperSize As swDwgPaperSizes_e
    Dim dWidth As Double
    Dim dHeight As Double
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
```

```
    ' Get current sheet
    Set swSheet = swDrawing.GetCurrentSheet
    vSheetProperties = swSheet.GetProperties
    dSheetScale = vSheetProperties(2) / vSheetProperties(3)
    nPaperSize = swSheet.GetSize(dWidth, dHeight)
```

```
    Debug.Print "Sheet scale  = " & dSheetScale
    Debug.Print "Sheet width  = " & dWidth
    Debug.Print "Sheet height = " & dHeight
```

```
    lNumViews = 0
    vViewNames = swDrawing.GetDrawingPaletteViewNames
```

```
    If (Not (IsEmpty(vViewNames))) Then
        lNumViews = (UBound(vViewNames) - LBound(vViewNames) + 1)
        Debug.Print "Number of views on palette = " & lNumViews
        For Each vViewName In vViewNames
            strViewName = vViewName
            Debug.Print strViewName
            If (strViewName = "*Current") Then
                Set swView = swDrawing.DropDrawingViewFromPalette2(strViewName, dWidth / 5#, dHeight / 5#, 0#)
                Debug.Print "  Dropped => " & swView.Name
            End If
```

```
            If (strViewName = "*Isometric") Then
                Set swView = swDrawing.DropDrawingViewFromPalette2(strViewName, dWidth / 3#, dHeight / 2#, 0#)
                Debug.Print "  Dropped => " & swView.Name
            End If
```

```
            If (strViewName = "*Front") Then
                Set swView = swDrawing.DropDrawingViewFromPalette2(strViewName, dWidth / 4#, dHeight / 3#, 0#)
                Debug.Print "  Dropped => " & swView.Name
            End If
        Next vViewName
    End If
```

```
End Sub
```

---
title: "Create Relative Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Relative_Drawing_View_Example_VB.htm"
---

# Create Relative Drawing View Example (VBA)

This example shows how to create a relative drawing view.

```
' ******************************************************************************
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\maingrip.sldprt.
' 2. Select File > Make Drawing from Part.
' 3. Run the macro.
'
' Postconditions:
' 1. Iterates through the drawing views
'    in the View Palette and drops
'    *Current drawing view in the drawing.
' 2. Activates the part.
' 3. Selects two faces for the relative drawing view.
' 4. Activates the drawing.
' 5. Creates and inserts a relative drawing
'    view using the selected faces.
'
' NOTE: Because the part document is used elsewhere, do not
' save any changes when closing it.
' ******************************************************************************
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim numViews As Long
Dim viewNames As Variant
Dim viewName As Variant
Dim viewPaletteName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swDrawing = swApp.ActiveDoc
```

```
    ' Get number of views on View Palette
    numViews = 0
    viewNames = swDrawing.GetDrawingPaletteViewNames
```

```
    ' Iterate through views on View Palette
    ' When view name equals *Current, drop
    ' that view in drawing
    If (Not (IsEmpty(viewNames))) Then
            numViews = (UBound(viewNames) - LBound(viewNames) + 1)
            For Each viewName In viewNames
                viewPaletteName = viewName
                If (viewPaletteName = "*Current") Then
                    Set swView = swDrawing.DropDrawingViewFromPalette2(viewPaletteName, 0#, 0#, 0#)
                End If
            Next viewName
        End If
```

```
    ' Activate the part document and
    ' select two faces for the relative drawing view
    swApp.ActivateDoc3 "maingrip.sldprt", False, swRebuildOnActivation_e.swUserDecision, errors
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "FACE", 4.66263268498324E-02, 5.58799999987514E-03, -6.17351393179888E-03, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 5.04738910727269E-02, 1.67315253537481E-03, -4.96149996774875E-03, True, 2, Nothing, 0)
```

```
    ' Activate the drawing document
    ' Create and insert the relative drawing view using
    ' the selected faces
    ' Activate the relative drawing view
    swApp.ActivateDoc3 "maingrip - Sheet1", False, swRebuildOnActivation_e.swUserDecision, errors
    Set swDrawing = swApp.ActiveDoc
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\maingrip.sldprt"
    Set swView = swDrawing.CreateRelativeView(fileName, 0.203608914116486, 0.493530187561698, swRelativeViewCreationDirection_FRONT, swRelativeViewCreationDirection_RIGHT)
    status = swDrawing.ActivateView("Drawing View2")
```

```
End Sub
```

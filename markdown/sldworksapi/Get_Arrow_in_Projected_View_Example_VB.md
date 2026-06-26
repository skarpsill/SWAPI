---
title: "Get Arrow in Projected View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Arrow_in_Projected_View_Example_VB.htm"
---

# Get Arrow in Projected View Example (VBA)

This example shows how to get the arrow in a projected view.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a drawing that has a projected view that contains
'    an arrow with a label.
' 2. Select that projected view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets information about the projected view's arrow.
' 2. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Sub ProcessTextFormat(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTextFormat As SldWorks.TextFormat)

    Debug.Print "    BackWards                    = " & swTextFormat.BackWards
    Debug.Print "    Bold                         = " & swTextFormat.Bold
    Debug.Print "    CharHeight                   = " & swTextFormat.CharHeight
    Debug.Print "    CharHeightInPts              = " & swTextFormat.CharHeightInPts
    Debug.Print "    CharSpacingFactor            = " & swTextFormat.CharSpacingFactor
    Debug.Print "    Escapement                   = " & swTextFormat.Escapement
    Debug.Print "    IsHeightSpecifiedInPts       = " & swTextFormat.IsHeightSpecifiedInPts
    Debug.Print "    Italic                       = " & swTextFormat.Italic
    Debug.Print "    LineLength                   = " & swTextFormat.LineLength
    Debug.Print "    LineSpacing                  = " & swTextFormat.LineSpacing
    Debug.Print "    ObliqueAngle                 = " & swTextFormat.ObliqueAngle
    Debug.Print "    Strikeout                    = " & swTextFormat.Strikeout
    Debug.Print "    TypeFaceName                 = " & swTextFormat.TypeFaceName
    Debug.Print "    Underline                    = " & swTextFormat.Underline
    Debug.Print "    UpsideDown                   = " & swTextFormat.UpsideDown
    Debug.Print "    Vertical                     = " & swTextFormat.Vertical
    Debug.Print "    WidthFactor                  = " & swTextFormat.WidthFactor

    Debug.Print ""
End Sub
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swView                      As SldWorks.View
    Dim swProjArr                   As SldWorks.ProjectionArrow
    Dim swBaseView                  As SldWorks.View
    Dim vCoord                      As Variant
    Dim swTextFormat                As SldWorks.TextFormat
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swProjArr = swView.GetProjectionArrow
    Set swBaseView = swProjArr.GetView
    Set swTextFormat = swProjArr.GetTextFormat
```

```
    vCoord = swProjArr.GetCoordinates
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swView.Name & " --> " & swBaseView.Name
    Debug.Print "  Coordinates              = (" & vCoord(0) * 1000# & ", " & vCoord(1) * 1000# & ", " & vCoord(2) * 1000# & ") mm"
    Debug.Print "  Label                    = " & swProjArr.GetLabel
    Debug.Print "  Use document text format = " & swProjArr.GetUseDocTextFormat
```

```
    ProcessTextFormat swApp, swModel, swTextFormat
```

```
End Sub
```

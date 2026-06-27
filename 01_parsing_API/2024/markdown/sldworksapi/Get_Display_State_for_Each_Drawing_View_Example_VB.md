---
title: "Get Display State for Each Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_for_Each_Drawing_View_Example_VB.htm"
---

# Get Display State for Each Drawing View Example (VBA)

This example shows how to get the display state for each drawing view.

```
'------------------------------------------------------
' Preconditions:
' 1. Open a drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the drawing views on the current sheet and
'    gets each drawing view's display state.
' 2. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim swView As SldWorks.View
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
    Set swView = swDraw.GetFirstView
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swSheet.GetName
```

```
    While Not swView Is Nothing
        Debug.Print "    " & swView.GetName2 & " [" & swView.DisplayState & "]"
        Set swView = swView.GetNextView
    Wend
```

```
End Sub
```

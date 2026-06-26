---
title: "Activate Each View on Current Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Each_View_on_Current_Sheet_Example_VB.htm"
---

# Activate Each View on Current Sheet Example (VBA)

This example shows how to activate each drawing view on the current sheet.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a drawing with one or more drawing views.
' 2. Click a drawing view to activate it.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Activates each drawing view on the current sheet.
' 2. Examine the Immediate window.
'-----------------------------------------------------
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
    Dim swActiveView As SldWorks.View
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
    Set swActiveView = swDraw.ActiveDrawingView
    Set swView = swDraw.GetFirstView
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swSheet.GetName
    Debug.Print "  Active view = " & swActiveView.GetName2
    Debug.Print ""
```

```
    While Not swView Is Nothing
        Debug.Print "    " & swView.GetName2 & " [" & swView.Type & "]"
        ' Returns false if trying to activate the drawing sheet
        bRet = swDraw.ActivateView(swView.GetName2):
        If False = bRet Then
            Debug.Assert swSheet.GetName = swView.GetName2
            bRet = swDraw.ActivateSheet(swView.GetName2)
        End If
        Debug.Assert bRet
        Set swView = swView.GetNextView
    Wend
```

```
End Sub
```

---
title: "Get Display State for Each Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_for_Each_Drawing_View_Example_VBNET.htm"
---

# Get Display State for Each Drawing View Example (VB.NET)

This example shows how to get the display state for each drawing view.

```
'-------------------------------------------------------
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
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim swSheet As Sheet
        Dim swView As View

        swModel = swApp.ActiveDoc
        swDraw = swModel
        swSheet = swDraw.GetCurrentSheet
        swView = swDraw.GetFirstView
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  " & swSheet.GetName)
        While Not swView Is Nothing
            Debug.Print("    " & swView.GetName2 & " [" & swView.DisplayState & "]")
            swView = swView.GetNextView
        End While
    End Sub

    Public swApp As SldWorks

End Class
```

---
title: "Mirror View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_View_Example_VBNET.htm"
---

# Mirror View Example (VB.NET)

This example shows how to mirror a view.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Mirrors the drawing view.
' 3. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swDrawing As DrawingDoc
        Dim swView As View
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim mirrored As Boolean
        Dim orientation As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.slddrw"
        swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swView = swDrawing.GetFirstView 'This is the drawing template
        swView = swView.GetNextView 'This is the first drawing view in the drawing
        swView.SetMirrorViewOrientation(True, swMirrorViewPositions_e.swMirrorViewPosition_Horizontal)
        swView.GetMirrorViewOrientation(mirrored, orientation)
        Debug.Print("Mirrored? " & mirrored)
        Debug.Print("Orientation (0 = horizontal)? " & orientation)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

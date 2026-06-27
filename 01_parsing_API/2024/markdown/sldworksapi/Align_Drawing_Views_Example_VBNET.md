---
title: "Align Drawing Views Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Drawing_Views_Example_VBNET.htm"
---

# Align Drawing Views Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swDrawingDoc As DrawingDoc
    Dim swView As View
    Dim swViewAlignWith As View
    Dim swModelDocExtension As ModelDocExtension
    Dim swSelectionMgr As SelectionMgr
    Dim status As Boolean
    Dim errors As Integer, warnings As Integer
    Dim fileName As String

    Sub main()

        ' Open drawing
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swDrawingDoc = swModel

        ' Activate Sheet2
        status = swDrawingDoc.ActivateSheet("Sheet2")
        swModel.ClearSelection2(True)

        ' Activate Drawing View6 and make it the active
        ' drawing view
        status = swDrawingDoc.ActivateView("Drawing View6")
        swView = swDrawingDoc.ActiveDrawingView
        swModelDocExtension = swModel.Extension

        ' Select Drawing View3 and select it to be
        ' the base view
        status = swModelDocExtension.SelectByID2("Drawing View3", "DRAWINGVIEW", 0.166130896593432, 0.265618781363279, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swViewAlignWith = swSelectionMgr.GetSelectedObject6(1, -1)

        ' Drawing View6 aligns horizontally
        ' with the center of Drawing View3
        status = swView.AlignWithView(swAlignViewTypes_e.swAlignViewHorizontalCenter, swViewAlignWith)

        Debug.Print("Did the specified drawing views align? " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

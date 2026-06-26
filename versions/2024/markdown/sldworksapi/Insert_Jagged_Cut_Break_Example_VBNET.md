---
title: "Insert Jagged Cut Break Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Jagged_Cut_Break_Example_VBNET.htm"
---

# Insert Jagged Cut Break Example (VB.NET)

This example shows how to insert a jagged cut break in a drawing view.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing and selects Drawing View1.
' 2. Inserts a jagged cut break.
' 3. Examine the drawing and Immediate window.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save changes.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDrawingDoc As DrawingDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionManager As SelectionMgr
        Dim swView As View
        Dim swBreakLine As BreakLine
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swDrawingDoc = swModel
        swModelDocExt = swModel.Extension

        ' Activate and select the view to which to add jagged cut break
        status = swDrawingDoc.ActivateView("Drawing View1")
        status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionManager = swModel.SelectionManager
        swView = swSelectionManager.GetSelectedObject6(1, -1)
        swBreakLine = swView.InsertBreak3(2, -0.0291950859897372, 0.0198236302285804, swBreakLineStyle_e.swBreakLine_Jagged, 2, True)
        Debug.Print("Break line style (5 = jagged cut): " & swBreakLine.Style)
        Debug.Print(" Shape intensity: " & swBreakLine.ShapeIntensity)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

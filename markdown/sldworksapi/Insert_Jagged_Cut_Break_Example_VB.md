---
title: "Insert Jagged Cut Break Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Jagged_Cut_Break_Example_VB.htm"
---

# Insert Jagged Cut Break Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim swBreakLine As SldWorks.BreakLine
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawingDoc = swModel
    Set swModelDocExt = swModel.Extension
```

```
    ' Activate and select the view to which to add jagged cut break
    status = swDrawingDoc.ActivateView("Drawing View1")
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionManager = swModel.SelectionManager
    Set swView = swSelectionManager.GetSelectedObject6(1, -1)
    Set swBreakLine = swView.InsertBreak3(2, -2.91950859897372E-02, 1.98236302285804E-02, swBreakLineStyle_e.swBreakLine_Jagged, 2, True)
    Debug.Print "Break line style (5 = jagged cut): " & swBreakLine.Style
    Debug.Print " Shape intensity: " & swBreakLine.ShapeIntensity
```

```
End Sub
```

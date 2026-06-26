---
title: "Create Break View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Broken_View_Example_VB.htm"
---

# Create Break View Example (VBA)

This example shows how to create and remove a broken view.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified file to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing and selects Drawing View1.
' 2. Examine the drawing, then press F5.
' 3. Inserts break lines in Drawing View1.
' 4. Examine the drawing, then press F5.
' 5. Modifies the positions of the break lines and breaks the view.
' 6. Examine the drawing, then press F5.
' 7. Removes the break from Drawing View1.
' 8. Examine the drawing and the Immediate window.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save changes.
'----------------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swSelectData As SldWorks.SelectData
Dim swView As SldWorks.View
Dim swBreakLine As SldWorks.BreakLine
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long

Sub main()

    Set swApp = Application.SldWorks

    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw"

    Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)

    Set swDrawingDoc = swModel

    Set swModelDocExt = swModel.Extension
```

```vb
    ' Activate and select the view to break
     status = swDrawingDoc.ActivateView("Drawing View1")
     status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
     Set swSelectionManager = swModel.SelectionManager
     Set swSelectData = swSelectionManager.CreateSelectData
     Set swView = swSelectionManager.GetSelectedObject6(1, -1)
    Stop
     ' Examine the drawing; press F5

     Set swBreakLine = swView.InsertBreak(2, -2.91950859897372E-02, 1.98236302285804E-02, 2)

    Stop
     ' Break lines inserted; press F5

     status = swBreakLine.SetPosition(-0.03, 0.05)
     swModel.EditRebuild3
     Debug.Print ("Break line: ")
     Debug.Print (" Selected: " & swBreakLine.Select(True, Nothing))
     Debug.Print (" Style: " & swBreakLine.Style)
     Debug.Print (" Orientation: " & swBreakLine.Layer)
     Debug.Print (" Position: " & swBreakLine.GetPosition(0))

     swDrawingDoc.BreakView

    Stop
     ' Positions of the break lines are modified, and the view is broken
     ' Press F5

     status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
     swDrawingDoc.UnBreakView

     ' Break is removed

 End Sub
```

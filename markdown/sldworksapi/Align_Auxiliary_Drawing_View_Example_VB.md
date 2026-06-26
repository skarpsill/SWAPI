---
title: "Align Auxiliary Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Auxiliary_Drawing_View_Example_VB.htm"
---

# Align Auxiliary Drawing View Example (VBA)

This example shows how to align an auxiliary drawing view.

```vb
 '-------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing with an auxiliary view.
 ' 2. Modify this macro to select the auxiliary view.
 '
 ' Postconditions:
 ' 1. Aligns the auxiliary view horizontally in the clockwise direction.
 ' 2. Press F5.
 ' 3. Aligns the auxiliary view horizontally in a counterclockwise direction.
 ' 4. Press F5.
 ' 5. Aligns the auxiliary view using the default alignment.
 ' 6. Press F5.
 ' 7. Aligns the auxiliary view along the projection angle.
 '------------------------------------------------------------------------------
 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean

Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.110297569919827, 0.215100510639068, 0, False, 0, Nothing, 0)
     Dim DrawView As SldWorks.View
     Set DrawView = Part.SelectionManager.GetSelectedObject6(1, -1)
     boolstatus = DrawView.AlignDrawingView(swHorizontalToSheetClockwise)
     Stop
     boolstatus = DrawView.AlignDrawingView(swHorizontalToSheetCounterclockwise)
     Stop
     boolstatus = DrawView.AlignDrawingView(swDefaultAlignment)
     Stop
     boolstatus = DrawView.AlignDrawingView(swProjectedAngle)
End Sub
```

---
title: "Align Auxiliary Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Auxiliary_Drawing_View_Example_VBNET.htm"
---

# Align Auxiliary Drawing View Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Drawing View2",  "DRAWINGVIEW", 0.110297569919827, 0.215100510639068, 0, False, 0, Nothing, 0)
         Dim DrawView As View
         DrawView = Part.SelectionManager.GetSelectedObject6(1, -1)
         boolstatus = DrawView.AlignDrawingView(swAlignDrawingViewTypes_e.swHorizontalToSheetClockwise)
         Stop
         boolstatus = DrawView.AlignDrawingView(swAlignDrawingViewTypes_e.swHorizontalToSheetCounterclockwise)
         Stop
         boolstatus = DrawView.AlignDrawingView(swAlignDrawingViewTypes_e.swDefaultAlignment)
         Stop
         boolstatus = DrawView.AlignDrawingView(swAlignDrawingViewTypes_e.swProjectedAngle)

     End Sub

     Public swApp As SldWorks

 End  Class
```

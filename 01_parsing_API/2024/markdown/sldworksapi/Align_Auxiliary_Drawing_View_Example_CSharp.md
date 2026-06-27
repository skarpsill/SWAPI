---
title: "Align Auxiliary Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Align_Auxiliary_Drawing_View_Example_CSharp.htm"
---

# Align Auxiliary Drawing View Example (C#)

This example shows how to align an auxiliary drawing view.

```vb
//-------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing with an auxiliary view.
 // 2. Modify this macro to select the auxiliary view.
 //
 // Postconditions:
 // 1. Aligns the auxiliary view horizontally in the clockwise direction.
 // 2. Press F5.
 // 3. Aligns the auxiliary view horizontally in a counterclockwise direction.
 // 4. Press F5.
 // 5. Aligns the auxiliary view using the default alignment.
 // 6. Press F5.
 // 7. Aligns the auxiliary view along the projection angle.
 //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace AlignAuxDrawView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 Part;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Drawing View2",  "DRAWINGVIEW", 0.110297569919827, 0.215100510639068, 0, false, 0, null, 0);
             View DrawView = default(View);
             DrawView = (View)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
             boolstatus = DrawView.AlignDrawingView((int)swAlignDrawingViewTypes_e.swHorizontalToSheetClockwise);
             System.Diagnostics.Debugger.Break();
             boolstatus = DrawView.AlignDrawingView((int)swAlignDrawingViewTypes_e.swHorizontalToSheetCounterclockwise);
             System.Diagnostics.Debugger.Break();
             boolstatus = DrawView.AlignDrawingView((int)swAlignDrawingViewTypes_e.swDefaultAlignment);
             System.Diagnostics.Debugger.Break();
             boolstatus = DrawView.AlignDrawingView((int)swAlignDrawingViewTypes_e.swProjectedAngle);
         }

         public SldWorks swApp;
     }
 }
```

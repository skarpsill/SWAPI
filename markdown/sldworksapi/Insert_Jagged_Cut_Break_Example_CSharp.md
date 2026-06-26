---
title: "Insert Jagged Cut Break Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Jagged_Cut_Break_Example_CSharp.htm"
---

# Insert Jagged Cut Break Example (C#)

This example shows how to insert a jagged cut break in a drawing view.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Verify that the drawing to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing and selects Drawing View1.
// 2. Inserts a jagged cut break.
// 3. Examine the drawing and Immediate window.
//
// NOTE: Because this drawing document is used elsewhere,
// do not save changes.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            View swView = default(View);
            BreakLine swBreakLine = default(BreakLine);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawingDoc = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Activate and select the view to which to add jagged cut break
            status = swDrawingDoc.ActivateView("Drawing View1");
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swView = (View)swSelectionManager.GetSelectedObject6(1, -1);
            swBreakLine = (BreakLine)swView.InsertBreak3(2, -0.0291950859897372, 0.0198236302285804, (int)swBreakLineStyle_e.swBreakLine_Jagged, 2, true);
            Debug.Print("Break line style (5 = jagged cut): " + swBreakLine.Style);
            Debug.Print(" Shape intensity: " + swBreakLine.ShapeIntensity);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

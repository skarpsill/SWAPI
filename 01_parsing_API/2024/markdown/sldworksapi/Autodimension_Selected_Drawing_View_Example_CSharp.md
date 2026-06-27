---
title: "Autodimension Selected Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_Selected_Drawing_View_Example_CSharp.htm"
---

# Autodimension Selected Drawing View Example (C#)

This example shows how to autodimension a selected drawing view.

```
//-----------------------------------------------------------------
// Preconditions: Verify that the specified drawing document to
// open exists.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Activates Drawing View1.
// 3. Selects a vertex.
// 4. Autodimensions the drawing view based on the
//    selected vertex.
// 5. Examine the drawing.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace AutodimensionCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawing = default(DrawingDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int selmark = 0;
            int ret = 0;

            // Open drawing document of part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;
            status = swDrawing.ActivateView("Drawing View1");
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Select drawing view
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);

            // Horizontal and vertical datum, or a vertex datum, baselines for
            // dimension creation
            // These are optional; if not selected, autodimension uses default datums,
            // the leftmost and bottommost edges
            selmark = (int)swAutodimMark_e.swAutodimMarkHorizontalDatum;
            selmark = (int)swAutodimMark_e.swAutodimMarkVerticalDatum;
            selmark = (int)swAutodimMark_e.swAutodimMarkOriginDatum;

            // Select a vertex
            status = swModelDocExt.SelectByID2("", "VERTEX", 0.20215546544586, 0.2496899375, 0.00479999999998881, true, selmark, null, 0);

            // Autodimensions the drawing view based on the selected vertex
            ret = swDrawing.AutoDimension((int)swAutodimEntities_e.swAutodimEntitiesBasedOnPreselect, (int)swAutodimScheme_e.swAutodimSchemeBaseline, (int)swAutodimHorizontalPlacement_e.swAutodimHorizontalPlacementAbove, (int)swAutodimScheme_e.swAutodimSchemeBaseline, (int)swAutodimVerticalPlacement_e.swAutodimVerticalPlacementRight);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Merge and Unmerge Bend Tags Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_and_Unmerge_Bend_Tags_Example_CSharp.htm"
---

# Merge and Unmerge Bend Tags Example (C#)

This example shows how to merge and unmerge bend tags in a drawing.

```
//---------------------------------------------------------------
// Preconditions:
// 1. The specified drawing document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. The specified drawing document opens.
// 2. Press F5 repeatedly after examining the changes
//    in the bend tags and the output in the Immediate window.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MergeBendTagsCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Note swNote = default(Note);
            View swView = default(View);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            Note[] noteList = new Note[2];

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.slddrw";
            swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            System.Diagnostics.Debugger.Break();
            // Locate the bend tags (A, B, C, and D)
            // in the drawing
            // Press F5 to continue

            // Select a bend tag to merge
            status = swModelDocExt.SelectByID2("DetailItem37@Drawing View1", "NOTE", 0.0902750427561398, 0.24484926035503, 0, false, 0, null, 0);
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, 0);
            noteList[0] = swNote;
            Debug.Print("Is a bendline note? " + swNote.IsBendLineNote);
            swModel.ClearSelection2(true);

            // Select another bend tag with which to merge
            // the previously selected bend tag
            status = swModelDocExt.SelectByID2("DetailItem38@Drawing View1", "NOTE", 0.0978933563656073, 0.244401124260355, 0, true, 0, null, 0);
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, 0);
            noteList[1] = swNote;
            Debug.Print("Is a bendline note? " + swNote.IsBendLineNote);
            swModel.ClearSelection2(true);

            // Select the drawing view in which to
            // merge bend tags
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0.0765893917313017, 0.16302919597189, 0, false, 0, null, 0);
            swView = (View)swSelectionMgr.GetSelectedObject6(1, 0);
            swModel.ClearSelection2(true);

            //Merge the selected bend tags
            status = swView.MergeBendTags(true, noteList);

            swModel.EditRebuild3();

            System.Diagnostics.Debugger.Break();
            // Verify that bend tag A and B merged into
            // bend tag A, bend tag C was renamed to B,
            // and bend tag D was renamed to C
            // Press F5 to continue

            // Select the merged bend tag
            swDrawingDoc = (DrawingDoc)swModel;
            status = swDrawingDoc.ActivateView("Drawing View1");
            status = swModelDocExt.SelectByID2("DetailItem38@Drawing View1", "NOTE", 0.098037379978424, 0.245097849056604, 0, false, 0, null, 0);
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, 0);
            noteList[0] = swNote;

            // Unmerge the merged bend tag
            swView.MergeBendTags(false, noteList);

            System.Diagnostics.Debugger.Break();
            // Verify that bend tag A and B unmerged,
            // bend tag B was renamed back to C, and bend tag C
            // was renamed back to D
            // Press F5 to finish

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

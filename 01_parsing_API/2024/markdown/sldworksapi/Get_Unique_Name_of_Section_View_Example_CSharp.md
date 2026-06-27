---
title: "Get Unique Name of Section View Example(C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Unique_Name_of_Section_View_Example_CSharp.htm"
---

# Get Unique Name of Section View Example(C#)

## Get Unique Name of Section View Example (C#)

This example shows how to get the unique name of a section view.

```
//----------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing document with three views,
//    two of which are section views with the
//    same display name.
// 2. Open the Immediate window.
//
// Postconditions: Inspect the Immediate window
// for the display names and internal unique names
// of the section views.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace UniqueNameCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDraw = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);
            bool boolstat = false;
            SelectionMgr selMgr = default(SelectionMgr);
            View sectionView = default(View);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            selMgr = (SelectionMgr)swModel.SelectionManager;
            swDraw = (DrawingDoc)swModel;
            swSheet = (Sheet)swDraw.GetCurrentSheet();

            // Get the section views
            swView = (View)swDraw.GetFirstView();
            while (((swView != null)))
            {

                if ((swView.Type == (int)swDrawingViewTypes_e.swDrawingSectionView))
                {
                    // Print the section view's display name
                    Debug.Print("Display name: " + swView.GetName2());

                    swModel.ClearSelection2(true);

                    boolstat = swModel.Extension.SelectByID2(swView.GetUniqueName(), "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
                    sectionView = (View)selMgr.GetSelectedObject6(1, -1);

                    // Print the section view's unique name
                    Debug.Print("Unique name: " + sectionView.GetUniqueName());

                    swModel.ClearSelection2(true);
                    Debug.Print("");
                }

                swView = (View)swView.GetNextView();
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

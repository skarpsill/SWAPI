---
title: "Get Display State for Each Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_for_Each_Drawing_View_Example_CSharp.htm"
---

# Get Display State for Each Drawing View Example (C#)

This example shows how to get the display state for each drawing view.

```
//----------------------------------------------------------
// Preconditions:
// 1. Open a drawing.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Traverses the drawing views on the current sheet and
//    gets each drawing view's display state.
// 2. Examine the Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not
// save changes.
//-----------------------------------------------------------
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
            DrawingDoc swDraw = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;
            swSheet = (Sheet)swDraw.GetCurrentSheet();
            swView = (View)swDraw.GetFirstView();
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  " + swSheet.GetName());
            while ((swView != null))
            {
                Debug.Print("    " + swView.GetName2() + " [" + swView.DisplayState + "]");
                swView = (View)swView.GetNextView();
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

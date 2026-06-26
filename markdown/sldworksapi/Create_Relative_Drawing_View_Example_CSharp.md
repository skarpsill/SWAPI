---
title: "Create Relative Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Relative_Drawing_View_Example_CSharp.htm"
---

# Create Relative Drawing View Example (C#)

This example shows how to create a relative drawing view.

```
// ******************************************************************************
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\maingrip.sldprt.
// 2. Select File > Make Drawing from Part.
// 3. Run the macro.
//
// Postconditions:
// 1. Iterates through the drawing views
//    in the View Palette and drops
//    *Current drawing view in the drawing.
// 2. Activates the part.
// 3. Selects two faces for the relative drawing view.
// 4. Activates the drawing.
// 5. Creates and inserts a relative drawing
//    view using the selected faces.
//
// NOTE: Because the part document is used elsewhere, do not
// save any changes when closing it.
// ******************************************************************************

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace CreateRelativeViewCSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        DrawingDoc swDrawing;
        View swView;
        ModelDocExtension swModelDocExt;
        string fileName;
        bool status;
        int errors;
        int warnings;
        int numViews;
        object[] viewNames;
        string viewName;
        string viewPaletteName;
        int i;

        public void Main()
        {
            swDrawing = (DrawingDoc)swApp.ActiveDoc;

            // Get number of views on View Palette
            numViews = 0;
            viewNames = (object[])swDrawing.GetDrawingPaletteViewNames();

            // Iterate through views on View Palette
            // When view name equals *Current, drop
            // that view in drawing
            if (!((viewNames == null)))
            {
                numViews = (viewNames.GetUpperBound(0) - viewNames.GetLowerBound(0));
                for (i = 0; i <= numViews; i++)
                {
                    viewPaletteName = (string)viewNames[i];
                    if ((viewPaletteName == "*Current"))
                    {
                        swView = (View)swDrawing.DropDrawingViewFromPalette2(viewPaletteName, 0.0, 0.0, 0.0);
                    }
                }
            }

            // Activate the part document and
            // select two faces for the relative drawing view
            swApp.ActivateDoc3("maingrip.sldprt", false, (int)swRebuildOnActivation_e.swUserDecision, ref errors);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0466263268498324, 0.00558799999987514, -0.00617351393179888, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0504738910727269, 0.00167315253537481, -0.00496149996774875, true, 2, null, 0);

            // Activate the drawing document
            // Create and insert the relative drawing view using
            // the selected faces
            // Activate the relative drawing view
            swApp.ActivateDoc3("maingrip - Sheet1", false, (int)swRebuildOnActivation_e.swUserDecision, ref errors);
            swDrawing = (DrawingDoc)swApp.ActiveDoc;
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\maingrip.sldprt";
            swView = (View)swDrawing.CreateRelativeView(fileName, 0.203608914116486, 0.493530187561698, (int)swRelativeViewCreationDirection_e.swRelativeViewCreationDirection_FRONT, (int)swRelativeViewCreationDirection_e.swRelativeViewCreationDirection_RIGHT);
            status = swDrawing.ActivateView("Drawing View2");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

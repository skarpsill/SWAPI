---
title: "Scale Hatch Pattern to Section View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Scale_Hatch_Pattern_With_Section_View_Example_CSharp.htm"
---

# Scale Hatch Pattern to Section View Example (C#)

This example shows how to scale a hatch pattern to a section view.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\introsw\bolt-assembly.slddrw.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Scales the hatch pattern to the section view.
// 2. Examine the Immediate window.
//
// NOTE: Because this drawing is used elsewhere, do not save changes.
//--------------------------------------------------------------------------
using System;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        DrawingDoc swDrawing;
        View swView;
        DrSection swSectionView;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawing = (DrawingDoc)swModel;
            swDrawing.ActivateView("Drawing View5");
            swView = (View)swDrawing.ActiveDrawingView;
            swSectionView = (DrSection)swView.GetSection();
            swSectionView.ScaleHatchPattern = true;
            Debug.Print("  Scale hatch pattern to section view? " + swSectionView.ScaleHatchPattern);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

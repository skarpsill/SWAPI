---
title: "Auto-arrange Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Auto-arrange_Dimensions_Example_CSharp.htm"
---

# Auto-arrange Dimensions Example (C#)

This example shows how to auto-arrange the selected dimensions.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
// 2. Box-select the dimensions in Drawing View1.
//
// Postconditions:
// 1. Auto-arranges the selected dimensions.
// 2. Examine Drawing View1.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

using System;

namespace AlignDimensionsCSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swDrawingDoc = (DrawingDoc)swModel;
            status = swModelDocExt.AlignDimensions((int)swAlignDimensionType_e.swAlignDimensionType_AutoArrange,
0.001);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }
}
```

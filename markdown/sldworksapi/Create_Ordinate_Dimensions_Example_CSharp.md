---
title: "Create Ordinate Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ordinate_Dimensions_Example_CSharp.htm"
---

# Create Ordinate Dimensions Example (C#)

This example shows how to create ordinate dimensions in a drawing.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
// 2. Click Tools > Options > Document Properties, expand Dimensions,
//    click Ordinate, change Base ordinate dimension standard to DIN,
//    and click OK.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Creates ordinate dimensions.
// 2. Click a blank area in the drawing.
// 3. Examine the base ordinate dimension in the drawing and the
//    Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//--------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModelDoc = default(ModelDoc2);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            bool status = false;
            int errors = 0;
            bool useDoc = false;
            double arrowSize = 0;

            swModelDoc = (ModelDoc2)swApp.ActiveDoc;
            swDrawingDoc = (DrawingDoc)swModelDoc;
            swModelDocExt = (ModelDocExtension)swModelDoc.Extension;
            status = swDrawingDoc.ActivateView("Drawing View1");

            //Create ordinate dimension
            status = swModelDocExt.SelectByID2("", "VERTEX", 0.0876609155372049, 0.255953076919585, -499.97349537912, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", 0.0954286078448972, 0.256322967029476, -499.97349537912, true, 0, null, 0);
            errors = swModelDocExt.AddOrdinateDimension((int)swAddOrdinateDims_e.swHorizontalOrdinate, 0.094688827625117, 0.272968021978022, 0);

            //Add an ordinate dimension
            swModelDoc.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "VERTEX", 0.101346849603139, 0.257062747249256, -499.97349537912, false, 0, null, 0);
            swModelDoc.ClearSelection2(true);
            swModelDoc.SetPickMode();

            //Change the diameter of the circle of the base ordinate dimension
            status = swModelDocExt.SelectByID2("D1@Sketch3@2012-sm.SLDDRW", "DIMENSION", 0.0878551078448972, 0.275113384615385, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;
            swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, -1);
            swDisplayDimension.SetOrdinateDimensionArrowSize(false, 0.00288);
            swDisplayDimension.GetOrdinateDimensionArrowSize(out useDoc, out arrowSize);
            Debug.Print("Base ordinate dimension diameter of circle for arrow: " + arrowSize * 1000 + "mm");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```

---
title: "Get Arrow in Projected View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Arrow_in_Projected_View_Example_CSharp.htm"
---

# Get Arrow in Projected View Example (C#)

This example shows how to get the arrow in a projected view.

```
//---------------------------------------------------------
// Preconditions:
// 1. Open a drawing that has a projected view that contains
//    an arrow with a label.
// 2. Select that projected view.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets information about the projected view's arrow.
// 2. Examine the Immediate window.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetLabelProjectionArrowCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void ProcessTextFormat(SldWorks swApp, ModelDoc2 swModel, TextFormat swTextFormat)
        {
            Debug.Print("    BackWards                    = " + swTextFormat.BackWards);
            Debug.Print("    Bold                         = " + swTextFormat.Bold);
            Debug.Print("    CharHeight                   = " + swTextFormat.CharHeight);
            Debug.Print("    CharHeightInPts              = " + swTextFormat.CharHeightInPts);
            Debug.Print("    CharSpacingFactor            = " + swTextFormat.CharSpacingFactor);
            Debug.Print("    Escapement                   = " + swTextFormat.Escapement);
            Debug.Print("    IsHeightSpecifiedInPts       = " + swTextFormat.IsHeightSpecifiedInPts());
            Debug.Print("    Italic                       = " + swTextFormat.Italic);
            Debug.Print("    LineLength                   = " + swTextFormat.LineLength);
            Debug.Print("    LineSpacing                  = " + swTextFormat.LineSpacing);
            Debug.Print("    ObliqueAngle                 = " + swTextFormat.ObliqueAngle);
            Debug.Print("    Strikeout                    = " + swTextFormat.Strikeout);
            Debug.Print("    TypeFaceName                 = " + swTextFormat.TypeFaceName);
            Debug.Print("    Underline                    = " + swTextFormat.Underline);
            Debug.Print("    UpsideDown                   = " + swTextFormat.UpsideDown);
            Debug.Print("    Vertical                     = " + swTextFormat.Vertical);
            Debug.Print("    WidthFactor                  = " + swTextFormat.WidthFactor);
            Debug.Print("");
        }

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            DrawingDoc swDraw = default(DrawingDoc);
            View swView = default(View);
            ProjectionArrow swProjArr = default(ProjectionArrow);
            View swBaseView = default(View);
            double[] vCoord = null;
            TextFormat swTextFormat = default(TextFormat);
            bool bRet = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swView = (View)swSelMgr.GetSelectedObject6(1, -1);
            swProjArr = (ProjectionArrow)swView.GetProjectionArrow();
            swBaseView = (View)swProjArr.GetView();
            swTextFormat = (TextFormat)swProjArr.GetTextFormat();
            vCoord = (double[])swProjArr.GetCoordinates();
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  " + swView.Name + " --> " + swBaseView.Name);
            Debug.Print("  Coordinates              = (" + vCoord[0] * 1000.0 + ", " + vCoord[1] * 1000.0 + ", " + vCoord[2] * 1000.0 + ") mm");
            Debug.Print("  Label                    = " + swProjArr.GetLabel());
            Debug.Print("  Use document text format = " + swProjArr.GetUseDocTextFormat());

            ProcessTextFormat(swApp, swModel, swTextFormat);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }

}
```

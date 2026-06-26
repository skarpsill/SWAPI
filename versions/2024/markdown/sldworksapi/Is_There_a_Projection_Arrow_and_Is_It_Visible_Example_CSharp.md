---
title: "Is There a Projection Arrow and Is It Visible Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_CSharp.htm"
---

# Is There a Projection Arrow and Is It Visible Example (C#)

This example shows how to find out if:

- the selected drawing view is a projected view
- a projection arrow exists in the projected view
- the projected arrow is visible

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
// 2. Double-click the projected view (i.e., the upper-right drawing view).
// 3. In the PropertyManager page, click the Arrow check box and
//    type a label for the projection arrow.
// 4. Click OK to close the PropertyManager page.
//
// Postconditions:
// 1. Creates a visible projection arrow for Drawing View2, which is
//    a projected view.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because this drawing document is used elsewhere, do not save
// changes.
//--------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Visibleprojectionarrowcsharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DrawingDoc swDrawing;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}View swView;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ProjectionArrow swProjectionArrow;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int typeDrawingView;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDrawing = (DrawingDoc)swModel;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View2");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (View)swDrawing.ActiveDrawingView;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}typeDrawingView = swView.Type;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (typeDrawingView == 4)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Type of selected drawing view is projected.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Type of selected drawing view is not projected. Exiting macro.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swProjectionArrow = (ProjectionArrow)swView.GetProjectionArrow();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swProjectionArrow != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Projection arrow visible: " + swProjectionArrow.Visible);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("No projection arrow in projected view.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

---
title: "Replace View Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_View_Model_Example_CSharp.htm"
---

# Replace View Model Example (C#)

This example shows how to replace a model in drawing views.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\assem20.slddrw.
 // 2. Verify that the specified replacement model exists.
 //
 // Postconditions: Replaces the specified component in Drawing View1
 // with the specified model.
 //
 // NOTE: Because the model is used elsewhere, do not save changes
 // when closing it.
 //---------------------------------------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
namespace ReplaceViewModel_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            DrawingDoc swDrawingDoc;
            SelectionMgr swSelectionMgr;
            DrawingComponent swDrawingComponent;
            View swView;
            Component2 swComponent;
            object view;
            object instance;
            object[] views = new object[1];
            object[] instances = new object[1];
            DispatchWrapper[] viewsIn = new DispatchWrapper[1];
            DispatchWrapper[] instancesIn = new DispatchWrapper[1];
            bool status;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawingDoc = (DrawingDoc)swModel;
            status = swDrawingDoc.ActivateView("Drawing View1");

            //Select the view in which to replace the model
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swView = (View)swSelectionMgr.GetSelectedObject6(1, -1);
            view = (object)swView;
            views[0] = view;
            viewsIn[0] = new DispatchWrapper(views[0]);

            // Select the instance of the model to replace
            status = swModelDocExt.SelectByID2("Assem20-3@Drawing View1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swDrawingComponent = (DrawingComponent)swSelectionMgr.GetSelectedObject6(1, -1);
            swComponent = (Component2)swDrawingComponent.Component;
            instance = (object)swComponent;
            instances[0] = instance;
            instancesIn[0] = new DispatchWrapper(instances[0]);

            status = swDrawingDoc.ReplaceViewModel("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\bagel.sldprt", (viewsIn), (instancesIn));

        }

        public SldWorks swApp;

    }
}
```

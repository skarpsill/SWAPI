---
title: "Create a Callout in a Model View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Model_View_Callouts_Example_CSharp.htm"
---

# Create a Callout in a Model View Example (C#)

This example shows how to create a callout in a model view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Select:
 //    Project > Add Reference > .NET > SolidWorks.Interop.swpublished
 //
 // Postconditions:
 // 1. A callout with one row is created in the first model view.
 // 2. Press F5 three more times to add a callout to three other model views.

 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swpublished;
 using System;
 using System.Runtime.InteropServices;
 using System.Diagnostics;
 namespace ModelViewCallout_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModelDoc;
         ModelDocExtension swModelDocExtn;
         ModelViewManager ViewMgr;
         ModelView swModelView;
         Callout Viewcallout;

         CalloutHandler handle = new CalloutHandler();

         public void Main()
         {
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExtn = swModelDoc.Extension;

             ViewMgr = swModelDoc.ModelViewManager;
             ViewMgr.ViewportDisplay = (int)swViewportDisplay_e.swViewportFourView;
             swModelDoc.GetModelViewCount();
             swModelView = (ModelView)swModelDoc.GetFirstModelView();
             while (((swModelView != null)))
             {
                 Viewcallout = swModelView.CreateCallout(1, handle);
                 Viewcallout.set_Label2(0,"TEST");
                 Viewcallout.SkipColon =  false;
                 Viewcallout.set_ValueInactive(0,true);
                 Viewcallout.SetTargetPoint(0, 0.0, 0.0, 0.0);
                 Viewcallout.Display(true);
                 System.Diagnostics.Debugger.Break();
                 swModelView = (ModelView)swModelView.GetNext();
             }

         }

         public SldWorks swApp;

     }

     [ComVisibleAttribute(true)]
     public class CalloutHandler : SwCalloutHandler
     {

         public bool OnStringValueChanged(object pManipulator, int RowID, string Text)
         {

             Debug.Print("Text: " + Text);
             Debug.Print("Row: " + RowID);

             return true;

         }

     }
 }
```

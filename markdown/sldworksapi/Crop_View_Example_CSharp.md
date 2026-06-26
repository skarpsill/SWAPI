---
title: "Crop View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_View_Example_CSharp.htm"
---

# Crop View Example (C#)

This example shows how to crop a view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Ensure the specified drawing document exists.
 //
 // Postconditions: The view is cropped around the specified rectangle.
 //
 // NOTE: Because the model is used elsewhere, do not save changes when exiting.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CropView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         View myView;
         DrawingDoc drawingDoc;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw", 3, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("foodprocessor - Sheet1",  false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             myView = (View)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);

             drawingDoc = (DrawingDoc)Part;
             boolstatus = drawingDoc.ActivateView("Drawing View1");
             object vSkLines = null;
             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0574722079408937, 0.0331536511827661, 0, 0.0371399698368841, -0.0373161088172339, 0);

             longstatus = myView.Crop();
             Part.ClearSelection2(true);

         }

         public SldWorks swApp;

     }

 }
```

---
title: "Rotate Drawing View 45 Degrees Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Drawing_View_45_Degrees_Example_CSharp.htm"
---

# Rotate Drawing View 45 Degrees Example (C#)

This example shows how to rotate the selected drawing view 45º.

```vb
 //---------------------------------------------------------------
 // Preconditions: Verify that the specified file to open exists.
 //
 // Postconditions: Rotates the selected drawing view 45º.
 //---------------------------------------- ----------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace DrawingViewRotateCSharp.csproj
 {

     partial  class  SolidWorksMacro
     {

         public  void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             DrawingDoc swDrawing = default(DrawingDoc);
             bool status = false;
             int errors = 0;
             int warnings = 0;

             swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\driveworksxpress\\mobile gantry.slddrw", (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "",  ref errors,  ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swModel.ViewZoomtofit2();
             swDrawing = (DrawingDoc)swModel;

             status = swDrawing.ActivateView("Drawing View4");
             status = swModelDocExt.SelectByID2("Drawing View4", "DRAWINGVIEW", 0.1122300799499, 0.1471819585104, 0, false, 0, null, 0);

             //Convert degrees to radians, the default system unit
             // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
             status = swDrawing.DrawingViewRotate(45 / 57.3);
         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

---
title: "Set Display Mode of View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Display_Mode_of_View_Example_CSharp.htm"
---

# Set Display Mode of View Example (C#)

This example shows how to set the display mode of a drawing view.

```vb
 // -------------------------------------
 // Preconditions:
 // 1. Open a drawing and select a drawing view.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the selected view's current display mode.
 // 2. Resets the display mode.
 // 3. Gets the new display mode.
 // 4. Examine the Immediate window and graphics area.
 // --------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Diagnostics;
 using System.Globalization;
 using System.IO;
 using System.Linq;
 using System.Reflection;
 using System.Runtime.CompilerServices;
 using System.Security;
 using System.Text;
 using System.Threading.Tasks;
 using Microsoft.VisualBasic;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace SetDisplayMode_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
           public  void Main()
          {
                   ModelDoc2 swModel;
                   DrawingDoc swDraw;
                   Sheet swSheet;
                  View swView;
                   SelectionMgr swSelectionMgr;

                  swModel = (ModelDoc2)swApp.ActiveDoc;
                  swDraw = (DrawingDoc)swModel;
                  swSheet = (Sheet)swDraw.GetCurrentSheet();
                  swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

                  swView = (View)swSelectionMgr.GetSelectedObject6(1, -1);

                   Debug.Print("=====Current Display Mode======");
                   Debug.Print("");

                  bool UseParentProp;
                  UseParentProp = swView.GetUseParentDisplayMode();
                   Debug.Print("Using parent view mode?  " + UseParentProp);

                   long displayMode;
                  displayMode = swView.GetDisplayMode2();
                   Debug.Print("Current display mode as defined by swDisplayMode_e:  " + displayMode);

                   bool Facetted;
                  Facetted = swView.GetFacettedHlrDisplay();
                   Debug.Print("Faceted (draft quality)?:  " + Facetted);

                   bool EdgesMode;
                  EdgesMode = swView.GetDisplayEdgesInShadedMode();
                   Debug.Print("Display edges when the view is in shaded mode?  " + EdgesMode);

                   bool cThreadQuality;
                  cThreadQuality = swView.GetCThreadQuality();
                   Debug.Print("Precision cosmetic thread dislay quality? " + cThreadQuality);

                   // Reset display mode: Do not use parent view's display mode, shaded mode, draft quality, no edges displayed, precision cosmetic threads
                  swView.SetDisplayMode4(false, 3,   true,   false,   true);

                   Debug.Print("");
                   Debug.Print("=====After Setting Display Mode======");
                   Debug.Print("");
                   Debug.Print("Using parent view mode?  " + swView.GetUseParentDisplayMode());
                   Debug.Print("Current display mode as defined by swDisplayMode_e:  " + swView.GetDisplayMode2());
                   Debug.Print("Faceted (draft quality)?  " + swView.GetFacettedHlrDisplay());
                   Debug.Print("Display edges when view is in shaded mode?  " + swView.GetDisplayEdgesInShadedMode());
                   Debug.Print("Precision cosmetic thread dislay quality? " + swView.GetCThreadQuality());
              }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```

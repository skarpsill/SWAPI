---
title: "Display Hidden Lines in Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Hidden_Lines_in_Drawing_Example_CSharp.htm"
---

# Display Hidden Lines in Drawing Example (C#)

This example shows how to set the display mode of a drawing view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document.
 // 2. Select a view.
 // 3. Inspect the graphics area and press F5 six times.
 //
 // Postconditions: The display mode, hide/show, and suppression
 // settings for the document are modified as specified.
 //----------------------------------------------------------------------------

 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace DisplayHiddenLinesinDrawing_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;

             swDraw.ViewDisplayHidden();
             System.Diagnostics.Debugger.Break();
             swDraw.ViewDisplayHiddengreyed();
             System.Diagnostics.Debugger.Break();
             swDraw.ViewDisplayWireframe();
             System.Diagnostics.Debugger.Break();
             swDraw.ViewDisplayShaded();
             System.Diagnostics.Debugger.Break();

             // Suppress view
             swDraw.SuppressView();
             System.Diagnostics.Debugger.Break();
             // Display an X where the view was suppressed
             swDraw.HideShowDrawingViews();
             System.Diagnostics.Debugger.Break();
             // Unsuppress view
             swDraw.UnsuppressView();

         }

         public SldWorks swApp;

     }
 }
```

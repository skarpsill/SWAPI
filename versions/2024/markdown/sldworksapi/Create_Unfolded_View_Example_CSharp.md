---
title: "Create Unfolded View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Unfolded_View_Example_CSharp.htm"
---

# Create Unfolded View Example (C#)

This example shows how to create an unfolded view from an existing view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open:
 //    public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw
 //
 // Postconditions: A new unfolded view is created from Drawing View1.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
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
 namespace InsertUnfoldedView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         DrawingDoc ddoc;
         View myView;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             ddoc = (DrawingDoc)Part;
             boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
             myView = ddoc.CreateUnfoldedViewAt3(0.379074752406062, 0.276482735105582, 0, false);

         }

         public SldWorks swApp;

     }
 }
```

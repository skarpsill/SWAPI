---
title: "Insert Weldment Cut List Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List_Table_Example_CSharp.htm"
---

# Insert Weldment Cut List Table Example (C#)

This example shows how to insert a weldment cut list table in a drawing.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified cut list template exists.
 // 2. Open public_documents\samples\tutorial\weldments\weldment_box2.sldprt.
 // 3. Click File > Make Drawing from Part > OK > drag a view onto
 //    the sheet > OK.
 // 4. Expand the drawing view in the FeatureManager design tree.
 // 5. Right-click weldment_box2 and select Open Part(weldment_box2.sldprt).
 // 6. Right-click the Cut list folder and click Update Automatically.
 // 7. Click Window > weldment_box2 - Sheet1*.
 //
 // Postconditions:
 // 1. Inserts a weldment cut list table.
 // 2. Examine the FeatureManager design tree and graphics area.
 //
 // NOTE: Because this part is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace InsertWeldmentCutList_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         const string WeldmentTableTemplate = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\cut list.sldwldtbt";

         public void Main()
         {

             DrawingDoc oDrawing = default(DrawingDoc);
             View swView = default(View);
             WeldmentCutListAnnotation WMTable = default(WeldmentCutListAnnotation);

             oDrawing = (DrawingDoc)swApp.ActiveDoc;
             swView = (View)oDrawing.GetFirstView();
             swView = (View)swView.GetNextView();

             // Insert the weldment cut list table

             WMTable = swView.InsertWeldmentTable(false, 0.1996662889191, 0.1013905859662, (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "Default<As Welded>", WeldmentTableTemplate);
         }

         public SldWorks swApp;

     }
 }
```

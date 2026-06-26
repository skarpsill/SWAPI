---
title: "Insert Weld Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weld_Table_Example_CSharp.htm"
---

# Insert Weld Table Example (C#)

This example shows how to insert a weld table into a drawing view.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open the drawing of a part that contains a weld bead.
 // 2. Verify that install_dir\lang\english\weldtable-standard.sldwldtbt exists.
 //
 // Postconditions:
 // 1. Inserts a weld table.
 // 2. Examine the drawing and the FeatureManager design tree.
 // -------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace InsertWeldTable_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         DrawingDoc Draw;
         ModelDoc2 Part;
         View swActiveView;

         bool boolstatus;
         Const WeldTableTemplate As String =  "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldtable-standard.sldwldtbt"

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             Draw = (DrawingDoc)Part;
            boolstatus = Draw.ActivateView("Drawing View1");
             swActiveView = (View)Draw.ActiveDrawingView;
             bool boolResult = false;
             boolResult = swActiveView.InsertWeldTable(false, true,  true, 0, 0,  (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft, "Default", WeldTableTemplate);
         }

         public SldWorks swApp;

     }
 }
```

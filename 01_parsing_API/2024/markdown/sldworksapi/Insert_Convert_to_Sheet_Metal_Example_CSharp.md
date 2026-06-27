---
title: "Convert Extrusion to Sheet Metal Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Convert_to_Sheet_Metal_Example_CSharp.htm"
---

# Convert Extrusion to Sheet Metal Example (C#)

This example shows how to convert a solid body to sheet metal.

```vb
 //--------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\sweepcutextrude.sldprt.
 //
 // Postconditions:
 // 1. Converts Boss-Extrude1 to sheet metal containing two rip edges.
 // 2. Examine the FeatureManager design tree, which now contains:
 //    * Sheet-Metal1
 //    * Convert-Solid1
 //    * Flat-Pattern1
 // NOTE: Because the part is used elsewhere, do not save changes.
 //-------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace InsertConvertSheetMetal_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swDoc = null;
             bool boolstatus = false;

             swDoc = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.008205131831119, 0.02357994168915, 0.03366815886659,  true, 0,  null, 0);
             boolstatus = swDoc.Extension.SelectByID2("", "EDGE", -0.004077318654993, 0.02376323764372, 0.04987547143355,  true, 1,  null, 0);
             boolstatus = swDoc.Extension.SelectByID2("", "EDGE", 0.02890215593544, 0.02392631827274, 0.03020230805026,  true, 1,  null, 0);
             boolstatus = swDoc.Extension.SelectByID2("", "EDGE", -0.007010951021414, 0.02376186282277, -0.0001235945334201,  true, 1,  null, 0);

             // Convert extrusion to sheet metal of thickness=13mm,
             //  bend radius=0.5mm, rip gap=2mm, relief type = rectangular,
             //  relief ratio = 0.5, rip edge overlap type = open butt, and
             //  rip edge overlap ratio = 0.5, do not keep bodies
             boolstatus = swDoc.FeatureManager.InsertConvertToSheetMetal2(0.013,  false,  false, 0.0005, 0.002, 0, 0.5, 1, 0.5, false);

             swDoc.ClearSelection2(true);
         }

         public SldWorks swApp;

     }
 }
```

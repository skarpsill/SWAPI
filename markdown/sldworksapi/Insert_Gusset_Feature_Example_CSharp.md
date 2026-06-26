---
title: "Insert Gusset Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Gusset_Feature_Example_CSharp.htm"
---

# Insert Gusset Feature Example (C#)

This example shows how to create a weldment gusset feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 //
 // Postconditions:
 // 1. Creates Gusset5.
 // 2. Expand CutList(32) in the FeatureManager design tree and
 //    scroll to the bottom of the list.
 // 3. Examine the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
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
 namespace InsertGusset_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature myFeature;
         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.600909534718824, 0.15614125327869, -0.985000000000127,  true, 1,  null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.597259667129663, 0.0149999999998727, -0.944257845206607,  true, 1,  null, 0);

             myFeature = Part.FeatureManager.InsertGussetFeature3(0.005, (int)swGussetThicknessType_e.swGussetThicknessBothSides, (int)swGussetProfileLocationType_e.swGussetProfileLocationCenter, false, 0.025, 0.025, 0.015, 0.78539816339745, 0.015,  false,
             0.005, 0, false, false, false, 0.0125, 0.0125, 0.785398163397452, true, false);
         }

         public SldWorks swApp;

     }
 }
```

---
title: "Get Table Anchor Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Table_Anchor_Example_CSharp.htm"
---

# Get Table Anchor Example (C#)

This example shows how to get the anchor for a selected bill of materials table.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document that has a bill of materials.
 // 2. Expand the Sheet Format node in the FeatureManager design tree and
 //    select the bill of materials anchor feature.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace TableAnchor_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeat;
         SelectionMgr swSelMgr;
         TableAnchor swTableAnchor;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, 0);
             swTableAnchor = (TableAnchor)swFeat.GetSpecificFeature2();

             // Type of table anchor as defined in swTableAnnotationType_e
             Debug.Print("Type of table anchor = " + swTableAnchor.Type);

         }

         public SldWorks swApp;

     }
 }
```

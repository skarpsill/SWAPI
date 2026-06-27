---
title: "Get Whether Feature is Frozen Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Feature_is_Locked_Example_CSharp.htm"
---

# Get Whether Feature is Frozen Example (C#)

This example shows how to get whether a feature is frozen.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly.
 // 2. Select a frozen feature in the FeatureManager design tree.
 //
 // Postconditions: Inspect the Immediate Window.
 //-----------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace FeatureIsFrozen_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

             bRet = swFeat.IsFrozen();
             Debug.Print("Feature is frozen? " + bRet);

         }

         public SldWorks swApp;
     }
 }
```

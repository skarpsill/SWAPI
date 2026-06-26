---
title: "Get Fixed Face of Flatten-Bends Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flatten-Bends_Feature_Example_CSharp.htm"
---

# Get Fixed Face of Flatten-Bends Feature Example (C#)

This example shows how to get the fixed face of a flatten-bends feature.

```vb
 //------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part.
 // 2. Select a Process-Bends feature in the FeatureManager design
 //    tree.
 //
 // Postconditions:
 // 1. Rolls the FeatureManager design tree back to the feature
 //    that contains the fixed face of the Process-Bends feature.
 // 2. Selects the fixed face of the Process-Bends feature.
 // 3. Examine the FeatureManager design tree and graphics area,
 //    then press F5.
 // 4. Rolls the FeatureManager design tree forward.
 //-----------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetFixedFace_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             BendsFeatureData swBends = default(BendsFeatureData);
             Face2 swFace = default(Face2);
             Entity swEntity = default(Entity);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swBends = (BendsFeatureData)swFeat.GetDefinition();

             // Roll back to access the Process-Bends feature data
             bRet = swBends.AccessSelections(swModel, null);

             swFace = (Face2)swBends.GetFixedFace();
             swEntity = (Entity)swFace;
             bRet = swEntity.Select4(false, null);

             System.Diagnostics.Debugger.Break();
             // Press F5

             // Cancel any changes made
             swBends.ReleaseSelectionAccess();

         }

         public SldWorks swApp;
     }
 }
```

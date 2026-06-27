---
title: "Get Ruled-Surface Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Ruled_Surface_Feature_Data_Example_CSharp.htm"
---

# Get Ruled-Surface Feature Data Example (C#)

This example shows how to get ruled-surface feature data.

```vb
 //-----------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that contains a ruled-surface feature.
 // 2. Select the ruled-surface feature.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the type of ruled-surface feature.
 // 2. Examine the Immediate window.
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

 namespace RuledSurfaceFeatDataType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeat;
         SelectionMgr swSelMgr;

         RuledSurfaceFeatureData swRuledSurfFeat;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swRuledSurfFeat = (RuledSurfaceFeatureData)swFeat.GetDefinition();

             // Ruled-surface feature type as defined in swRuledSurfaceType_e
             Debug.Print("Ruled-surface feature type: " + swRuledSurfFeat.Type);

         }

         public SldWorks swApp;

     }
 }
```

---
title: "Get Simple Fillet Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Simple_Fillet_Feature_Data_Example_CSharp.htm"
---

# Get Simple Fillet Feature Data Example (C#)

This example shows how to get simple fillet feature data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that contains a simple fillet feature.
 // 2. Select the simple fillet feature.
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
 namespace GetSimpleFilletEdgeCount_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         Feature swFeat;
         SimpleFilletFeatureData2 swFeatData;

         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             boolstatus = swModelDocExt.SelectByID2("Fillet2", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);

             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swFeatData = (SimpleFilletFeatureData2)swFeat.GetDefinition();

             Debug.Print("Edge count: " + swFeatData.GetEdgeCount());

         }

         public SldWorks swApp;

     }
 }
```

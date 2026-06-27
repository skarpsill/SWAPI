---
title: "Get Data for Wrap Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Wrap_Feature_Example_CSharp.htm"
---

# Get Data for Wrap Feature Example (C#)

This example shows how to get data for a wrap feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document with a wrap feature.
 // 2. Select the wrap feature.
 //
 // Postconditions: Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace WrapFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             WrapSketchFeatureData swWrapSketch = default(WrapSketchFeatureData);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swWrapSketch = (WrapSketchFeatureData)swFeat.GetDefinition();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("Feature = " + swFeat.Name);
             Debug.Print("   Reverse direction?  " + swWrapSketch.ReverseDirection);
             Debug.Print("   Type of surface revolve =  " + swWrapSketch.Type);
             Debug.Print("   Thickness =  " + swWrapSketch.Thickness);

         }

         public SldWorks swApp;
     }

 }
```

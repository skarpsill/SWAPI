---
title: "Get Reference Axis Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Axis_Data_Example_CSharp.htm"
---

# Get Reference Axis Data Example (C#)

This example shows how to get reference axis data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part, assembly, or drawing document.
 // 2. Select a reference axis.
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

 namespace ReferenceAxisFeatDataType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             RefAxis swRefAxis = default(RefAxis);
             RefAxisFeatureData swRefAxisData = default(RefAxisFeatureData);
             double[] swMathAxis = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swRefAxis = (RefAxis)swFeat.GetSpecificFeature2();
             swMathAxis = (double[])swRefAxis.GetRefAxisParams();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    Start point = (" + swMathAxis[0] * 1000.0 + ", " + swMathAxis[1] * 1000.0 + ", " + swMathAxis[2] * 1000.0 + ") mm");
             Debug.Print("    End point = (" + swMathAxis[3] * 1000.0 + ", " + swMathAxis[4] * 1000.0 + ", " + swMathAxis[5] * 1000.0 + ") mm");

             swRefAxisData = (RefAxisFeatureData)swFeat.GetDefinition();
             Debug.Print("    Type = " + swRefAxisData.Type);

         }

         public SldWorks swApp;

     }

 }
```

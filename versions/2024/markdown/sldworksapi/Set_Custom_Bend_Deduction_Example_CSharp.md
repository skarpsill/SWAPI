---
title: "Set Custom Bend Deduction Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Custom_Bend_Deduction_Example_CSharp.htm"
---

# Set Custom Bend Deduction Example (C#)

This example shows how to set a custom bend deduction for a miter flange feature.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part that contains a miter flange
 //    feature with bends.
 // 2. Select the miter flange feature.
 //
 // Postconditions: Sets the selected miter flange's custom
 // bend deduction to 1 mm.
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
 namespace CustomBendAllowanceType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         bool boolstatus;
         MiterFlangeFeatureData FeatureData;
         Feature Feature;
         CustomBendAllowance bData;
         SelectionMgr selMgr;
         Component component = null;

         string nam;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             // Get the selected feature
             selMgr = (SelectionMgr)Part.SelectionManager;
             Feature = (Feature)selMgr.GetSelectedObject6(1, -1);

             // Get the name of the selected feature
             nam = Feature.GetTypeName();

             // Get the feature definition
             FeatureData = (MiterFlangeFeatureData)Feature.GetDefinition();

             // Get whether to use default bend allowance to determine the current state
             bool useCustom = false;
             useCustom = FeatureData.UseDefaultBendAllowance;

             // Get the custom bend allowance object
             bData = FeatureData.GetCustomBendAllowance();

             long bType = 0;
             bType = bData.Type;
             // Set the bend allowance type to deduction
             bData.Type = (int)swBendAllowanceTypes_e.swBendAllowanceDeduction;

             // Set the value of the bend deduction
             bData.BendDeduction = 0.001;

             FeatureData.UseDefaultBendAllowance =  false;

             // Set the value of the custom bend deduction
             FeatureData.SetCustomBendAllowance(bData);

             // Modify the feature definition
             boolstatus = Feature.ModifyDefinition(FeatureData, Part, component);

         }

         public SldWorks swApp;

     }

 }
```

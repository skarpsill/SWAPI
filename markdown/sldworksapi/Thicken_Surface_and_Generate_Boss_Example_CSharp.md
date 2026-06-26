---
title: "Thicken Surface and Generate Boss Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Thicken_Surface_and_Generate_Boss_Example_CSharp.htm"
---

# Thicken Surface and Generate Boss Example (C#)

This example shows how to thicken a surface and then generate a boss.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document and select a boundary surface.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a thicken feature.
 // 2. Inspect the Immediate window.
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
 namespace GetThickenFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             FeatureManager swFeatMgr = default(FeatureManager);
             Feature swFeat = default(Feature);
             ThickenFeatureData swThicken = default(ThickenFeatureData);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeatMgr = swModel.FeatureManager;

             bRet = swSelMgr.SetSelectedObjectMark(1, 1, (int)swSelectionMarkAction_e.swSelectionMarkSet);

             swFeat = swFeatMgr.FeatureBossThicken(0.001, (int)swThickenThicknessType_e.swThickenSideOne, 0, false, true, true, true);
             swThicken = (ThickenFeatureData)swFeat.GetDefinition();

             Debug.Print("Feature: " + swFeat.Name);
             Debug.Print("  Automatically select all bodies? " + swThicken.AutoSelect);
             Debug.Print("  True if thicken feature affects specified bodies, false if it affects all bodies: " + swThicken.FeatureScope);
             Debug.Print("  Is a boss feature? " + swThicken.IsBossFeature());
             Debug.Print("  Merge the results if a multibody part?  " + swThicken.Merge);
             Debug.Print("  Fill a volume?  " + swThicken.FillVolume);
             Debug.Print("  Thickness:  " + swThicken.Thickness * 1000.0 + " mm");
             Debug.Print("  Thickness type as defined in swThickenThicknessType_e:  " + swThicken.ThicknessSide);

         }

         public SldWorks swApp;

     }
 }
```

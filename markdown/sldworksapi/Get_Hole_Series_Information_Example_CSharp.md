---
title: "Get Hole Series Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hole_Series_Information_Example_CSharp.htm"
---

# Get Hole Series Information Example (C#)

This example shows how to get information about a hole series.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly that contains a hole series feature.
 // 2. Configure holes in the SOLIDWORKS Toolbox.
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
 namespace HoleSeriesFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         SelectionMgr SelMgr;
         bool boolstatus;
         Feature swFeat;
         HoleSeriesFeatureData2 swFeatData;
         Face2 swFace;

         Entity swEnt;

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             SelMgr = (SelectionMgr)swDoc.SelectionManager;
             swFeat = (Feature)swDoc.FirstFeature();

             while ((swFeat != null))
             {
                 Debug.Print(swFeat.GetTypeName() + ", " + swFeat.Name);
                 if (swFeat.GetTypeName() == "HoleSeries")
                 {
                     swFeatData = (HoleSeriesFeatureData2)swFeat.GetDefinition();
                     Debug.Print("  Standard:", swFeatData.Standard);

                     int i = 0;

                     for (i = 0; i <= swFeatData.GetComponentsCount() - 1; i++)
                     {
                         Debug.Print("  Component " + i);
                         Debug.Print("    Type:", swFeatData.get_Type(i));
                         Debug.Print("    Size:", swFeatData.get_Size(i));
                     }

                     Debug.Print("  FastenerMaterial:", swFeatData.Material);

                     // Bolt and nut information causes an error
                     // if SOLIDWORKS Toolbox is not configured
                     Debug.Print("  BoltHeadDiameter:", swFeatData.BoltHeadDiameter);
                     Debug.Print("  BoltDiameter:", swFeatData.BoltDiameter);
                     Debug.Print("  NutDiameter:", swFeatData.NutDiameter);
                     Debug.Print("  FastenerPreload:", swFeatData.Preload);
                     Debug.Print("  FastenerDefaultUnits:", swFeatData.FastenerDefaultUnits);
                     Debug.Print("  FastenerTopHoleType:", swFeatData.FastenerTopHoleType);
                     Debug.Print("  FastenerBottomHoleType:", swFeatData.FastenerBottomHoleType);
                     Debug.Print("  FastenerHoleCount:", swFeatData.FastenerHoleCount);

                     // End face
                     swFeatData.AccessSelections(swDoc, null);
                     swFace = (Face2)swFeatData.EndFace;
                     swEnt = (Entity)swFace;

                     if ((swEnt != null))
                     {
                         boolstatus = swEnt.Select4(false, null);
                         Debug.Print(" Face selection = " + boolstatus);
                     }

                     // Sketch points
                     int ncount = 0;
                     ncount = swFeatData.GetSketchPointsCount();
                     Debug.Print(" Sketch Point Count = " + ncount);

                     object[] vPtArr = null;
                     vPtArr = (object[])swFeatData.GetSketchPoints();

                     SketchPoint swSketchPoint = default(SketchPoint);

                     for (i = 0; i < ncount; i++)
                     {
                         swSketchPoint = (SketchPoint)vPtArr[i];
                         swSketchPoint.Select4(false, null);
                     }

                     // Components
                     ncount = swFeatData.GetComponentsCount();
                     Debug.Print("  ComponentsCount Count = " + ncount);
                     vPtArr = (object[])swFeatData.GetComponents();
                     Component swComp = null;

                     for (i = 0; i < ncount; i++)
                     {
                         swComp = (Component)vPtArr[i];
                         if ((swComp != null))
                         {
                             Debug.Print("  " + swComp.Name2 + " --> " + swComp.GetPathName());
                         }
                         else
                         {
                             Debug.Print("  Could not get component.");
                         }
                     }

                     swFeatData.ReleaseSelectionAccess();

                 }

                 swFeat = (Feature)swFeat.GetNextFeature();

             }

         }

         public SldWorks swApp;

     }
 }
```

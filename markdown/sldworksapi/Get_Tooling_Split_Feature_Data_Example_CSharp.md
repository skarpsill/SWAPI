---
title: "Get Tooling Split Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tooling_Split_Feature_Data_Example_CSharp.htm"
---

# Get Tooling Split Feature Data Example (C#)

This example shows how to get tooling split feature data.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that contains a Tooling Split1 feature.
 // 2. Select Tooling Split1 in the FeatureManager design tree.
 // 3. Open an Immediate window.
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

 namespace GetToolingSplitData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         Feature swFeat;
         ToolingSplitFeatureData swToolingSplitFeatData;
         Body2 bod;
         bool bRet;
         int i;
         object[] cavSurf;
         object[] coreSurf;
         object[] partSurf;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swToolingSplitFeatData = (ToolingSplitFeatureData)swFeat.GetDefinition();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    Draft angle: " + swToolingSplitFeatData.Angle);
             Debug.Print("    Depth of block in direction 1: " + swToolingSplitFeatData.get_Depth(0));
             Debug.Print("    Depth of block in direction 2: " + swToolingSplitFeatData.get_Depth(1));
             Debug.Print("    Interlock surface? " + swToolingSplitFeatData.InterlockSurface);

             bRet = swToolingSplitFeatData.AccessSelections(swModel, null);

             Debug.Print("    Cavity surfaces:");
             Debug.Print("    Count: " + swToolingSplitFeatData.GetCavitySurfacesCount());
             cavSurf = (object[])swToolingSplitFeatData.CavitySurfaces;
             for (i = 0; i <= swToolingSplitFeatData.GetCavitySurfacesCount() - 1; i++)
             {
                 bod = (Body2)cavSurf[i];
                 Debug.Print("      " + bod.Name);
             }
             Debug.Print("    Core surfaces:");
             Debug.Print("    Count: " + swToolingSplitFeatData.GetCoreSurfacesCount());
             coreSurf = (object[])swToolingSplitFeatData.CoreSurfaces;
             for (i = 0; i <= swToolingSplitFeatData.GetCoreSurfacesCount() - 1; i++)
             {
                 bod = (Body2)coreSurf[i];
                 Debug.Print("      " + bod.Name);
             }
             Debug.Print("    Parting surfaces:");
             Debug.Print("    Count: " + swToolingSplitFeatData.GetPartingSurfacesCount());
             partSurf = (object[])swToolingSplitFeatData.PartingSurfaces;
             for (i = 0; i <= swToolingSplitFeatData.GetPartingSurfacesCount() - 1; i++)
             {
                 bod = (Body2)partSurf[i];
                 Debug.Print("      " + bod.Name);
             }

             swToolingSplitFeatData.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

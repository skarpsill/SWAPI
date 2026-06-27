---
title: "Get Sheet Metal Folder Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_Metal_Folder_Feature_Example_CSharp.htm"
---

# Get Sheet Metal Folder Feature Example (C#)

This example shows how to get the sheet metal folder and its contents.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a multibody sheet metal part that has a folder
 // of sheet metal features.
 //
 // Postconditions: Inspect the Immediate window.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace GetSheetMetalFolder_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 myModel;
         FeatureManager featureMgr;
         Feature feat;
         SheetMetalFolder sheetMetalFolder;
         object[] featArray;

         int i;

         public void Main()
         {
             myModel = (ModelDoc2)swApp.ActiveDoc;
             featureMgr = myModel.FeatureManager;

             sheetMetalFolder = (SheetMetalFolder)featureMgr.GetSheetMetalFolder();
             feat = (Feature)sheetMetalFolder.GetFeature();
             Debug.Print("Sheet metal folder name: " + feat.Name);
             Debug.Print("  Number of sheet metal features in the folder: " + sheetMetalFolder.GetSheetMetalCount());
             featArray = (object[])sheetMetalFolder.GetSheetMetals();
             for (i = featArray.GetLowerBound(0); i <= featArray.GetUpperBound(0); i++)
             {
                 feat = (Feature)featArray[i];
                 Debug.Print("    " + feat.Name);
             }
         }

         public SldWorks swApp;
     }
 }
```

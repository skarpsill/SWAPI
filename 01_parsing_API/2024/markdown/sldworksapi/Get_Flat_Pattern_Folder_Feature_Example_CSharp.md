---
title: "Get Flat-Pattern Folder Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Flat_Pattern_Folder_Feature_Example_CSharp.htm"
---

# Get Flat-Pattern Folder Feature Example (C#)

This example shows how to get the flat-pattern folder and its contents.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a multibody sheet metal part that has a folder
 // of flat-patterns.
 //
 // Postconditions: Inspect the Immediate window.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace GetFlatPatternFolderFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 myModel;
         FeatureManager featureMgr;
         Feature feat;
         object[] featArray;

         int i;

         public void Main()
         {
             myModel = (ModelDoc2)swApp.ActiveDoc;
             featureMgr = myModel.FeatureManager;
             FlatPatternFolder flatPatternFolder = default(FlatPatternFolder);
             flatPatternFolder = (FlatPatternFolder)featureMgr.GetFlatPatternFolder();
             feat = flatPatternFolder.GetFeature();
             Debug.Print("Flat-pattern folder name: " + feat.Name);
             Debug.Print("  Number of flat-pattern features in the folder: " + flatPatternFolder.GetFlatPatternCount());
             featArray = (object[])flatPatternFolder.GetFlatPatterns();
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

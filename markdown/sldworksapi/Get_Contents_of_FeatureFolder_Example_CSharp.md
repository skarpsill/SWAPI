---
title: "Get Contents of FeatureFolder Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Contents_of_FeatureFolder_Example_CSharp.htm"
---

# Get Contents of FeatureFolder Example (C#)

This example shows how to obtain the contents of feature folders.

```vb
 //-------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Right-click a feature in the FeatureManager design tree.
 // 3. Select Add to New Folder, which adds the feature to
 //    the new folder.
 // 4. Open the Immediate Window.
 //
 // Postconditions: Inspect the Immediate Window.
 //------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace FeatureFolder_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             FeatureManager swFeatMgr = default(FeatureManager);
             Feature swFeat = default(Feature);
             IFeatureFolder swFeatFolder = default(IFeatureFolder);
             Feature swFtrFolder = default(Feature);
             string FeatType = null;
             string FeatTypeName = null;
             object[] Features = null;
             int i = 0;

             Feature[] featureArr = new Feature[3];

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swFeatMgr = swModel.FeatureManager;

             swFeat = (Feature)swModel.FirstFeature();
             while ((swFeat != null))
             {
                 FeatType = swFeat.Name;
                 FeatTypeName = swFeat.GetTypeName2();

                 if ((FeatTypeName == "FtrFolder" & !FeatType.Contains("EndTag")))
                 {
                     Debug.Print(FeatType + " [" + FeatTypeName + "]");
                     swFeatFolder = (IFeatureFolder)swFeat.GetSpecificFeature2();
                     Features = (object[])swFeatFolder.GetFeatures();
                     Debug.Print(" Number of Features: " + swFeatFolder.GetFeatureCount());
                     for (i = 0; i <= (swFeatFolder.GetFeatureCount() - 1); i++)
                     {
                         swFtrFolder = (Feature)Features[i];
                         Debug.Print(" Name of feature: " + swFtrFolder.Name);
                         Debug.Print(" Type of feature: " + swFtrFolder.GetTypeName2());
                     }
                 }
                 swFeat = (Feature)swFeat.GetNextFeature();

             }
         }
         public SldWorks swApp;
     }
 }
```

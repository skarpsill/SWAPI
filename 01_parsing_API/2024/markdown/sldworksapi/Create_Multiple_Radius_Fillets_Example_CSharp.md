---
title: "Create Multiple-Radius Fillets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Radius_Fillets_Example_CSharp.htm"
---

# Create Multiple-Radius Fillets Example (C#)

This example shows how to create multiple-radius fillets.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\box.sldprt.
 // 2. Select three intersecting edges on the inside of the part.
 //
 // Postconditions:
 // 1. Fillets the three selected edges using three
 //    different radii.
 // 2. Examine the graphics area and FeatureManager design tree.
 //
 // Note: Because the model is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace FilletFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         FeatureManager swFeatMgr;
         object VarRadArray8;
         double[] radArray8 = new double[3];

         int FilletOptions;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swFeatMgr = swModel.FeatureManager;

             //Multiple Radii
             radArray8[0] = 0.01;
             radArray8[1] = 0.015;
             radArray8[2] = 0.02;
             VarRadArray8 = radArray8;

             //Fillet options
             FilletOptions = (int)swFeatureFilletOptions_e.swFeatureFilletPropagate + (int)swFeatureFilletOptions_e.swFeatureFilletAttachEdges + (int)swFeatureFilletOptions_e.swFeatureFilletKeepFeatures;

             //Create multiple-radius fillets along selected edges
             swFeatMgr.FeatureFillet(FilletOptions, 0.01, (int)swFeatureFilletType_e.swFeatureFilletType_Simple, (int)swFilletOverFlowType_e.swFilletOverFlowType_Default, (VarRadArray8), 0, 0);

         }

         public SldWorks swApp;

     }
 }
```

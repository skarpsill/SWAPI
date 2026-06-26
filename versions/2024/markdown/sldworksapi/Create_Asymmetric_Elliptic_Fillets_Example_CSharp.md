---
title: "Create Variable Radius Asymmetric Elliptical Fillet Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Asymmetric_Elliptic_Fillets_Example_CSharp.htm"
---

# Create Variable Radius Asymmetric Elliptical Fillet Example (C#)

This example shows how to create a variable radius asymmetric elliptical fillet and get its data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\block.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a variable radius asymmetric elliptical fillet, VarFillet1,
 //    in the FeatureManager design tree.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace FeatureFillet3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         Feature myFeature;
         Edge swedge;
         Vertex ver1;
         Vertex ver2;
         VariableFilletFeatureData2 swFeatData;
         int Fillet_ProfileTyp;
         double[] dists26 = new double[2];
         double AsyRadius1;
         double AsyRadius2;
         double AsyRadius3;
         double AsyRadius4;
         bool boolstatus;
         double[] radiis = new double[2];
         object radiiArray0;
         object conicRhosArray0;
         object setBackArray0;
         object pointArray0;
         object pointRhoArray0;
         object dist2Array0;
         object pointDist2Array0;

         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             radiis[0] = 0.008;
             radiis[1] = 0.009;
             radiiArray0 = radiis;
             dists26[0] = 0.006;
             dists26[1] = 0.007;
             dist2Array0 = dists26;

             conicRhosArray0 = 0;
             setBackArray0 = 0;
             pointArray0 = 0;
             pointRhoArray0 = 0;
             pointDist2Array0 = 0;
```

```vb
            boolstatus = swModel.Extension.SelectByID2("", "EDGE", 1.66068305868521E-02, -4.40742070395572E-06, -1.49970056632469E-02, true, 1, null, 0);
```

```vb
             if (boolstatus == false)
                 ErrorMsg(swApp, "Failed to select edge");

             myFeature = (Feature)swModel.FeatureManager.FeatureFillet3((int)swFeatureFilletOptions_e.swFeatureFilletAsymmetric + (int)swFeatureFilletOptions_e.swFeatureFilletKeepFeatures + (int)swFeatureFilletOptions_e.swFeatureFilletAttachEdges + (int)swFeatureFilletOptions_e.swFeatureFilletUniformRadius + (int)swFeatureFilletOptions_e.swFeatureFilletPropagate, 0, 0, 0, (int)swFeatureFilletType_e.swFeatureFilletType_VariableRadius, (int)swFilletOverFlowType_e.swFilletOverFlowType_Default, (int)swFeatureFilletProfileType_e.swFeatureFilletCircular, (radiiArray0), (dist2Array0), (conicRhosArray0),
             (setBackArray0), (pointArray0), (pointDist2Array0), (pointRhoArray0));
             if (myFeature == null)
                 ErrorMsg(swApp, "Failed to create fillet");

             swFeatData = (VariableFilletFeatureData2)myFeature.GetDefinition();
             if (swFeatData == null)
                 ErrorMsg(swApp, "Failed to get definition for fillet feature");

             boolstatus = swFeatData.AccessSelections(swModel,  null);
             if (boolstatus == false)
                 ErrorMsg(swApp, "Failed to access selections for fillet feature");

             boolstatus = swFeatData.AsymmetricFillet;
             if (boolstatus == false)
                 ErrorMsg(swApp, "Fillet is not asymmetric");
             Debug.Print("Variable size fillet is asymmetric? " + boolstatus);

             swedge = (Edge)swFeatData.GetFilletEdgeAtIndex(0);
             if (swedge == null)
                 ErrorMsg(swApp, "Failed to get edge");

             ver1 = (Vertex)swedge.GetStartVertex();
             if (ver1 == null)
                 ErrorMsg(swApp, "Failed to get start vertex of edge");

             ver2 = (Vertex)swedge.GetEndVertex();
             if (ver2 == null)
                 ErrorMsg(swApp, "Failed to get end vertex of edge");

             AsyRadius1 = swFeatData.GetRadius2(ver1,  out boolstatus);
             if (AsyRadius1 != 0.008)
                 ErrorMsg(swApp, "Radius R1 at vertex V1 is wrong");
             Debug.Print("Radius R1 at vertex V1: " + AsyRadius1);

             AsyRadius2 = swFeatData.GetDistance(ver1);
             if (AsyRadius2 != 0.006)
                 ErrorMsg(swApp, "Radius R2 at vertex V1 is wrong");
             Debug.Print("Radius R2 at vertex V1: " + AsyRadius2);

             AsyRadius3 = swFeatData.GetRadius2(ver2,  out boolstatus);
             if (AsyRadius3 != 0.009)
                 ErrorMsg(swApp, "Radius R1 for vertex V2 is wrong");
             Debug.Print("Radius R1 at vertex V2: " + AsyRadius3);

             AsyRadius4 = swFeatData.GetDistance(ver2);
             if (AsyRadius4 != 0.007)
                 ErrorMsg(swApp, "Radius R2 for vertex V2 is wrong");
             Debug.Print("Radius R2 at vertex V2: " + AsyRadius4);

             Fillet_ProfileTyp = swFeatData.ConicTypeForCrossSectionProfile;
             if (Fillet_ProfileTyp != 0)
                 ErrorMsg(swApp, "Profile type is not elliptical");
             Debug.Print("Fillet profile type as defined in swFeatureFilletProfileType_e (0 = Elliptical): " + Fillet_ProfileTyp);

             swFeatData.ReleaseSelectionAccess();

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }
 }
```

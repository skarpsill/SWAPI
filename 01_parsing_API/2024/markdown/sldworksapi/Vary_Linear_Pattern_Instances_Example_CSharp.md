---
title: "Vary Linear Pattern Instances Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Vary_Linear_Pattern_Instances_Example_CSharp.htm"
---

# Vary Linear Pattern Instances Example (C#)

This example shows how to vary pattern instances.

//-------------------------------------------------------------------------------

```vb
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\box.sldprt.
 // 2. Open the Immediate window.

 // Postconditions:
 // 1. Creates a bi-directional linear pattern of a CBORE feature.
 // 2. Specifies to vary pattern instances.
 // 3. Sets the spacing increment of instances in both directions.
 // 4. Modifies the spacing of instance #3.
 // 5. Increments a near countersink diameter for all pattern instances in Direction 1.
 // 6. Modifies the near countersink diameter for instance #3.
 // 7. Inspect the Immediate window and the graphics area.
```

//

```vb
 // NOTE: Because the part is used elsewhere, do not save changes.
 //  ------------------------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace VaryPatternInstances_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
           public  void Main()
          {
               ModelDoc2 swModel;
               SelectionMgr swSelMgr;
               Feature feat;
               LinearPatternFeatureData LPFeatData;
               bool boolstatus;
               InstanceToVaryOptions swInstOpts;

              swModel = (ModelDoc2)swApp.ActiveDoc;
              swSelMgr = (SelectionMgr)swModel.SelectionManager;

              boolstatus = swModel.Extension.SelectByRay(0.0439252690830472, 0.0299751045230323, 0.0126537412306789, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000633983676613175, 1,  true, 1, 0);
              boolstatus = swModel.Extension.SelectByRay(-0.0178361123644777, 0.0298747083165836, -0.0388627220451099, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000633983676613175, 1,  true, 2, 0);
              boolstatus = swModel.Extension.SelectByID2("CBORE for #6 Binding Head Machine Screw1",  "BODYFEATURE", 0, 0, 0,   true, 4,   null, 0);
              swModel.ActivateSelectedFeature();
              swModel.ClearSelection2(true);
              boolstatus = swModel.Extension.SelectByID2("CBORE for #6 Binding Head Machine Screw1",  "BODYFEATURE", 0, 0, 0,   false, 4,   null, 0);
              boolstatus = swModel.Extension.SelectByRay(0.0439252690830472, 0.0299751045230323, 0.0126537412306789, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000633983676613175, 1,  true, 1, 0);
              boolstatus = swModel.Extension.SelectByRay(-0.0178361123644777, 0.0298747083165836, -0.0388627220451099, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000633983676613175, 1,  true, 2, 0);

               Feature swFeat;
               FeatureManager swFeatMgr;

              swFeatMgr = swModel.FeatureManager;
               LinearPatternFeatureData swFeatData;
              swFeatData = (LinearPatternFeatureData)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmLPattern);
              swFeatData.D1EndCondition = 0;
              swFeatData.D1ReverseDirection =   false;
              swFeatData.D1Spacing = 0.02;
              swFeatData.D1TotalInstances = 2;
              swFeatData.D2EndCondition = 0;
              swFeatData.D2PatternSeedOnly =   false;
              swFeatData.D2ReverseDirection =   false;
              swFeatData.D2Spacing = 0.01;
              swFeatData.D2TotalInstances = 2;
              swFeatData.GeometryPattern =   false;
              swFeatData.VarySketch =   false;

              swFeat = swFeatMgr.CreateFeature(swFeatData);

              boolstatus = swModel.Extension.SelectByID2("LPattern1",   "BODYFEATURE", 0, 0, 0,   false, 0,   null, 0);
              feat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
              LPFeatData = (LinearPatternFeatureData)feat.GetDefinition();

               // Turn on Instances To Vary
              boolstatus = LPFeatData.AccessSelections(swModel,  null);

              LPFeatData.InstancesToVary =   true;
               Debug.Print("Vary instances? " + LPFeatData.InstancesToVary);

              boolstatus = feat.ModifyDefinition(LPFeatData, swModel,  null);

               // Get and set IInstanceToVaryOptions
              boolstatus = LPFeatData.AccessSelections(swModel,  null);

              swInstOpts = (InstanceToVaryOptions)LPFeatData.GetInstanceToVaryOptions();

               // Set D1 and D2 spacing increments of all pattern instances
              swInstOpts.D1SpacingIncrement = 0.05;
              swInstOpts.D2SpacingIncrement = 0.05;
               Debug.Print("D1 spacing increment is " + swInstOpts.D1SpacingIncrement);
               Debug.Print("D2 spacing increment is " + swInstOpts.D2SpacingIncrement);

               // Get current D1 and D2 modified spacing value for patten instance #3 (2,2)
               Debug.Print("Current D1 modified spacing value for instance #3 is " + swInstOpts.GetD1ModifiedSpacingValue(3));
               Debug.Print("Current D2 modified spacing value for instance #3 is " + swInstOpts.GetD2ModifiedSpacingValue(3));

               // Modify the D1 and D2 spacing value for pattern instance #3 (2,2)
              boolstatus = swInstOpts.ModifyD1SpacingValue(3, swInstOpts.GetD1ModifiedSpacingValue(3) + 0.02);
              boolstatus = swInstOpts.ModifyD2SpacingValue(3, swInstOpts.GetD2ModifiedSpacingValue(3) + 0.02);

               // Get the new D1 and D2 modified spacing value for pattern instance #3 (2,2)
               Debug.Print("New D1 modified spacing value for instance #3 is " + swInstOpts.GetD1ModifiedSpacingValue(3));
               Debug.Print("New D2 modified spacing value for instance #3 is " + swInstOpts.GetD2ModifiedSpacingValue(3));

               // Increment a dimension for all pattern instances in Direction 1
               string[] vIncr1Dims =   new   string[1];
              double[] vIncr1DimValues =   new   double[1];
              vIncr1Dims[0] =   "Near C'Sink Dia.@Sketch2";
              vIncr1DimValues[0] = 0.005;

               object incrDims;
               object incrDimValues;

              swInstOpts.SetD1IncrementDimensions(vIncr1Dims, vIncr1DimValues);
              swInstOpts.GetD1IncrementDimensions(out incrDims,   out incrDimValues);

               // Modify a specific dimension just for pattern instance #3 (2,2)
               string[] vDims =   new   string[1];
               double[] vDimValues =   new   double[1];
              vDims[0] =   "Near C'Sink Dia.@Sketch2";
              vDimValues[0] = 0.02;
              boolstatus = swInstOpts.ModifyDimensions(3, vDims, vDimValues);

              swInstOpts.GetModifiedDimensions(3,   out incrDims,   out incrDimValues);

               // Modify the pattern feature with the instance to vary options
              LPFeatData.SetInstanceToVaryOptions(swInstOpts);
              boolstatus = feat.ModifyDefinition(LPFeatData, swModel,  null);
          }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```

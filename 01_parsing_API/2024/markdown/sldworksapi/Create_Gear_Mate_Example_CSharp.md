---
title: "Create Gear Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Gear_Mate_Example_CSharp.htm"
---

# Create Gear Mate Example (C#)

This example shows how to create a gear mechanical mate.

```vb
  // --------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\MechanicalMates\spurgear.sldasm.
 // 2. Delete GearMate1 from the Mates folder in the FeatureManager design tree.
 //
 // Postconditions: Inspect the Mates folder in the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // --------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateGearMate
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 Part;
         private AssemblyDoc swAssembly;
         private bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;
             swAssembly = (AssemblyDoc)Part;

             boolstatus = Part.Extension.SelectByRay(-0.00560801689982782, -0.00324062886681986, -0.00252602902980925, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000593757005519753, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.0367362652137331, -0.000655599730123413, -0.00290761848191323, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000593757005519753, 2, true, 1, 0);

             // Create GearMateFeatureData
             GearMateFeatureData MateData = (GearMateFeatureData)swAssembly.CreateMateData(10);

             // Set the entities To mate
             object[] EntitiesToMate = new object[2];
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             object EntitiesToMateVar = EntitiesToMate;
             MateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the gear ratio numerator
             MateData.GearRatioNumerator = 0.012954;

             // Set the gear ratio denominator
             MateData.GearRatioDenominator = 0.012954;

             // Set the mate orientation direction
             MateData.Reverse = false;

             // Create the mate
             Feature MateFeature = (Feature)swAssembly.CreateMate(MateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

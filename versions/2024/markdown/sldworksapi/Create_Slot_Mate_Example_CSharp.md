---
title: "Create Slot Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Slot_Mate_Example_CSharp.htm"
---

# Create Slot Mate Example (C#)

This example shows how to create a slot mechanical mate.

```vb
  // --------------------------------------------------------------------------------
 // Preconditions: Open
 // public_documents\samples\tutorial\api\MechanicalMates\slot_slot.sldasm.
 //
 // Postconditions: Inspect the Mates folder of the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // --------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateSlotMate_CSharp
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
             boolstatus = Part.Extension.SelectByRay(0.12649032355856, 0.133857958976421, 0.00879467058769023, 0.0353905007657348, 0.579257713320296, 0.814375843216443, 0.00214371287556113, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.0959257342875013, 0.0999222046038994, -0.0251429018803719, 0.0353905007657348, 0.579257713320296, 0.814375843216443, 0.00214371287556113, 2, true, 1, 0);

             // Create SlotMateFeatureData
             SlotMateFeatureData MateData = (SlotMateFeatureData)swAssembly.CreateMateData(21);

             // Set the entities to mate
             object[] EntitiesToMate = new object[2];
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             object EntitiesToMateVar = EntitiesToMate;
             MateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the mate alignment
             MateData.MateAlignment = 0;

             // Set the mate constraint
             MateData.Constraint = 0;

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

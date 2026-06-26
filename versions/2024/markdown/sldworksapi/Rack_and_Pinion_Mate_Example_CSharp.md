---
title: "Create Rack and Pinion Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rack_and_Pinion_Mate_Example_CSharp.htm"
---

# Create Rack and Pinion Mate Example (C#)

This example shows how to create a rack and pinion mechanical mate.

```vb
  // ------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\MechanicalMates\Rack And Pinion.sldasm.
 // 2. Delete RackPinionMate1 from the Mates folder of the FeatureManager design tree.
 //
 // Postconditions: Inspect the Mates folder in the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateRackPinionMate_CSharp
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

             boolstatus = Part.Extension.SelectByRay(-0.0463518983485187, 0.061012999696942, -0.00642963015610576, -0.398796540128449, 0.236369842894561, -0.886053393962, 0.000798486578462134, 1, true, 64, 0);
             boolstatus = Part.Extension.SelectByRay(0.00790589165686129, -0.00993915877270979, -0.00438167267822109, -0.398796540128449, 0.236369842894561, -0.886053393962, 0.000798486578462134, 2, true, 128, 0);

             // Create RackPinionMateFeatureData
             RackPinionMateFeatureData MateData = (RackPinionMateFeatureData)swAssembly.CreateMateData(13);

             // Set the mate diameter type
             MateData.DiameterType = 0;

             // Set the mate diameter value
             MateData.DiameterVal = 0.0254;

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

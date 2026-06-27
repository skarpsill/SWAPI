---
title: "Create Screw Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Screw_Mate_Example_CSharp.htm"
---

# Create Screw Mate Example (C#)

This example shows how to create a screw mechanical mate.

```vb
  // --------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\MechanicalMates\Gearbox.sldasm.
 // 2. Delete Screw2 from the Mates folder of the FeatureManager design tree.
 //
 // Postconditions: Inspect the Mates folder in the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // --------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateScrewMate_CSharp
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
             boolstatus = Part.Extension.SelectByRay(0.00613295661213442, 0.0689560082602441, 0.0745357419147012, -0.540837135649095, -0.258416475165147, -0.800447448659875, 0.000789884801245894, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(-0.000675539884355203, 0.0795322044607474, 0.0128285894949158, -0.540837135649095, -0.258416475165147, -0.800447448659875, 0.000789884801245894, 1, true, 1, 0);

             // Create ScrewMateFeatureData
             ScrewMateFeatureData MateData = (ScrewMateFeatureData)swAssembly.CreateMateData(17);

             // Set the entities To mate
             object[] EntitiesToMate = new object[2];
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             object EntitiesToMateVar = EntitiesToMate;
             MateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the mate revolution type
             MateData.RevolutionType = 0;

             // Set the mate revolution value
             MateData.RevolutionVal = 1;

             // Set the mate orientation direction
             MateData.Reverse = true;

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

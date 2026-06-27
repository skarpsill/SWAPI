---
title: "Create Hinge Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Hinge_Mate_Example_CSharp.htm"
---

# Create Hinge Mate Example (C#)

This example shows how to create a hinge mechanical mate.

```vb
  // ------------------------------------------------------------------------------------
 // Preconditions: Open
 // public_documents\samples\tutorial\api\MechanicalMates\Hinge-Assy.sldasm.
 //
 // Postconditions: Inspect the Mates folder in the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // -------------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateHingeMate_CSharp
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

             boolstatus = Part.Extension.SelectByRay(0.0343240086878041, 0.0999999999998522, -0.00512270896450673, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 32768, 0);
             boolstatus = Part.Extension.SelectByRay(0.0824118572918451, 0.10000000000008, -0.0468924659023173, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 32768, 0);
             boolstatus = Part.Extension.SelectByRay(0.0182257333177063, 0.0419666144006783, 0, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 65536, 0);
             boolstatus = Part.Extension.SelectByRay(0.0779243258261317, 0.0497185607756023, -0.0384484600391488, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 65536, 0);
             boolstatus = Part.Extension.SelectByRay(0.0533819856866558, 0.0921914939762019, -0.00131731445623018, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.0580246157638271, 0.0700560308736158, -0.0192219802344198, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.000797167289842004, 2, true, 1, 0);

             // Create HingeMateFeatureData
             HingeMateFeatureData MateData = (HingeMateFeatureData)swAssembly.CreateMateData(22);

             // Set the concentric entities to mate
             object[] ConcentricEntitiesToMate = new object[2];
             ConcentricEntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(5, -1);
             ConcentricEntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(6, -1);
             object ConcentricEntitiesToMateVar = ConcentricEntitiesToMate;
             MateData.EntitiesToMate[0] = ConcentricEntitiesToMateVar;

             // Set the coincident entities to mate
             object[] CoincidentEntitiesToMate = new object[2];
             CoincidentEntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             CoincidentEntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             object CoincidentEntitiesToMateVar = CoincidentEntitiesToMate;
             MateData.EntitiesToMate[1] = CoincidentEntitiesToMateVar;

             // Set the mate angle selection
             MateData.AngleSelection = true;

             // Set the angle entities to mate
             object[] AngleEntitiesToMate = new object[2];
             AngleEntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(3, -1);
             AngleEntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(4, -1);
             object AngleEntitiesToMateVar = AngleEntitiesToMate;
             MateData.EntitiesToMate[2] = AngleEntitiesToMateVar;

             // Set the mate angle value
             MateData.Angle = 0.5235987755983;

             // Set the mate angle minimum value
             MateData.MinVal = 0.5235987755983;

             // Set the mate angle maximum value
             MateData.MaxVal = 0.5235987755983;

             // Set the mate alignment
             MateData.MateAlignment = 0;

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

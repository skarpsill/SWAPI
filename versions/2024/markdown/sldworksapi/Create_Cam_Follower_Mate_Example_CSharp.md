---
title: "Create a Cam-Follower Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cam_Follower_Mate_Example_CSharp.htm"
---

# Create a Cam-Follower Mate Example (C#)

This example shows how to create a cam-follower mate.

```vb
  //---------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\MechanicalMates\Cam-Follower.sldasm.
 // 2. Delete CamMateCoincident1 from the Mates folder in the FeatureManager
 //    design tree.
 //
 // Postconditions:
 // Inspect the Mates folder in the FeatureManager design tree.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
  // -----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CamFollowerMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 Part;
         private AssemblyDoc assy;
         private bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;
             assy = (AssemblyDoc)Part;

             boolstatus = Part.Extension.SelectByRay(-0.00229201081452857, 0.0761655216381314, 0.00981125242168446, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.00288013169157359, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0, 0.0762, 0, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.00288013169157359, 3, true, 8, 0);

             // Create CamFollowerMateFeatureData
             CamFollowerMateFeatureData MateData = (CamFollowerMateFeatureData)assy.CreateMateData(9);

             // Set the Entities To Mate
             object FirstEntityToMate = null;
             object SecondEntityToMate = null;
             FirstEntityToMate = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             MateData.EntitiesToMate[0] = FirstEntityToMate;
             SecondEntityToMate = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             MateData.EntitiesToMate[1] = SecondEntityToMate;

             // Set the Mate Alignment
             MateData.MateAlignment = 2;

             // Create the mate
             Feature MateFeature = (Feature)assy.CreateMate(MateData);

             Part.EditRebuild3();
         }
         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

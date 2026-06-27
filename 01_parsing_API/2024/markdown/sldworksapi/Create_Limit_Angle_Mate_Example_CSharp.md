---
title: "Create and Edit Limit Angle Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Limit_Angle_Mate_Example_CSharp.htm"
---

# Create and Edit Limit Angle Mate Example (C#)

This example shows how to create and edit a limit angle advanced mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a limit angle mate.
 // 2. Press F5 to continue.
  // 3. Modifies the mate alignment of the limit angle mate.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace LimitAngleMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private AssemblyDoc swAssy;
         private AngleMateFeatureData swAngleMateData;
         private MateFeatureData swMateData;
         private SelectionMgr swSelMgr;
         private bool boolstatus;
         private Feature feat;
         private Face2[] facesDist = new Face2[2];
         private object vFacesDist;

         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssy = (AssemblyDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swMateData = (MateFeatureData)swAssy.CreateMateData(6); //Angle mate

             Debug.Print("Type of mate as defined in swMateType_e: " + swMateData.TypeName);

             swAngleMateData = (AngleMateFeatureData)swMateData;
             swAngleMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;
             swAngleMateData.FlipDimension = false;
             swAngleMateData.Angle = 0.523599;
             swAngleMateData.MaximumAngle = 0.523599;
             swAngleMateData.MinimumAngle = 0.506145;

             boolstatus = swModel.Extension.SelectByRay(0.00868857956595548, 0.0414144214960288, 0.0633435410960033, -0.520148774728431, -0.59141018013918, -0.616181183562315, 0.000468381592786756, 2, true, 1, 0);
             boolstatus = swModel.Extension.SelectByRay(0.0313565896258297, 0.0296508617577445, 0.0442099188854286, 0.340524666870961, -0.380278973953885, -0.859901653226112, 0.000431713609895031, 2, true, 1, 0);

             facesDist[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             facesDist[1] = (Face2)swSelMgr.GetSelectedObject6(2, -1);

             vFacesDist = facesDist;
             swAngleMateData.EntitiesToMate = vFacesDist;

             feat = (Feature)swAssy.CreateMate(swAngleMateData);

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             feat = swModel.Extension.GetLastFeatureAdded();
             Debug.Print("Feature type created is " + feat.GetTypeName2());

             swMateData = (MateFeatureData)feat.GetDefinition();
             swAngleMateData = (AngleMateFeatureData)swMateData;

             //Change alignment of limit angle mate
             if (swMateData.TypeName == (int)swMateType_e.swMateANGLE)
             {

                 Debug.Print("Angle mate alignment is " + swAngleMateData.MateAlignment);

                 if (swAngleMateData.MateAlignment == (int)swMateAlign_e.swMateAlignALIGNED)
                 {
                     swAngleMateData.MateAlignment = (int)swMateAlign_e.swMateAlignANTI_ALIGNED;
                 }
                 else
                 {
                     swAngleMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;
                 }

                 Debug.Print("Angle mate alignment changed to " + swAngleMateData.MateAlignment);
                 Debug.Print("Angle: " + swAngleMateData.Angle);
                 Debug.Print("Minimum angle: " + swAngleMateData.MinimumAngle);
                 Debug.Print("Maximum angle: " + swAngleMateData.MaximumAngle);
                 Debug.Print("Move entities to opposite sides of the dimension? " + swAngleMateData.FlipDimension);

                 boolstatus = feat.ModifyDefinition(swAngleMateData, swAssy, null);

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

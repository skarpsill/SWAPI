---
title: "Create and Edit Limit Distance Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Limit_Distance_Mate_Example_CSharp.htm"
---

# Create and Edit Limit Distance Mate Example (C#)

This example shows how to create and edit a limit distance mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a limit distance mate.
 // 2. Press F5 to continue.
  // 3. Modifies the mate alignment of the limit distance mate.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace LimitDistanceMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private AssemblyDoc swAssy;
         private DistanceMateFeatureData swDistMateData;
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

             swMateData = (MateFeatureData)swAssy.CreateMateData(5); //Distance mate

             Debug.Print("Type of mate as defined in swMateType_e: " + swMateData.TypeName);

             swDistMateData = (DistanceMateFeatureData)swMateData;
             swDistMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;
             swDistMateData.FlipDimension = false;
             swDistMateData.Distance = 0.0254;
             swDistMateData.MaximumDistance = 0.0254;
             swDistMateData.MinimumDistance = 0.01;

             boolstatus = swModel.Extension.SelectByRay(0.00868857956595548, 0.0414144214960288, 0.0633435410960033, -0.520148774728431, -0.59141018013918, -0.616181183562315, 0.000468381592786756, 2, true, 1, 0);
             boolstatus = swModel.Extension.SelectByRay(0.0313565896258297, 0.0296508617577445, 0.0442099188854286, 0.340524666870961, -0.380278973953885, -0.859901653226112, 0.000431713609895031, 2, true, 1, 0);

             facesDist[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             facesDist[1] = (Face2)swSelMgr.GetSelectedObject6(2, -1);

             vFacesDist = facesDist;

             swDistMateData.EntitiesToMate = vFacesDist;

             feat = (Feature)swAssy.CreateMate(swDistMateData);

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             feat = swModel.Extension.GetLastFeatureAdded();
             Debug.Print("Feature GetTypeName2 of mate created is " + feat.GetTypeName2());

             swMateData = (MateFeatureData)feat.GetDefinition();

             if (swMateData.TypeName == (int)swMateType_e.swMateDISTANCE)
             {

                 swDistMateData = (DistanceMateFeatureData)swMateData;
                 Debug.Print("Distance mate alignment is " + swDistMateData.MateAlignment);

                 if (swDistMateData.MateAlignment == (int)swMateAlign_e.swMateAlignALIGNED)
                 {
                     swDistMateData.MateAlignment = (int)swMateAlign_e.swMateAlignANTI_ALIGNED;
                 }
                 else
                 {
                     swDistMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;
                 }

                 Debug.Print("Distance mate alignment changed to " + swDistMateData.MateAlignment);
                 Debug.Print("Distance: " + swDistMateData.Distance);
                 Debug.Print("Minimum distance: " + swDistMateData.MinimumDistance);
                 Debug.Print("Maximum distance: " + swDistMateData.MaximumDistance);
                 Debug.Print("Move entities to opposite sides of the dimension? " + swDistMateData.FlipDimension);

                 boolstatus = feat.ModifyDefinition(swDistMateData, swAssy, null);

             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

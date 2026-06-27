---
title: "Create and Edit Width Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Width_Mate_Example_CSharp.htm"
---

# Create and Edit Width Mate Example (C#)

This example shows how to create and edit a width mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Creates a width mate of constraint type, dimension.
 // 2. Press F5 to continue.
  // 3. Changes the width mate to constraint type, percent.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace WidthMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private AssemblyDoc swAssy;
         private WidthMateFeatureData swWidthMateData;
         private MateFeatureData swMateData;
         private SelectionMgr swSelMgr;
         private bool boolstatus;
         private Feature feat;
         private Face2[] faceTab = new Face2[2];
         private Face2[] facesWidth = new Face2[2];
         private object vFacesTab;
         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssy = (AssemblyDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swMateData = (MateFeatureData)swAssy.CreateMateData(11); //Width mate

             if (swMateData.TypeName == (int)swMateType_e.swMateWIDTH)
             {

                 swWidthMateData = (WidthMateFeatureData)swMateData;
                 swWidthMateData.ConstraintType = (int)swMateWidthOptions_e.swMateWidth_Dimension;

                 Debug.Print("Width Mate Constraint Type is " + swWidthMateData.ConstraintType);

                 // Select faces for the width and tab of this width mate
                 boolstatus = swModel.Extension.SelectByRay(0.00868857956595548, 0.0414144214960288, 0.0633435410960033, -0.520148774728431, -0.59141018013918, -0.616181183562315, 0.000468381592786756, 2, true, 1, 0);
                 boolstatus = swModel.Extension.SelectByRay(0.040068521476087, 0.0399799509449394, 0.0585753748188154, 0.320596315934938, -0.422312467890091, -0.847862124212143, 0.000468381592786756, 2, true, 1, 0);
                 boolstatus = swModel.Extension.SelectByRay(0.0313565896258297, 0.0296508617577445, 0.0442099188854286, 0.340524666870961, -0.380278973953885, -0.859901653226112, 0.000431713609895031, 2, true, 16, 0);
                 boolstatus = swModel.Extension.SelectByRay(0.0267766714922573, 0.0259424893815421, 0.0380784753310763, -0.849725692314326, -0.107993323108602, 0.516046209156602, 0.000431713609895031, 2, true, 16, 0);

                 facesWidth[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
                 facesWidth[1] = (Face2)swSelMgr.GetSelectedObject6(2, -1);

                 object vFacesWidth = facesWidth;

                 swWidthMateData.WidthSelection = vFacesWidth;

                 faceTab[0] = (Face2)swSelMgr.GetSelectedObject6(3, -1);
                 faceTab[1] = (Face2)swSelMgr.GetSelectedObject6(4, -1);

                 vFacesTab = faceTab;

                 swWidthMateData.TabSelection = (vFacesTab);

                 if (swWidthMateData.ConstraintType == (int)swMateWidthOptions_e.swMateWidth_Dimension)
                 {
                     swWidthMateData.DistanceFromEnd = 0.04975511004;
                     swWidthMateData.FlipDimension = true;
                 }

                 feat = (Feature)swAssy.CreateMate(swWidthMateData);

             }

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             feat = swModel.Extension.GetLastFeatureAdded();

             swMateData = (MateFeatureData)feat.GetDefinition();

             if (swMateData.TypeName == (int)swMateType_e.swMateWIDTH)
             {
                 swWidthMateData = (WidthMateFeatureData)swMateData;

                 swWidthMateData.ConstraintType = (int)swMateWidthOptions_e.swMateWidth_Percent;
                 swWidthMateData.PercentDistanceFromEnd = 47;
                 swWidthMateData.FlipDimension = false;
                 Debug.Print("Width mate constraint type changed to " + swWidthMateData.ConstraintType);
                 Debug.Print("Distance from the end of this width mate: " + swWidthMateData.DistanceFromEnd);
                 Debug.Print("Percentage of distance from the end of this width mate: " + swWidthMateData.PercentDistanceFromEnd);
                 Debug.Print("Move entities to opposite sides of the dimension? " + swWidthMateData.FlipDimension);

                 boolstatus = feat.ModifyDefinition(swWidthMateData, swAssy, null);

             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

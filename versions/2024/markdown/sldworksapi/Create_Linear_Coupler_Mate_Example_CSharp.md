---
title: "Create and Edit Linear-Linear Coupler Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Coupler_Mate_Example_CSharp.htm"
---

# Create and Edit Linear-Linear Coupler Mate Example (C#)

This example shows how to create and edit a linear/linear coupler mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo4.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a linear/linear coupler mate.
 // 2. Press F5 to continue.
 // 3. Changes the reverse property of the mate.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace LinearCouplerMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private AssemblyDoc swAssy;
         private LinearCouplerMateFeatureData swLinearMateData;
         private MateFeatureData swMateData;
         private SelectionMgr swSelMgr;
         private bool boolstatus;
         private Feature feat;
         private Face2[] facesLC = new Face2[2];
         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssy = (AssemblyDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swMateData = (MateFeatureData)swAssy.CreateMateData(18); //Linear/linear coupler mate

             if (swMateData.TypeName == (int)swMateType_e.swMateLINEARCOUPLER)
             {

                 swLinearMateData = (LinearCouplerMateFeatureData)swMateData;

                 swLinearMateData.CouplerRatioNumerator = 0.00099;
                 Debug.Print("Linear/linear coupler ratio numerator is " + swLinearMateData.CouplerRatioNumerator);

                 swLinearMateData.CouplerRatioDenominator = 0.00199;
                 Debug.Print("Linear/linear coupler ratio denominator is " + swLinearMateData.CouplerRatioDenominator);

                 swLinearMateData.Reverse = false;

                 boolstatus = swModel.Extension.SelectByRay(-0.0805427342211829, 0.00068649651763053, 0.0119585811536354, 0.722099295067451, -0.530192163929043, -0.44437470379324, 0.00135613437918167, 2, false, 0, 0);
                 boolstatus = swModel.Extension.SelectByRay(-0.0435951139756412, -0.00915195091067744, 0.0234497167883774, 0.722099295067451, -0.530192163929043, -0.44437470379324, 0.00135613437918167, 2, true, 0, 0);

                 facesLC[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
                 facesLC[1] = (Face2)swSelMgr.GetSelectedObject6(2, -1);

                 object vFacesLC = facesLC;

                 swLinearMateData.MateEntity1 = facesLC[0];
                 swLinearMateData.MateEntity2 = facesLC[1];

                 feat = (Feature)swAssy.CreateMate(swLinearMateData);

             }

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             feat = swModel.Extension.GetLastFeatureAdded();

             Debug.Print("Feature GetTypeName2 of mate created is " + feat.GetTypeName2());

             swMateData = (MateFeatureData)feat.GetDefinition();

             if (swMateData.TypeName == (int)swMateType_e.swMateLINEARCOUPLER)
             {

                 swLinearMateData = (LinearCouplerMateFeatureData)swMateData;

                 Debug.Print("Linear/linear coupler mate reverse is " + swLinearMateData.Reverse);

                 if (swLinearMateData.Reverse == true)
                 {
                     swLinearMateData.Reverse = false;
                 }
                 else
                 {
                     swLinearMateData.Reverse = true;
                 }

                 Debug.Print("Linear/linear coupler mate reverse changed to " + swLinearMateData.Reverse);

                 boolstatus = feat.ModifyDefinition(swLinearMateData, swAssy, null);

             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

---
title: "Create and Edit Profile Center Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Profile_Center_Mate_Example_CSharp.htm"
---

# Create and Edit Profile Center Mate Example (C#)

This example shows how to create and edit a profile center mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo2.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a profile center mate.
 // 2. Press F5 to continue.
 // 3. Changes the mate alignment of the mate.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace ProfileCenterMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private AssemblyDoc swAssy;
         private ProfileCenterMateFeatureData swProfileMateData;
         private MateFeatureData swMateData;
         private SelectionMgr swSelMgr;
         private bool boolstatus;
         private Feature feat;
         private Face2[] facesPC = new Face2[2];
         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssy = (AssemblyDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swMateData = (MateFeatureData)swAssy.CreateMateData(24); //Profile center mate

             if (swMateData.TypeName == (int)swMateType_e.swMatePROFILECENTER)
             {

                 swProfileMateData = (ProfileCenterMateFeatureData)swMateData;

                 swProfileMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;
                 Debug.Print("Profile Center mate alignment is " + swProfileMateData.MateAlignment);

                 swProfileMateData.FlipDimension = false;
                 Debug.Print("ProfileCenter flip dimension is " + swProfileMateData.FlipDimension);

                 swProfileMateData.LockRotation = false;
                 Debug.Print("Profile center mate lock rotation is " + swProfileMateData.LockRotation);

                 swProfileMateData.OffsetDistance = 0.0254;
                 Debug.Print("Profile center mate offset distance is " + swProfileMateData.OffsetDistance);

                 boolstatus = swModel.Extension.SelectByRay(0.0152510997612296, 0.0525002489357007, 0.132234612849345, -0.271844060659921, -0.167859116984408, -0.947588583473408, 0.000708485696755524, 2, true, 1, 0);
                 boolstatus = swModel.Extension.SelectByRay(0.136053581313973, 0.0198237342244454, 0.0953905211266601, -0.30846884126036, 0.319767565972896, -0.895877043864425, 0.000708485696755524, 2, false, 0, 0);

                 facesPC[0] = (Face2)swSelMgr.GetSelectedObject6(1, -1);
                 facesPC[1] = (Face2)swSelMgr.GetSelectedObject6(2, -1);

                 object vFacesPC = facesPC;

                 swProfileMateData.EntitiesToMate = vFacesPC;

                 feat = (Feature)swAssy.CreateMate(swProfileMateData);

             }

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             feat = swModel.Extension.GetLastFeatureAdded();

             Debug.Print("Feature GetTypeName2 of mate created is " + feat.GetTypeName2());
             swMateData = (MateFeatureData)feat.GetDefinition();

             if (swMateData.TypeName == (int)swMateType_e.swMatePROFILECENTER)
             {
                 swProfileMateData = (ProfileCenterMateFeatureData)swMateData;

                 Debug.Print("Profile center mate alignment is " + swProfileMateData.MateAlignment);

                 if (swProfileMateData.MateAlignment == (int)swMateAlign_e.swMateAlignALIGNED)
                 {
                     swProfileMateData.MateAlignment = (int)swMateAlign_e.swMateAlignANTI_ALIGNED;
                 }
                 else
                 {
                     swProfileMateData.MateAlignment = (int)swMateAlign_e.swMateAlignALIGNED;

                 }

                 Debug.Print("Profile center mate alignment changed to " + swProfileMateData.MateAlignment);

                 boolstatus = feat.ModifyDefinition(swProfileMateData, swAssy, null);

             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

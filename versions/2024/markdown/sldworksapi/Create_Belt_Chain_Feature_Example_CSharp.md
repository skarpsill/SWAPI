---
title: "Create Belt/Chain Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Belt_Chain_Feature_Example_CSharp.htm"
---

# Create Belt/Chain Feature Example (C#)

This example shows how to create a Belt/Chain assembly feature.

```vb
 // =====================================================================
 // Preconditions: Ensure the specified assembly template and part exist.
 //
 // Postconditions:
 // 1. Creates an assembly of two steel discs.
 // 2. Press F5 to create Belt1 in the FeatureManager design tree.
 //    If a Save As dialog appears, click Cancel.
 // 3. Modifies Belt1's belt length, belt thickness,
 //    and pulley diameters. If a Save As dialog appears, click Cancel.
 // ============================================================
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace Macro1_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
          public   DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
           {
               int ArraySize;
              ArraySize = Objects.GetUpperBound(0);
               var d =  new  DispatchWrapper[ArraySize + 1];
               int ArrayIndex;
               var loopTo = ArraySize;
               for (ArrayIndex = 0; ArrayIndex <= loopTo; ArrayIndex++)
                  d[ArrayIndex] =   new   DispatchWrapper(Objects[ArrayIndex]);
               return d;
           }
            public  void Main()
           {
               ModelDoc2 swModel;
               SelectionMgr selMgr;
               BeltChainFeatureData beltChainFeatData;
               var pulleyComps =   new   object[2];
               var pulleyDiams =   new   double[2];
               var pullyFlips =   new   bool[2];
              var pulleyDiamsOri =   new   double[2];
               Feature swFeat;
               BeltChainFeatureData swFeatData;
               int I;
               int J;
               bool boolstatus;
               var longwarnings =   default(int);
               double swSheetWidth;
              swSheetWidth = 0d;
               double swSheetHeight;
              swSheetHeight = 0d;
              swModel = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight);
               AssemblyDoc swAssembly;
              swAssembly = (AssemblyDoc)swModel;

               // Insert steel disc component

               string AssemblyTitle;
              AssemblyTitle = swModel.GetTitle();
               ModelDoc2 tmpObj;
               var errors =  default(int);
              tmpObj = swApp.OpenDoc6(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1,   "", errors, longwarnings);
              swModel = (ModelDoc2)swApp.ActivateDoc3(AssemblyTitle,   true, 0,   ref errors);
               Component2 swInsertedComponent;
              swInsertedComponent = ((AssemblyDoc)swModel).AddComponent5(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0,   "",   false,   "", 0.00404421078452853d, 0.00404421078422676d, 0.0122628871084471d);
              swApp.CloseDoc(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt");

               // Insert steel disc component

              AssemblyTitle = swModel.GetTitle();
              tmpObj = swApp.OpenDoc6(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1,   "", errors, longwarnings);
              swModel = (ModelDoc2)swApp.ActivateDoc3(AssemblyTitle,   true, 0, errors);
              swInsertedComponent = ((AssemblyDoc)swModel).AddComponent5(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0,   "",   false,   "", 0.0200044210784528d, 0.0200044210784227d, 0.0122628871084471d);
              swApp.CloseDoc(@"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt");

               // Float the components

              boolstatus = swModel.Extension.SelectByID2("steel disc-1",  "COMPONENT", 0, 0, 0,   false, 0,   null, 0);
               //swModel.UnfixComponent();
              swModel.ClearSelection2(true);
              boolstatus = swModel.Extension.SelectByID2("steel disc-2",   "COMPONENT", 0, 0, 0,   false, 0,   null, 0);
               //swModel.UnfixComponent();
              swModel.ClearSelection2(true);

               // Move one disc

              boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14",   "COMPONENT", 0, 0, 0,   false, 0,   null, 0);
              boolstatus = swModel.Extension.SelectByID2("Unknown",  "MANIPULATOR", 0.0340009836225566d, -0.00352899570186584d, -0.0115173288530189d,   false, 0,   null, 0);
              swModel.ClearSelection2(true);
              boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14",   "COMPONENT", 0, 0, 0,   false, 0,   null, 0);
               var TransformData =   new   double[16];
              TransformData[0] = 1d;
              TransformData[1] = 0d;
              TransformData[2] = 0d;
              TransformData[3] = 0d;
              TransformData[4] = 1d;
              TransformData[5] = 0d;
              TransformData[6] = 0d;
              TransformData[7] = 0d;
              TransformData[8] = 1d;
              TransformData[9] = 0.0664528131333411d;
              TransformData[10] = 0.0046349356621274d;
              TransformData[11] = 0.00919716533133533d;
              TransformData[12] = 1d;
              TransformData[13] = 0d;
              TransformData[14] = 0d;
              TransformData[15] = 0d;
               object TransformDataVariant;
              TransformDataVariant = TransformData;
               MathUtility swMathUtil;
              swMathUtil = (MathUtility)swApp.GetMathUtility();
               MathTransform swTransForm;
              swTransForm = (MathTransform)swMathUtil.CreateTransform(TransformDataVariant);
               Component2 swComp;
              swComp = (Component2)((SelectionMgr)swModel.SelectionManager).GetSelectedObjectsComponent4(1, -1);
              boolstatus = swComp.SetTransformAndSolve2(swTransForm);
              boolstatus = swModel.ForceRebuild3(false);
              swModel.ClearSelection2(true);

               // Select the pulley faces

              boolstatus = swModel.Extension.SelectByRay(0.0130157615084272d, 0.00990176398499898d, 0.0121640119419908d, -0.333333333266778d, -0.333333333254022d, -0.881917103743329d, 0.000973554376657825d, 2,  false, 0, 0);
              boolstatus = swModel.Extension.SelectByRay(0.0769710902559098d, 0.00667589089525222d, 0.0112969076145077d, -0.333333333266778d, -0.333333333254022d, -0.881917103743329d, 0.000973554376657825d, 2,  false, 0, 0);
              selMgr = (SelectionMgr)swModel.SelectionManager;
               var loopTo = pulleyComps.GetUpperBound(0);
               for (I = 0; I <= loopTo; I++)
                  pulleyComps[I] = selMgr.GetSelectedObject6(I + 1, -1);

               // Create Belt/Chain feature

              beltChainFeatData = (BeltChainFeatureData)swModel.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmBeltAndChain);
               var loopTo1 = pulleyComps.GetUpperBound(0);
               for (J = 0; J <= loopTo1; J++)
                  pulleyDiams[J] = 0.005d * (J + 2);

               DispatchWrapper[] dArray;
              dArray = ObjectArrayToDispatchWrapperArray(pulleyComps);
              beltChainFeatData.PulleyComponents = dArray;
              beltChainFeatData.PulleyDiameters = pulleyDiams;
              pullyFlips[0] =   false;
              pullyFlips[1] =   false;
              beltChainFeatData.FlipSides = pullyFlips;
              beltChainFeatData.BeltLocationPlane = selMgr.GetSelectedObject6(3, -1);
              beltChainFeatData.DrivingLength =   true;
              beltChainFeatData.BeltLength = 0.59492d;
              beltChainFeatData.UseBeltThickness =   true;
              beltChainFeatData.BeltThickness = 0.003d;
              beltChainFeatData.CreateBeltPart =   true;
              beltChainFeatData.EngageBelt =   false;
               Debugger.Break();
              swFeat = swModel.FeatureManager.CreateFeature(beltChainFeatData);
              swFeatData = (BeltChainFeatureData)swFeat.GetDefinition();

               // Modify Belt/Chain feature

              boolstatus = swFeatData.AccessSelections(swModel,  null);
              pulleyDiamsOri = (double[])swFeatData.PulleyDiameters;
              pulleyDiamsOri[0] = 0.02d;
              pulleyDiamsOri[1] = 0.02d;
              swFeatData.PulleyDiameters = pulleyDiamsOri;
               Debug.Print("Pulley diameters changed to 20 mm");
              swFeatData.DrivingLength =   true;
              swFeatData.BeltLength = 0.3d;
               Debug.Print("Belt length (m) changed to " + swFeatData.BeltLength);
              swFeatData.BeltThickness = 0.002d;
               Debug.Print("Belt thickness (m) changed to " + swFeatData.BeltThickness);
              boolstatus = swFeat.ModifyDefinition(swFeatData, swModel,  null);
           }

            // The SldWorks swApp variable is pre-assigned for you.
            public  SldWorks swApp;

      }
 }
```

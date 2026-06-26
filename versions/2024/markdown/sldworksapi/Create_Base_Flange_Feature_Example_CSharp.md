---
title: "Create Base Flange Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Base_Flange_Feature_Example_CSharp.htm"
---

# Create Base Flange Feature Example (C#)

This example shows how to create a base flange feature.

```vb
 // ===========================================================
 // Preconditions:
 // 1. Ensure the specified part template exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates a flange profile sketch.
 // 2. Creates Base-Flange1 in the FeatureManager design tree.
 // 3. Inspect the Immediate window, graphics area,
 // and FeatureManager design tree.
 // ==================================================

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace Macro1_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            private  ModelDoc2 Part;
            private  PartDoc swPart;
            private  ModelDoc2 swModel;
            private  Feature swSKFeat;
            private  SketchSegment skSegment;
            private  BaseFlangeFeatureData swBaseFlangeFeat;
            private  BaseFlangeFeatureData baseFlangeFeatData;
            private  CustomBendAllowance cba;
            private  object[] var;
            private  Feature parent;
            private  Feature SHFeat;
            private  SheetMetalFeatureData smFeatData;
            private  CustomBendAllowance cba1;
            private  bool boolstatus;

            public  void Main()
           {
              Part = (ModelDoc2)swApp.ActiveDoc;
               double swSheetWidth;
              swSheetWidth = 0d;
               double swSheetHeight;
              swSheetHeight = 0d;
              Part = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight);
              swPart = (PartDoc)Part;
              swModel = (ModelDoc2)swApp.ActiveDoc;
              boolstatus = Part.Extension.SelectByID2("Top",  "PLANE", -0.0598881514598713d, 0.0393749830258702d, 0.00485137895479469d,   false, 0,   null, 0);
              Part.SketchManager.InsertSketch(true);
              Part.ClearSelection2(true);
              skSegment = Part.SketchManager.CreateLine(-0.140779d, 0.050824d, 0d, -0.106481d, -0.06735d, 0d);
              skSegment = Part.SketchManager.CreateLine(-0.106481d, -0.06735d, 0d, 0.084966d, -0.049265d, 0d);
              skSegment = Part.SketchManager.CreateLine(0.084966d, -0.049265d, 0d, 0.143274d, 0.063608d, 0d);
              Part.ClearSelection2(true);
              Part.SketchManager.InsertSketch(true);
              swSKFeat = (Feature)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);
               Debug.Print("Flange profile name : " + swSKFeat.Name +  " and type : " + swSKFeat.GetTypeName2());
              swBaseFlangeFeat = (BaseFlangeFeatureData)swModel.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmBaseFlange);
              cba = (CustomBendAllowance)swBaseFlangeFeat.GetCustomBendAllowance();
              cba.Type = (int)swBendAllowanceTypes_e.swBendAllowanceDirect;
              cba.BendAllowance = 0.05d;
              swBaseFlangeFeat.D1EndConditionType = 1;
              swBaseFlangeFeat.D1EndConditionDistance = 0.02d;
              swBaseFlangeFeat.ReverseDirection =   true;
              swBaseFlangeFeat.OffsetDirections = 2;
              swBaseFlangeFeat.D2EndConditionType = 1;
              swBaseFlangeFeat.D2EndConditionDistance = 0.05d;
              swBaseFlangeFeat.OverrideDefaultSheetMetalParameters =   true;
              swBaseFlangeFeat.Thickness = 0.035d;

               // Initialize the base flange feature
               // Initialize(
               // UseMaterialSheetMetalParameters=False,
               // UseDefaultBendAllowance=False,
               // CustomBendAllowance,
               // UseDefaultBendRelief=False,
               // ReliefType=swSheetMetalReliefTypes_e.swSheetMetalReliefRectangular,
               // UseReliefRatio=True,
               // ReliefRatio=0.8m,
               // ReliefWidth,
               // ReliefDepth)

              swBaseFlangeFeat.Initialize(false,   false, cba,   false, (int)swSheetMetalReliefTypes_e.swSheetMetalReliefRectangular,   true, 0.8d, 0d, 0d);
              SHFeat = swModel.FeatureManager.CreateFeature(swBaseFlangeFeat);
              baseFlangeFeatData = (BaseFlangeFeatureData)SHFeat.GetDefinition();
              Debug.Print("Use material sheet metal parameters? " + baseFlangeFeatData.UseMaterialSheetMetalParameters);
               Debug.Print("Use default bend allowance? " + baseFlangeFeatData.UseDefaultBendAllowance);
               Debug.Print("Use default bend relief? " + baseFlangeFeatData.UseDefaultBendRelief);
               Debug.Print("Use relief ratio? " + baseFlangeFeatData.UseReliefRatio);
               Debug.Print("Relief type as defined by swSheetMetalReliefTypes_e: " + baseFlangeFeatData.ReliefType);
              Debug.Print("Relief width: " + baseFlangeFeatData.ReliefWidth);
               Debug.Print("Relief depth: " + baseFlangeFeatData.ReliefDepth);
                Debug.Print("Relief ratio: " + baseFlangeFeatData.ReliefRatio);

               // Modify the relief ratio and override default AutoRelief in the parent sheet metal feature
              var = (object[])SHFeat.GetParents();
              parent = (Feature)var[1];
               Debug.Print("Parent type: " + parent.GetTypeName2());
              smFeatData = (SheetMetalFeatureData)parent.GetDefinition();
              cba1 = smFeatData.GetCustomBendAllowance();
               Debug.Print("Custom bend allowance type as defined in swBendAllowanceTypes_e: " + cba1.Type);
               Debug.Print("Bend allowance: " + cba1.BendAllowance);
               Debug.Print("Result code for override of AutoRelief as defined by swSheetMetalModifierError_e: " + smFeatData.SetOverrideDefaultParameter2((int)swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief,   true));
              smFeatData.ReliefRatio = 0.7d;
               Debug.Print("Base flange successfully modified? " + parent.ModifyDefinition(smFeatData, swModel,  null));
               Debug.Print("Base flange feature name : " + SHFeat.Name +  " and type : " + SHFeat.GetTypeName2());
           }

            // The SldWorks swApp variable is pre-assigned for you.
            public  SldWorks swApp;

      }
 }
```

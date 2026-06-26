---
title: "Create Fill Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Fill_Pattern_Example_CSharp.htm"
---

# Create Fill Pattern Example (C#)

This example shows how to create a Fill Pattern feature and get its data.

```vb
  //--------------------------------------------------------------------------
  // Preconditions: Ensure the specified part exists.
 //
 // Postconditions:
  // 1. Extrudes a hole in the middle of the block.
  // 2. Creates a circular fill pattern of the specified hole.
 // 3. Inspect the graphics area and the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateFillPattern_CSharp
 {
     partial class SolidWorksMacro
     {

         private Feature myFeature;
         private Feature swFeat;
         private FeatureManager swFeatMgr;
         private ModelDoc2 Part;
         private FillPatternFeatureData swFeatData;
         private bool boolstatus;

         public void Main()
         {

             int longstatus = 0;
             int longwarnings = 0;
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", longstatus, longwarnings);
             swApp.ActivateDoc2("block20.sldprt", false, longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("", "", -0.0032, 0.0418, 0.0, false, 0, null, 0);
             myFeature = Part.FeatureManager.SimpleHole2(0.0054, true, false, false, 1, 0, 0.0254, 0.0254, false, false, false, false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true, true, false);
             ((SelectionMgr)(Part.SelectionManager)).EnableContourSelection = false;
             Part.ActivateSelectedFeature();

             boolstatus = Part.Extension.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);
             boolstatus = Part.Extension.SelectByRay(0.00106119575008097, 0.039624, 0.0493456023787655, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.0011224765174324, 1, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.0636836165047043, 0.0396239999998329, -0.000633171793538168, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.0011224765174324, 2, true, 16384, 0);

             swFeatMgr = Part.FeatureManager;

             swFeatData = (FillPatternFeatureData)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmFillPattern);
             swFeatData.CreateSeedCutPolygonSides = 0;
             swFeatData.CreateSeedCutType = 0;
             swFeatData.Diagonal = 0.008;
             swFeatData.Diameter = 0.008;
             swFeatData.Dimension = 0.00565685424949238;
             swFeatData.FeaturesToPatternType = 0;
             swFeatData.GeometryPattern = false;
             swFeatData.InnerRadius = 0.00380422606518061;
             swFeatData.InstanceSpacing = 0.0170240490494193;
             swFeatData.LayoutSpacingType = 1;
             swFeatData.LoopSpacing = 0.0170240490494193;
             swFeatData.Margins = 0;
             swFeatData.NoOfInstances = 10;
             swFeatData.OuterRadius = 0.004;
             swFeatData.PatternLayoutPolygonSides = 0;
             swFeatData.PatternLayoutType = 0;
             swFeatData.Rotation = 0;
             swFeatData.SeedCutFlipShapeDirection = false;
             swFeatData.StaggerAngle = 1.0471975511966;
             swFeat = swFeatMgr.CreateFeature(swFeatData);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

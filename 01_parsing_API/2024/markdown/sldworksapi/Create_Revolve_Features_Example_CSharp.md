---
title: "Create Revolve Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Revolve_Features_Example_CSharp.htm"
---

# Create Revolve Features Example (C#)

This example shows how to create revolve features.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a new part document.
 // 2. Rename the namespace to match your C# project.
 //
 // Postconditions: Two revolve features and one cut-revolve feature are created.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace FeatureRevolves_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         FeatureManager swFeatMgr;
         SelectionMgr swSelMgr;

         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Create an axis
             boolstatus = swModelDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0, true, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             boolstatus = swModelDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0, true, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             swModel.InsertAxis2(true);

             // Create a rectangle
             boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", -0.08954836342753, 0.0004336873289503, 0.006720765739942,  false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             swModel.InsertSketch2(true);
             swModel.ClearSelection2(true);
             swModel.SketchRectangle(-0.05668466821757, -0.02198379306525, 0, -0.01330857427717, 0.03972855876814, 0,  true);

             // Create the first revolve feature
             swModel.InsertSketch2(true);
             swModel.ShowNamedView2("*Trimetric", 8);

             boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             boolstatus = swModelDocExt.SelectByID2("Axis1", "AXIS", 0, 0, 0, true, 16, null, (int)swSelectOption_e.swSelectOptionDefault);
             swFeatMgr = swModel.FeatureManager;

             swFeatMgr.FeatureRevolve2(true, true, false, false, false, false, 0, 0, 6.28318530718, 0, false,
             false, 0.01, 0.01, 0, 0, 0, true, true, true);

             // Create a cut-revolve feature using a face on the revolve feature
             swSelMgr.EnableContourSelection = false;
             boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.03095803920934, 0.01509536510872, 0.02198379306526,  false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             swModel.InsertSketch2(true);
             swModel.ClearSelection2(true);
             swModel.SketchRectangle(-0.04194874421597, 0.01774859621099, 0, -0.01883036471929, -0.01265654504095, 0,  true);
             swModel.InsertSketch2(true);

             boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             boolstatus = swModelDocExt.SelectByID2("Line4@Sketch2", "EXTSKETCHSEGMENT", -0.01883036471929, 0.003802500010693, 0,  true, 4, null, (int)swSelectOption_e.swSelectOptionDefault);
             swFeatMgr.FeatureRevolveCut(6.26573201466,  false, 0, 0, 0, true, true);

             // Create the second revolve feature using a face on the first revolve feature
             swSelMgr.EnableContourSelection = false;
             boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02333512246603, 0.03472018719853, 0.0219837930652,  false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             swModel.InsertSketch2(true);
             swModel.ClearSelection2(true);
             swModel.CreateCircle2(-0.02232361399104, 0.03354683337932, 0, -0.01445073476016, 0.02795861773112, 0);
             swModel.InsertSketch2(true);

             boolstatus = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
             boolstatus = swModelDocExt.SelectByRay(-1.81956067901865E-02, 1.80455411334037E-02, 2.17820530671702E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 9.91972972972973E-04, 1, False, 4, 0);
             swFeatMgr.FeatureRevolve2(true, true, false, false, false, false, 0, 0, 6.28318530718, 0, false,
             false, 0.01, 0.01, 0, 0, 0, true, true, true);
             swSelMgr.EnableContourSelection =  false;

         }

         public SldWorks swApp;

     }
 }
```

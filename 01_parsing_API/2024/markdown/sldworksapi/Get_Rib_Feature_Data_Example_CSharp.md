---
title: "Get Rib Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Rib_Feature_Data_Example_CSharp.htm"
---

# Get Rib Feature Data Example (C#)

This example shows how to get rib feature data.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the part document.
 // 2. Creates Shell1, Plane1, and Rib1.
 // 3. Inspect the FeatureManager design tree, the graphics area, and the
 //    Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertRib_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         RefPlane myRefPlane;
         SketchSegment skSegment;
         SelectionMgr swSelMgr;
         Feature swFeat;
         RibFeatureData2 swRibFeat;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("block20", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00878816842651986, 0.0396239999998897, -0.0292468281514857, false, 1, null, 0);
             Part.InsertFeatureShell(0.00254, false);

             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.00264031138414111, 0.028407059059532, -0.0613970439424634, true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.059937899786064, 0.0277866864457792, -0.00877977980189826, true, 1, null, 0);

             myRefPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(128, 0, 128, 0, 0, 0);
             Part.ClearSelection2(true);

             boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0.00664896553058725, 0.109417877974863, 0.0524178648701081, false, 0, null, 0);
             Part.SketchManager.InsertSketch(true);

             skSegment = Part.SketchManager.CreateLine(-0.085797, 0.021082, 0.0, -0.03423, 0.035134, 0.0);
             skSegment = Part.SketchManager.CreateLine(-0.03423, 0.035134, 0.0, 0.007726, 0.025357, 0.0);
             skSegment = Part.SketchManager.CreateLine(0.007726, 0.025357, 0.0, 0.111514, 0.039624, 0.0);
             Part.ClearSelection2(true);

             Part.SketchManager.InsertSketch(true);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
             Part.FeatureManager.InsertRib(true, false, 0.00254, 0, false, false, true, 0.0174532925199433, false, false);

             swSelMgr = (SelectionMgr)Part.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swRibFeat = (RibFeatureData2)swFeat.GetDefinition();

             Debug.Print("Rib feature type as defined in swRibType_e: " + swRibFeat.Type);
             Debug.Print("Thickness: " + swRibFeat.Thickness);
             Debug.Print("Extrusion direction as defined in swRibExtrusionDirection_e: " + swRibFeat.ExtrusionDirection);
             Debug.Print("Rib has a draft? " + swRibFeat.EnableDraft);
             if (swRibFeat.EnableDraft)
             {
                 Debug.Print("    Draft angle: " + swRibFeat.DraftAngle);
                 Debug.Print("    Draft outward? " + swRibFeat.DraftOutward);
             }
             Debug.Print("Add material to reverse side of the rib? " + swRibFeat.FlipSide);
             Debug.Print("Rib is extruded on two sides of the midplane? " + swRibFeat.IsTwoSided);
             if (!swRibFeat.IsTwoSided)
             {
                 Debug.Print("Single-sided rib is extruded on the reverse side? " + swRibFeat.ReverseThicknessDir);
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

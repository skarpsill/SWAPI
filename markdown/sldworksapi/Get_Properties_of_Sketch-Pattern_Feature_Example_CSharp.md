---
title: "Get Properties of Sketch Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Properties_of_Sketch-Pattern_Feature_Example_CSharp.htm"
---

# Get Properties of Sketch Pattern Feature Example (C#)

This example shows how to get the properties of a sketch pattern feature.

```vb
  //----------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Boss-Extrude2, Sketch3, and Sketch-Pattern1.
 // 2. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateSketchDrivenPattern_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature myFeature;
         SketchPatternFeatureData swSketchPatt;
         double[] vBasePt;
         object skPoint;
         object vSkLines;
         Sketch swSketch;
         Feature swSketchFeat;
         MathTransform swPatternTransform;
         bool boolstatus;
         int i;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("block20", false, ref longstatus);

             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0407921768468213, 0.0396239999998329, -0.0402814031592129, false, 0, null, 0);
             boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
             boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0518589252521906, 0.0451811131877662, 0, -0.0357471289475484, 0.0286242963995278, 0);
             Part.SketchManager.InsertSketch(true);

             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 4, null, 0);
             myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
             0, 0, false);

             Part.SketchManager.InsertSketch(true);
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00770328176440671, 0.0396239999998897, -0.00762437790422155, false, 0, null, 0);
             skPoint = Part.SketchManager.CreatePoint(-0.00527, 0.051345, 0.0);
             skPoint = Part.SketchManager.CreatePoint(-0.005854, 0.025783, 0.0);
             skPoint = Part.SketchManager.CreatePoint(-0.005888, -9E-06, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.019408, 0.051285, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.019093, 0.024628, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.019629, -0.000148, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.043756, 0.051962, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.043146, 0.025865, 0.0);
             skPoint = Part.SketchManager.CreatePoint(0.043401, 0.000225, 0.0);
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);

             boolstatus = Part.Extension.SelectByID2("Boss-Extrude2", "BODYFEATURE", -0.0477922378944982, 0.0421639999998433, 0.0233214950450815, false, 4, null, 0);
             boolstatus = Part.Extension.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, true, 64, null, 0);

             swSketchPatt = (SketchPatternFeatureData)Part.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmSketchPattern);
             swSketchPatt.GeometryPattern = false;
             swSketchPatt.UseCentroid = true;
             swSketchFeat = (Feature)Part.FeatureManager.CreateFeature(swSketchPatt);
             swSketchPatt = (SketchPatternFeatureData)swSketchFeat.GetDefinition();

             swSketchPatt.AccessSelections(Part, null);

             swSketch = (Sketch)swSketchPatt.Sketch;
             i = swSketch.GetSketchPointsCount2();

             swPatternTransform = swSketchPatt.GetTransform(i);

             vBasePt = (double[])swSketchPatt.GetBasePoint();

             Debug.Print(swSketchFeat.Name);
             Debug.Print("  Create pattern using only geometry? " + swSketchPatt.GeometryPattern);
             Debug.Print("  Pattern seed coordinates in mm:  (" + vBasePt[0] * 1000.0 + ", " + vBasePt[1] * 1000.0 + ", " + vBasePt[2] * 1000.0 + ")");
             Debug.Print("  Body count: " + swSketchPatt.GetPatternBodyCount());
             Debug.Print("  Face count: " + swSketchPatt.GetPatternFaceCount());
             Debug.Print("  Feature count: " + swSketchPatt.GetPatternFeatureCount());
             Debug.Print("  Reference point type (-1 for centroid): " + swSketchPatt.GetReferencePointType());
             Debug.Print("  Use centroid as the reference point? " + swSketchPatt.UseCentroid);
             Debug.Print("  Propagate visual properties? " + swSketchPatt.PropagateVisualProperty);

             swSketchPatt.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

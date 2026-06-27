---
title: "Create Projection Split Line Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Projection_Split_Line_Example_CSharp.htm"
---

# Create Projection Split Line Feature Example (C#)

This example shows how to create a projection split line feature.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Creates a new model document with a feature extrusion, reference plane,
 //    and sketch of an ellipse.
 // 2. Creates Split Line1 in the FeatureManager design tree.
 // 3. Inspect the Immediate window.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertSplitLineFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SketchSegment skSegment;
         RefPlane myRefPlane;
         SelectionMgr swSelMgr;
         SplitLineFeatureData swSplitLine;
         object vSkLines;
         Feature myFeature;
         bool boolstatus;
         int longstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             Part = (ModelDoc2)swApp.ActiveDoc;

             skSegment = Part.SketchManager.CreateEllipse(-0.0212512457655407, 0.0122505076014363, 0, 0.00277468345541365, 0.00705202391259263, 0, -0.0196159170237913, 0.0198085370103935, 0);
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);

             boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);

             myRefPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(8, 0.01778, 0, 0, 0, 0);
             Part.ClearSelection2(true);

             Part.SketchManager.InsertSketch(true);
             boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -0.0407148636658249, 0.0247341229458697, 0.0194913387248102, false, 0, null, 0);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
             boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);

             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0625406077424486, 0.0297244912047745, 0, 0.0584903577919818, -0.018090206988802, 0);
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 4, null, 0);

             myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
             0, 0, false);
             ((SelectionMgr)(Part.SelectionManager)).EnableContourSelection = false;

             boolstatus = Part.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", -0.0143044793836914, 0.00334438727079956, 0, true, 4, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0181817275523031, 0.0132444059746035, 0.0177800000000161, true, 1, null, 0);

             Part.InsertSplitLineProject(true, true);

             swSelMgr = (SelectionMgr)Part.SelectionManager;

             boolstatus = Part.Extension.SelectByID2("Split Line1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);

             myFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSplitLine = (SplitLineFeatureData)myFeature.GetDefinition();

             // Get split line feature data
             boolstatus = swSplitLine.AccessSelections(Part, null);

             Debug.Print(myFeature.Name);
             Debug.Print("    Split type as defined in swSplitLineFeatureType_e: " + swSplitLine.GetType());
             Debug.Print("    Single Direction? " + swSplitLine.SingleDirection);
             Debug.Print("    Reversed? " + swSplitLine.ReverseDirection);

             swSplitLine.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

---
title: "Create Replace Face Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Face_Example_CSharp.htm"
---

# Create Replace Face Feature Example (C#)

This example shows how to create a Replace Face feature.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part.
  // 2. Creates Plane1, Surface-Extrude1, and Replace Face1.
 // 3. Inspect the FeatureManager design tree, the graphics area, and the
 //    Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace ReplaceFace_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         SelectionMgr selMgr;
         ModelDoc2 Part;
         Feature feat;
         ReplaceFaceFeatureData featData;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("block20", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.00687152192142548, 0.0256655537640995, 0.049345602378537, true, 0, null, 0);
             RefPlane myRefPlane = default(RefPlane);
             myRefPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(264, 0.05842, 0, 0, 0, 0);
             Part.ClearSelection2(true);

             object pointArray = null;
             double[] points = new double[15];
             points[0] = -0.0700496017443584;
             points[1] = 0.0582762055241233;
             points[2] = 0;
             points[3] = -0.0357558994484748;
             points[4] = 0.0853945497913173;
             points[5] = 0;
             points[6] = -0.00588719099721402;
             points[7] = 0.0671372129016845;
             points[8] = 0;
             points[9] = 0.0273002628375139;
             points[10] = 0.0878577815467452;
             points[11] = 0;
             points[12] = 0.0737626982062238;
             points[13] = 0.0582762055241233;
             points[14] = 0;
             pointArray = points;
             SketchSegment skSegment = default(SketchSegment);
             skSegment = Part.SketchManager.CreateSpline((pointArray));
             Part.SketchManager.InsertSketch(true);
             boolstatus = Part.Extension.SelectByID2("Spline1@Sketch2", "EXTSKETCHSEGMENT", -0.0549544681183813, 0.0875052976097064, 0, false, 0, null, 0);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 4, null, 0);
             ((SelectionMgr)Part.SelectionManager).EnableContourSelection = true;
             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCHCONTOUR", 0, 0, 0, true, 4, null, 0);
             Part.FeatureExtruRefSurface2(true, false, false, 0, 0, 0.14478, 0.14478, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false);
             ((SelectionMgr)Part.SelectionManager).EnableContourSelection = false;
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0585444908073214, 0.0396239999998329, -0.0518899759430838, true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -0.0189730427370591, 0.0726880897401543, 0.115671174990496, true, 0, null, 0);
             Part.ClearSelection2(true);
             boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0585444908073214, 0.0396239999998329, -0.0518899759430838, true, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -0.0189730427370591, 0.0726880897401543, 0.115671174990496, true, 2, null, 0);
             Part.InsertFeatureReplaceFace();
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0362064915135534, 0.0856902732399476, 0.127037337239983, false, 0, null, 0);
             Part.FeatureManager.HideBodies();
             boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -0.0693294107213475, 0.0872697709380442, -0.0300713252946179, false, 0, null, 0);
             Part.BlankRefGeom();

             boolstatus = Part.Extension.SelectByID2("Replace Face1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             selMgr = (SelectionMgr)Part.SelectionManager;
             feat = (Feature)selMgr.GetSelectedObject6(1, -1);
             featData = (ReplaceFaceFeatureData)feat.GetDefinition();

             featData.AccessSelections(Part, null);

             object[] vFacesToReplace = null;
             vFacesToReplace = (object[])featData.FacesForReplacement;
             Debug.Print(featData.GetFacesForReplacementCount() + " face replaced in " + ((Feature)((Face2)vFacesToReplace[0]).GetFeature()).Name);
             Debug.Print(featData.GetReplacementSurfacesCount() + " replacement surface ");

             featData.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

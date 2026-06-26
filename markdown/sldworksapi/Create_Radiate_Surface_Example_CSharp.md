---
title: "Create Radiate Surface Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Radiate_Surface_Example_CSharp.htm"
---

# Create Radiate Surface Feature Example (C#)

This example shows how to create a radiate surface feature.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a new model document with a feature extrusion.
 // 2. Creates Boss-Extrude1 and Surface-Radiate1 in the graphics area and
 //    FeatureManager design tree.
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

 namespace CreateSurfRadiateFeat_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SelectionMgr swSelMgr;
         SelectData swSelData;
         SurfaceRadiateFeatureData swRadiate;
         Feature swFeat;
         Entity swEnt;
         object[] vRadEnt;
         Entity swRadDirEnt;
         int i;

         bool boolStatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolStatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.0448901407839529, 0.0279954694016864, 0.00466820674117181, false, 0, null, 0);
             Part.SketchManager.InsertSketch(true);
             Part.ClearSelection2(true);
             boolStatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
             boolStatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
             object vSkLines = null;
             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0555749908365768, 0.0329075527136081, 0, 0.0478203409524033, -0.0317145296545045, 0);
             Part.ClearSelection2(true);
             Part.SketchManager.InsertSketch(true);
             Part.ShowNamedView2("*Trimetric", 8);
             Part.SketchManager.InsertSketch(true);
             Part.ClearSelection2(true);
             boolStatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 4, null, 0);

             object myFeature = null;
             myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
             0, 0, false);

             boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0447337592343047, 0.0328467250718631, 0.00258132540182032, false, 2, null, 0);
             boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0556265649287866, 0.0156695101210289, 0.0025672149453726, true, 2, null, 0);
             boolStatus = Part.Extension.SelectByID2("", "EDGE", -0.0140113588298618, -0.0317157034173761, 0.00254079743683633, true, 2, null, 0);
             boolStatus = Part.Extension.SelectByID2("", "EDGE", 0.047780958393389, -0.00542256709667299, 0.00256078163948814, true, 2, null, 0);
             boolStatus = Part.Extension.SelectByID2("", "FACE", 0.0478203409524554, -0.00305747564971171, 0.000546558985774936, true, 1, null, 0);

             Part.InsertRadiateSurface(0.0254, false, false);

             swSelMgr = (SelectionMgr)Part.SelectionManager;
             swSelData = swSelMgr.CreateSelectData();

             boolStatus = Part.Extension.SelectByID2("Surface-Radiate1", "REFSURFACE", 0, 0, 0, false, 0, null, 0);

             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swRadiate = (SurfaceRadiateFeatureData)swFeat.GetDefinition();

             // Get radiate surface data
             Debug.Print("File = " + Part.GetPathName());
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    Distance: " + swRadiate.Distance * 1000.0 + " mm");
             Debug.Print("    Flip? " + swRadiate.Flip);
             Debug.Print("    Propagate to tangent faces? " + swRadiate.PropagateToTangentFaces);

             // Roll back to get direction reference and radiated edges
             boolStatus = swRadiate.AccessSelections(Part, null);
             swRadDirEnt = (Entity)swRadiate.DirectionReference;
             Part.ClearSelection2(true);

             vRadEnt = (object[])swRadiate.RadiatedEntities;

             Debug.Print("Type as defined in swSelectType_e:");
             for (i = 0; i <= swRadiate.GetRadiatedEntitiesCount() - 1; i++)
             {
                 swEnt = (Entity)vRadEnt[i];
                 Debug.Print("    Radiated Entity(" + i + ") = " + swEnt.GetType());

             }

             swRadiate.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

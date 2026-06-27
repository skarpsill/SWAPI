---
title: "Create Trimmed Surface Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Trimmed_Surface_Feature_Example_CSharp.htm"
---

# Create Trimmed Surface Feature Example (C#)

This example shows how to create a trimmed surface feature.

```vb
  // ---------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a new model document with two intersecting surface extrude
 //    features.
 // 2. Selects Surface-Extrude2 as the trim tool and sets the trimming options.
 // 3. Trims Surface-Extrude1.
 // 4. Creates Surface-Trim1 in the FeatureManager design tree.
 // 5. Inspect the Immediate window.
  // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace CrateSurfTrimFeatData_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SketchManager swSketchMgr = default(SketchManager);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SketchSegment swSketchSegment = default(SketchSegment);
             FeatureManager swFeatureMgr = default(FeatureManager);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             SurfaceTrimFeatureData surfTrimFeatData = default(SurfaceTrimFeatureData);
             bool status = false;

             // Create new model document
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
             swSketchMgr = (SketchManager)swModel.SketchManager;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             swFeatureMgr = (FeatureManager)swModel.FeatureManager;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Create two intersecting surfaces
             status = swModelDocExt.SelectByID2("Right Plane", "Plane", 0, 0, 0, false, 0, null, 0);
             swSketchMgr.InsertSketch(true);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.068922, 0.023964, 0.0, 0.042733, 0.005543, 0.0);
             swModel.ClearSelection2(true);
             status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             swFeatureMgr.FeatureExtruRefSurface2(true, false, false, 0, 0, 0.06604, 0.00254, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, false, false,
             false);
             swSelMgr.EnableContourSelection = false;

             status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
             swSketchMgr.InsertSketch(true);
             swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.041529, 0.023059, 0.0, -0.052625, -0.081662, 0.0);
             swModel.ClearSelection2(true);
             status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             swFeatureMgr.FeatureExtruRefSurface2(false, false, false, 0, 0, 0.0889, 0.06604, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, false, false,
             false);
             swSelMgr.EnableContourSelection = false;

             // Set the trimming options
             status = swFeatureMgr.PreTrimSurface(false, true, false, false);

             // Trim the surface
             status = swModelDocExt.SelectByID2("", "SURFACEBODY", 0.0289416986472588, 0.00781827749557351, 0.0290635845400971, true, 0, null, 0);
             swFeat = (Feature)swFeatureMgr.PostTrimSurface(true);

             swModel.ClearSelection2(true);

             surfTrimFeatData = (SurfaceTrimFeatureData)swFeat.GetDefinition();

             surfTrimFeatData.AccessSelections(swModel, null);

             Debug.Print(swFeat.Name);
             Debug.Print("  Number of pieces to keep: " + surfTrimFeatData.GetPiecesToKeepCount());
             Debug.Print("  Surface trim feature type as defined in swSurfaceTrimType_e: " + surfTrimFeatData.GetType());
             Debug.Print("");

             object[] varTrimTools = null;
             int i = 0;

             varTrimTools = (object[])surfTrimFeatData.TrimTools;
             Debug.Print("Trim tools:");
             for (i = 0; i <= surfTrimFeatData.GetTrimToolsCount() - 1; i++)
             {
                 Debug.Print("  " + ((Feature)varTrimTools[i]).Name);
             }

             surfTrimFeatData.ReleaseSelectionAccess();

         }

         /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

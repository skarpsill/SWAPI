---
title: "Create Surface Knit Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Surface_Knit_Feature_Example_CSharp.htm"
---

# Create Surface Knit Feature Example (C#)

This example shows how to create a surface knit feature.

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates two surfaces.
// 3. Creates a surface knit feature using the two
//    selected surfaces.
// 4. Examine the graphics area, FeatureManager design
//    tree, and Immediate window.
//--------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro2CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        SketchManager swSketchManager;
        SketchSegment swSketchSegment;
        FeatureManager swFeatureManager;
        SelectionMgr swSelectionManager;
        Feature swFeature;
        SurfaceKnitFeatureData swSurfaceKnitFeature;

        bool boolstatus;

        public void Main()
        {
            //Open new part document and create two surfaces
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchManager = (SketchManager)swModel.SketchManager;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateEllipse(-0.0415374666666667, 0, 0, 0.0534585333333333, 0, 0, -0.0415374666666667, 0.0208618666666667, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 4, null, 0);
            swFeatureManager.FeatureExtruRefSurface2(true, false, false, 0, 0, 0.05, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, false, false, false);
            swSelectionManager.EnableContourSelection = false;
            boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 1, null, 0);
            boolstatus = swModel.InsertPlanarRefSurface();
            swModel.ClearSelection2(true);

            // Select both surfaces and create surface knit feature
            boolstatus = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, false, 1, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Surface-Plane1", "SURFACEBODY", 0, 0, 0, true, 1, null, 0);
            swFeature = (Feature)swFeatureManager.InsertSewRefSurface(true, false, false, 0.0001, 0.0001);

            // Get some surface knit feature data
            swSurfaceKnitFeature = (SurfaceKnitFeatureData)swFeature.GetDefinition();
            Debug.Print("Knit-surface feature: ");
            Debug.Print("  Knit tolerance: " + swSurfaceKnitFeature.KnitTolerance * 1000 + " mm");
            Debug.Print("  Maximum value for gap range: " + swSurfaceKnitFeature.MaxValueForGapRange * 1000 + " mm");
            Debug.Print("  Minimum value for gap range: " + swSurfaceKnitFeature.MinValueForGapRange * 1000 + " mm");
            Debug.Print("  Use gap filters? " + swSurfaceKnitFeature.UseGapFilters);
            Debug.Print("  Use merge entities? " + swSurfaceKnitFeature.UseMergeEntities);
            Debug.Print("  Try to form solid? " + swSurfaceKnitFeature.UseTryToFormSolid);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

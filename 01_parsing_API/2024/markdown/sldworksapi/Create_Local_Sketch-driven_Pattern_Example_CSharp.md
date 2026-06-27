---
title: "Create Local Sketch-driven Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Sketch-driven_Pattern_Example_CSharp.htm"
---

# Create Local Sketch-driven Pattern Example (C#)

This example shows how to create a local sketch-driven pattern feature.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens specified assembly document.
// 2. Creates a sketch for the local sketch-driven
//    pattern.
// 3. Selects an assembly component and the just-created
//    sketch for the local sketch-driven pattern.
// 4. Creates local sketch-driven pattern.
// 5. Gets values and settings of the local sketch-driven pattern.
// 6. Examine the Immediate window and graphics area.
//
// NOTE: Because this assembly is used elsewhere, do not save
// changes.
//------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FeatureLocalSketchDrivenPatternCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SketchManager swSketchMgr = default(SketchManager);
            SketchPoint swSketchPoint = default(SketchPoint);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            LocalSketchPatternFeatureData swLocalSketchPatternFeat = default(LocalSketchPatternFeatureData);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\assem1.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Create sketch
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            swSketchPoint = (SketchPoint)swSketchMgr.CreatePoint(0.025, -0.05, 0.0);
            swSketchPoint = (SketchPoint)swSketchMgr.CreatePoint(0.05, -0.075, 0.0);
            swSketchPoint = (SketchPoint)swSketchMgr.CreatePoint(0.1, -0.05, 0.0);
            swSketchMgr.InsertSketch(true);

            //Select a component and the just-created sketch
            //for the local sketch-driven pattern
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 16, null, 0);

            //Insert local sketch-driven pattern
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
```

```vb
            swLocalSketchPatternFeat = (LocalSketchPatternFeatureData)swFeatMgr.CreateDefinition((int)swLocalSketchPatternReferencePoint_e.swFmLocalSketchPattern);
             swLocalSketchPatternFeat.ReferencePoint = 1;  //Bounding box center
             swFeat = (Feature)swFeatMgr.CreateFeature(swLocalSketchPatternFeat);

             //Get local sketch-driven pattern feature data
             swLocalSketchPatternFeat = (LocalSketchPatternFeatureData)swFeat.GetDefinition();
             Debug.Print("Local sketch-driven pattern properties: ");
             Debug.Print("  Number of components: " + swLocalSketchPatternFeat.GetPatternComponentCount());
             Debug.Print("  Number of items skipped: " + swLocalSketchPatternFeat.GetSkippedItemCount());
             Debug.Print("  Type of reference point: " + swLocalSketchPatternFeat.ReferencePoint);
             Debug.Print("  Is reference point a closed curve, sketch point, vertex, or default value: " + swLocalSketchPatternFeat.GetReferencePointType());

         }

         /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

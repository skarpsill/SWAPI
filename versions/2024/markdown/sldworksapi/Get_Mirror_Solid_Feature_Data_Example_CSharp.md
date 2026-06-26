---
title: "Get Mirror Solid Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Solid_Feature_Data_Example_CSharp.htm"
---

# Get Mirror Solid Feature Data Example (C#)

This example shows how to get data for a mirror solid feature.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects a plane and solid body.
// 3. Mirrors the solid body.
// 4. Gets the mirror solid feature and some of its data.
// 5. Prints to the Immediate window some mirror solid feature data.
// 6. Examine the Immediate window, FeatureManager design tree, and graphics
//    area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MirrorSolidFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            MirrorSolidFeatureData swMirrorSolidFeatureData = default(MirrorSolidFeatureData);
            Body2 swBody = default(Body2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            SelectData swSelData = default(SelectData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int i = 0;
            object[] bodies = null;

            //Open part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select plane and solid body
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Top", "PLANE", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Top", "PLANE", 0, 0, 0, false, 2, null, 0);
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, true, 256, null, 0);

            //Insert mirror solid feature
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertMirrorFeature2(true, false, false, false, (int)swFeatureScope_e.swFeatureScope_AllBodies);

            //Get mirror solid feature and some of its data
            swMirrorSolidFeatureData = (MirrorSolidFeatureData)swFeature.GetDefinition();
            Debug.Print("  " + swFeature.Name);
            Debug.Print("    Number of bodies                = " + swMirrorSolidFeatureData.GetPatternBodyCount());
            Debug.Print("    Merged bodies                   = " + swMirrorSolidFeatureData.Merge);
            Debug.Print("    Knit surfaces                   = " + swMirrorSolidFeatureData.KnitSurface);

            //Roll back to get to the bodies
            status = swMirrorSolidFeatureData.AccessSelections(swModel, null);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelectionMgr.CreateSelectData();
            bodies = (object[])swMirrorSolidFeatureData.PatternBodyArray;
            for (i = 0; i < bodies.Length; i++)
            {
                swBody = (Body2)bodies[i];
                status = swBody.Select(true, 0);
                Debug.Print("    Body " + i + 1 + "'s type (solid body = 0) = " + swBody.GetType());
            }

            //Release selection access
            swMirrorSolidFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

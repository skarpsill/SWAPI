---
title: "Get Data for Surface-flatten Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm"
---

# Get Data for Surface-flatten Feature Example (C#)

This example shows how to insert a surface-flatten feature and get its data.

```
//-------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Inserts a surface-flatten feature.
// 3. Gets surface-flatten feature data.
// 4. Examine the graphics area and FeatureManager design
//    tree.
//
// NOTE: Because this part is used elsewhere, do not save
// changes.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            SurfaceFlattenFeatureData swSurfaceFlattenFeatureData = default(SurfaceFlattenFeatureData);
            Edge swEdge = default(Edge);
            bool status = false;
            int warnings = 0;
            int errors = 0;
            string fileName = null;
            object[] edges = null;
            int nbrTearEdges = 0;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\hemisphere.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Select face, vertex, and curves for surface-flatten feature
            status = swModelDocExt.SelectByID2("", "FACE", 0.00546207138008786, -0.0373996629648742, 0.0130049636270216, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", 0, -0.0400014251170795, -0.00054185036618795, true, 16, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.011047389592717, -6.23453597697887E-06, 0.0382739927527045, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0108290857690036, -0.0262767618508641, 0.0280128973987478, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.00907918330954303, 0.0286363967873063, 0.0262553195430037, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0157595492108076, 0.0240950142317162, -0.0272880335909787, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0143808110794609, -0.0281074423709366, -0.0240578702886196, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.01886657492451, 2.48139106812095E-05, -0.035004838468241, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0140143161426676, -0.0374399859522778, 0.000123652313243445, true, 8, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0164192327552536, 0.0363245554251959, -9.58561062339106E-05, true, 8, null, 0);

            // Create surface-flatten feature
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertFlattenSurface2(8, true);

            // Get some surface-flatten feature data
            swSurfaceFlattenFeatureData = (SurfaceFlattenFeatureData)swFeature.GetDefinition();
            swSurfaceFlattenFeatureData.AccessSelections(swModel, null);
            Debug.Print("Feature = " + swFeature.Name);
            Debug.Print("   Accuracy of flattened triangle mesh =  " + swSurfaceFlattenFeatureData.AccuracyFactor);
            Debug.Print("   Keep internal control curves? " + swSurfaceFlattenFeatureData.KeepInternalControlCurves);
            if (swSurfaceFlattenFeatureData.ShouldMakeTears == true)
            {
                Debug.Print("   Tear edges: ");
                edges = (object[])swSurfaceFlattenFeatureData.TearEdges;
                nbrTearEdges = edges.Length;
                Debug.Print("      Number of tear edges: " + nbrTearEdges);
                for (i = 0; i <= nbrTearEdges - 1; i++)
                {
                    swEdge = (Edge)edges[i];
                    SelectionMgr swSelMgr = default(SelectionMgr);
                    swSelMgr = (SelectionMgr)swModel.SelectionManager;
                    status = swSelMgr.AddSelectionListObject(swEdge, null);
                    Debug.Print("            Type of object (51 = swSelREFEDGES): " + swSelMgr.GetSelectedObjectType3(1, -1));
                }
            }
            swSurfaceFlattenFeatureData.ReleaseSelectionAccess();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

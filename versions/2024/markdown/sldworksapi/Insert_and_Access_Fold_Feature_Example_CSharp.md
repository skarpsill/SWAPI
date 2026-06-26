---
title: "Insert and Access Fold Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Access_Fold_Feature_Example_CSharp.htm"
---

# Insert and Access Fold Feature Example (C#)

This example shows how to insert and access a fold feature.

```
//---------------------------------------------------------------
// Postconditions:
// 1. Verify that the specified sheet metal part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified sheet metal part document.
// 2. Creates an unfold feature.
// 3. Creates a fold feature.
// 4. Prints to the Immediate window some fold feature data.
// 5. Examine the FeatureManager design tree and the Immediate window.
//
// NOTE: Because this part is used elsewhere, do not save changes.
//---------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FoldsFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            FoldsFeatureData swFoldsFeatureData = default(FoldsFeatureData);
            Face2 swFace = default(Face2);
            Body2 swBody = default(Body2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int i = 0;
            object[] bendsArray = null;

            //Open sheet metal part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Insert unfold feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0135437392197275, 0.013831948116092, 0.0180159642212061, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0139765211971223, 0.045779599797811, -0.018375967305019, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 0.0145403568253926, 0.0461305825900808, -0.00849880301666417, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 0.0455785871991452, 0.0109703538056465, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 0.0139037479688966, 0.0457015473971296, 0.0275647689667267, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0135437392197275, 0.013831948116092, 0.0180159642212061, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0139765211971223, 0.045779599797811, -0.018375967305019, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 0.0145403568253926, 0.0461305825900808, -0.00849880301666417, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 0.0455785871991452, 0.0109703538056465, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 0.0139037479688966, 0.0457015473971296, 0.0275647689667267, true, 4, null, 0);
            swModel.InsertSheetMetalUnfold();

            //Insert fold feature
            status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0135437392197559, 0.0460611937937756, -0.019419982567797, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Unfold1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0135437392197559, 0.0460611937937756, -0.019419982567797, true, 4, null, 0);
            swModel.InsertSheetMetalFold();

            //Access the fold feature
            status = swModelDocExt.SelectByID2("Fold1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swFoldsFeatureData = (FoldsFeatureData)swFeature.GetDefinition();
            status = swFoldsFeatureData.AccessSelections(swModel, null);

            //Get name of fixed face body in the fold feature
            swFace = (Face2)swFoldsFeatureData.FixedFace;
            swBody = (Body2)swFace.GetBody();
            Debug.Print("Name of the body of the fixed face of the fold feature: " + swBody.Name);

            //Get the names bend features in the fold feature
            bendsArray = (object[])swFoldsFeatureData.Bends;
            for (i = 0; i < bendsArray.Length; i++)
            {
                swFeature = (Feature)bendsArray[i];
                Debug.Print("Name of bend feature" + (i + 1) + " of the fold feature: " + swFeature.Name);
            }

            //Release selection access
            swFoldsFeatureData.ReleaseSelectionAccess();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

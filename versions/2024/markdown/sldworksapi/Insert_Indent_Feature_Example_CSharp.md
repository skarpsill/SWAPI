---
title: "Insert Indent Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Indent_Feature_Example_CSharp.htm"
---

# Insert Indent Feature Example (C#)

This example shows how to insert and modify an indent feature.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Selects the boss-extrude body and a face on the
//    extrude-thin body.
// 3. Inserts an indent feature.
// 4. Modifies the thickness of the indent feature.
// 5. Examine the Immediate window, FeatureManager design tree,
//    and graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------

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
            FeatureManager swFeatureMgr = default(FeatureManager);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            IndentFeatureData swIndentFeatureData = default(IndentFeatureData);
            Body2 targetBody = default(Body2);
            Face2 swFace = default(Face2);
            Body2 toolRegionBody = default(Body2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            object[] toolBodyRegions = null;
            int toolBodyRegionType = 0;
            int nbrBodies = 0;
            int i = 0;

            //Open part where to insert indent feature
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select solid body for target body,
            //select face for tool body region, and
            //and insert indent feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0371343422566497, -0.0149999999999864, 0.0883053842352979, true, 4, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertIndent(0.01, 0, true, true, false, false);

            //Access and modify indent feature
            Debug.Print("Indent feature name: " + swFeature.Name);
            swIndentFeatureData = (IndentFeatureData)swFeature.GetDefinition();
            swIndentFeatureData.AccessSelections(swModel, null);
            nbrBodies = swIndentFeatureData.GetBodiesCount();
            Debug.Print("  Number of bodies: " + nbrBodies);
            targetBody = (Body2)swIndentFeatureData.TargetBody;
            Debug.Print("  Name of target body: " + targetBody.Name);
            toolBodyRegions = (object[])swIndentFeatureData.ToolBodyRegion;
            Debug.Print("  Number of tool body regions: " + toolBodyRegions.Length);
            for (i = 0; i < nbrBodies; i++)
            {
                swModel.ClearSelection2(true);
                swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
                status = swSelectionMgr.AddSelectionListObject(toolBodyRegions[i], null);
                toolBodyRegionType = swSelectionMgr.GetSelectedObjectType3(1, -1);
                Debug.Print("  Type of object selected for tool body region (2 = face; 3 = vertex): " + toolBodyRegionType);
                //If object selected for tool body region is a face,
                //then get the name of its body
                if (toolBodyRegionType == 2)
                {
                    swFace = (Face2)toolBodyRegions[i];
                    toolRegionBody = (Body2)swFace.GetBody();
                    Debug.Print("  Name of body of tool body region: " + toolRegionBody.Name);
                }
            }
            Debug.Print("  Original thickness: " + swIndentFeatureData.Thickness);
            //Change thickness
            swIndentFeatureData.Thickness = 0.011;
            Debug.Print("  Modified thickness: " + swIndentFeatureData.Thickness);
            status = swFeature.ModifyDefinition(swIndentFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

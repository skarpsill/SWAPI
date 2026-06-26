---
title: "Mirror Sheet-metal Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Sheet-metal_Part_Example_CSharp.htm"
---

# Mirror Sheet-metal Part Example (C#)

This example shows how to mirror a sheet-metal part.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the sheet-metal part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified sheet-metal part.
// 2. Creates a reference plane about which to mirror the
//    sheet-metal part.
// 3. Creates a new part document containing the mirrored
//    sheet-metal part, which includes the sheet-metal
//    information in the mirrored part.
// 4. Examine the graphics area and the Immediate window.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MirrorSheetMetalPartCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            PartDoc swPart = default(PartDoc);
            Feature swMirrorFeature = default(Feature);
            Feature swFeature = default(Feature);
            ModelDoc2 swResultPart = null;
            MirrorPartFeatureData swMirrorFeatData = default(MirrorPartFeatureData);
            RefPlane swRefPlane = default(RefPlane);
            Entity swPlane = default(Entity);
            int mirrorOptions = 0;
            int mirrorType = 0;
            swSelectType_e selType = default(swSelectType_e);
            string filename = null;
            int errors = 0;
            bool status = false;
            int warnings = 0;

            filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(filename, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            if (swModel == null)
                return;
            if (swModel.GetType() != (int)swDocumentTypes_e.swDocPART)
                return;

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swRefPlane = (RefPlane)swFeatureMgr.InsertRefPlane(8, 0.09, 0, 0, 0, 0);
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            selType = (swSelectType_e)swSelMgr.GetSelectedObjectType3(1, -1);
            if (!(selType == swSelectType_e.swSelDATUMPLANES))
                return;

            swPart = (PartDoc)swModel;
            mirrorOptions = (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportSMInfo + (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportIndProps + (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids + (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportCutListProperties;
            swMirrorFeature = (Feature)swPart.MirrorPart2(false, mirrorOptions, out swResultPart);
            if (swMirrorFeature == null)
            {
                Debug.Print("No feature!");
            }
            else
            {
                Debug.Print("Feature: " + swMirrorFeature.Name);
            }

            if (swResultPart == null)
            {
                Debug.Print("No new part! ");
            }
            else
            {
                Debug.Print("Part document title: " + swResultPart.GetTitle());
            }

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swMirrorFeature.Select2(false, -1);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swMirrorFeatData = (MirrorPartFeatureData)swFeature.GetDefinition();

            swMirrorFeatData.AccessSelections(swModel, null);

            Debug.Print("  Path name = " + swMirrorFeatData.PathName);
            Debug.Print("  Import:  ");
            Debug.Print("     Solid bodies?  " + swMirrorFeatData.SolidBodies);
            Debug.Print("     Cut-list properties? " + swMirrorFeatData.CutListProperties);
            Debug.Print("     Sheet-metal information?  " + swMirrorFeatData.SheetMetalInformation);
            Debug.Print("     Unlocked properties?  " + swMirrorFeatData.UnlockedProperties);

            mirrorType = swMirrorFeatData.GetMirrorPlaneType();
            Debug.Print("  Mirror plane type as defined in swMirrorPlaneType_e = " + mirrorType);
            swRefPlane = (RefPlane)swMirrorFeatData.GetMirrorPlane();
            swMirrorFeatData.ReleaseSelectionAccess();
            swPlane = (Entity)swRefPlane;
            swPlane.Select(false);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Get Gusset Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Gusset_Feature_Data_Example_CSharp.htm"
---

# Get Gusset Feature Data Example (C#)

This example shows how to get some data for a gusset feature.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects and gets the Gusset1 feature.
// 3. Gets some Gusset1 feature data.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GussetFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            GussetFeatureData swGussetFeatureData = default(GussetFeatureData);
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            Face2 oneFace = null;
            Face2 twoFace = null;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\weldment_box3.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select and get Gusset1
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Gusset1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swGussetFeatureData = (GussetFeatureData)swFeature.GetDefinition();

            //Access Gusset1 and get some feature data
            swGussetFeatureData.AccessSelections(swModel, null);
            Debug.Print("Profile type: " + swGussetFeatureData.ProfileType);
            Debug.Print("Thickness type: " + swGussetFeatureData.ThicknessType);
            Debug.Print("Thickness: " + swGussetFeatureData.Thickness);
            if (swGussetFeatureData.OffsetUsed == true)
            {
                Debug.Print("Profile offset distance: " + swGussetFeatureData.ProfileOffsetDistance);
            }
            else
            {
                Debug.Print("No profile offset used.");
            }
            status = swGussetFeatureData.GetSupportingFaces(out oneFace, out twoFace);
            status = oneFace.IsSame(twoFace);
            Debug.Print("Is the first supporting face the same as the second supporting face: " + status);
            swGussetFeatureData.ReleaseSelectionAccess();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Combine Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Combine_Bodies_Example_CSharp.htm"
---

# Combine Bodies Example (C#)

This example shows how to combine bodies in a multibody part.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Verify that the part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects two solid bodies.
// 3. Inserts a combine feature using the two selected
//    bodies.
// 4. Prints the type of combine feature to the Immediate
//    window.
// 5. Examine the Immediate window.
//
// NOTE: Because the part document is used elsewhere, do not
// save changes.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CombineBodiesCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            CombineBodiesFeatureData swCombineBodiesFeatureData = default(CombineBodiesFeatureData);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, false, 2, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, true, 2, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertCombineFeature((int)swBodyOperationType_e.SWBODYADD, null, null);

            swCombineBodiesFeatureData = (CombineBodiesFeatureData)swFeature.GetDefinition();
            status = swCombineBodiesFeatureData.AccessSelections(swModel, null);
            //swCombineBodiesOperationType_e:
            // swCombineBodiesOperationAdd = 0
            // swCombineBodiesOperationCommon = 2
            // swCombineBodiesOperationSubract = 1
            Debug.Print("Type of combine feature: " + swCombineBodiesFeatureData.OperationType);
            swCombineBodiesFeatureData.ReleaseSelectionAccess();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Edit Mate Reference Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Mate_Reference_Example_CSharp.htm"
---

# Edit Mate Reference Example (C#)

This example shows how to insert and edit a mate reference.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Adds a mate reference.
// 3. Edits the mate reference.
// 4. Expand MateReferences in the FeatureManager design tree
//    and click MyDefault<1>.
// 5. Examine the graphics area and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------

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
            Feature swFeature = default(Feature);
            FeatureManager swFeatureMgr = default(FeatureManager);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Entity swPlane = default(Entity);
            Face2 swFace = default(Face2);
            Entity swFaceEntity = default(Entity);
            MateReference swMateReference = default(MateReference);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Insert mate reference
            status = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, true, 1, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swPlane = (Entity)swSelectionMgr.GetSelectedObject6(1, -1);
            status = swModelDocExt.SelectByID2("", "FACE", 0.00835786916030656, 0.00429540237419701, 0, true, 2, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertMateReference2("Default", null, 0, 1, false, null, 0, 2, false, null,
            0, 0);
            swModel.ClearSelection2(true);

            //Edit mate reference
            status = swModelDocExt.SelectByID2("", "FACE", 0.0117890806857872, 0.00419179196288511, 0.00999999999999091, false, 0, null, 0);
            swFace = (Face2)swSelectionMgr.GetSelectedObject6(1, -1);
            swFaceEntity = (Entity)swFace;
            status = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swMateReference = (MateReference)swFeature.GetSpecificFeature2();
            swModel.ClearSelection2(true);
            status = swMateReference.Edit("MyDefault", swPlane, (int)swMateReferenceType_e.swMateReferenceType_default, (int)swMateReferenceAlignment_e.swMateReferenceAlignment_Any, swFaceEntity, (int)swMateReferenceType_e.swMateReferenceType_default, (int)swMateReferenceAlignment_e.swMateReferenceAlignment_Any, null, (int)swMateReferenceType_e.swMateReferenceType_default, (int)swMateReferenceAlignment_e.swMateReferenceAlignment_Any);
            Debug.Print("Mate reference modified and replaced? " + status);

            swModel.EditRebuild3();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

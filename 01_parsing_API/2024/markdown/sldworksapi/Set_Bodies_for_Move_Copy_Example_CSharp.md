---
title: "Set Bodies for Move/Copy Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Bodies_for_Move_Copy_Example_CSharp.htm"
---

# Set Bodies for Move/Copy Example (C#)

This example shows how to set a body for a move/copy.

```
//---------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects a solid body and two vertices.
// 3. Inserts a move/copy body feature.
// 4. Sets the body to move, copy, or rotate.
// 5. Examine the FeatureManager design tree, the graphics area, and
//    the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            MoveCopyBodyFeatureData swMoveCopyBodyFeatureData = default(MoveCopyBodyFeatureData);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            object[] bodyArr = new object[1];
            Body2 aBody = default(Body2);

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swPart = (PartDoc)swModel;

            //Select solid body and vertices for move/copy body feature
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, true, 8, null, 0);

            //Insert move/copy body feature
            swFeature = (Feature)swFeatureManager.InsertMoveCopyBody2(0, 0, 0, 0, -0.085, 0, 0.065, 0, 0, 0,
            true, 1);
            swFeature = (Feature)swPart.FeatureByName("Body-Move/Copy1");

            //Roll forward the feature and get and set move/copy body feature data
            swMoveCopyBodyFeatureData = (MoveCopyBodyFeatureData)swFeature.GetDefinition();
            status = swMoveCopyBodyFeatureData.AccessSelections(swModel, null);

            //Get the body to set
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            bodyArr[0] = (object)swSelectionMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);
            swMoveCopyBodyFeatureData.Bodies = bodyArr[0];
            if ((bodyArr == null))
            {
                Debug.Print("Body not set.");
            }
            else
            {
                Debug.Print("Body set.");
                aBody = (Body2)bodyArr[0];
                Debug.Print("Name of body set: " + aBody.Name);
            }

            //Roll back the feature
            swMoveCopyBodyFeatureData.ReleaseSelectionAccess();

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

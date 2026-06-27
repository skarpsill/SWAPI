---
title: "Move Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Bodies_Example_CSharp.htm"
---

# Move Bodies Example (C#)

This example shows how to move all of the bodies in a part document.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Specified part document to open exists.
// 2. Run the macro.
//
// Postconditions: All of the bodies in the part document
// are moved to the specified location.
//
// NOTE: Because this part is used elsewhere, do not save
// any changes when closing it.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace MoveBodiesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void SelectBodies(SldWorks swApp, ModelDoc2 swModel, object[] bodyArr)
        {
            // Select and mark the bodies to move
            SelectionMgr swSelMgr = default(SelectionMgr);
            SelectData swSelData = default(SelectData);
            Body2 swBody = default(Body2);
            bool status = false;
            int i = 0;

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();

            if ((bodyArr == null))
                return;
            for (i = 0; i <= bodyArr.GetUpperBound(0); i++)
            {

                swBody = (Body2)bodyArr[i];
                swSelData.Mark = 1;
                status = swBody.Select2(true, swSelData);
            }

        }

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            object[] bodyArr = null;
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swPart = (PartDoc)swModel;
            swFeatMgr = (FeatureManager)swModel.FeatureManager;

            swModel.ClearSelection2(true);

            // Get the bodies to move
            bodyArr = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
            SelectBodies(swApp, swModel, bodyArr);

            // Move the bodies
            swFeat = (Feature)swFeatMgr.InsertMoveCopyBody2(0.1, 0.2, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            false, 1);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Get Editing Status of Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Editing_Status_of_Features_Example_CSharp.htm"
---

# Get Editing Status of Features Example (C#)

This example shows how to get the editing status of one or more features.

```
//------------------------------------------------------------------------
// Preconditions
// 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. At System.Diagnostics.Debugger.Break(), examine the the Immediate
//    window, graphics area, and FeatureManager design tree.
// 2. Press F5.
// 3. Examine the Immediate window again.
//
// NOTE: Because this document is used elsewhere, do not save changes.
//-------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            FeatureManager swFeatMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Object[] varFeat;
            long editStatus = 0;
            bool retVal = false;
            long i = 0;
            string featName = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swFeatMgr = swModel.FeatureManager;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = swModel.Extension;

            // Traverse through the FeatureManager design tree
            // to get the editing status of all features
            // Change the editing status of a sketch and feature
            // during feature traversal
            varFeat = (Object[])swFeatMgr.GetFeatures(true);
            editStatus = (long)swFeatureEditStatus_e.swFeature_NonEditable;
            for (i = varFeat.GetLowerBound(0); i <= varFeat.GetUpperBound(0); i++)
            {
                Feature swFeat = default(Feature);
                swFeat = (Feature)varFeat[i];
                featName = swFeat.Name;
                switch ((featName))
                {
                    case "Sketch2":
                        // Select and edit a sketch
                        retVal = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
                        swModel.EditSketch();

                        System.Diagnostics.Debugger.Break();
                        // Examine the Immediate window, graphics area, and FeatureManager design tree
                        // All of the features beneath Extrude1 cannot be edited because
                        // Extrude2's Sketch2 is in edit mode
                        // Press F5

                        break;

                    case "Extrude3":
                        // Close the open sketch
                        swModel.InsertSketch2(true);
                        break;
                    case "Cut-Extrude2":
                        // Select and edit a feature
                        retVal = swModelDocExt.SelectByID2("Cut-Extrude2", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
                        swModel.FeatEdit();
                        break;
                }

                // Get the editing status of the current feature
                editStatus = swFeat.GetEditStatus();
                switch ((editStatus))
                {
                    case 0:
                        Debug.Print(swFeat.Name + " can be edited.");
                        break;
                    case 1:
                        Debug.Print(swFeat.Name + " cannot currently be edited.");
                        break;
                    case 2:
                        Debug.Print(swFeat.Name + " is already being edited.");
                        break;
                }
                swFeat = null;
            }

            // End feature editing
            swModel.InsertSketch2(true);
        }
        public SldWorks swApp;
    }
}
```

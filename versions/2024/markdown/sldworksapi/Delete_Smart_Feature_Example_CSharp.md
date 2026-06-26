---
title: "Delete a Smart Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Smart_Feature_Example_CSharp.htm"
---

# Delete a Smart Feature Example (C#)

This example shows how to delete a feature from a Smart Component.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
// 2. Expand the Smart Feature and Features folders to verify that
//    Features contains two extrusion features.
//
// Postconditions:
// 1. Deletes one extrusion feature from the Features folder.
// 2. Expand the Smart Feature and Features folders to verify that
//    Features contains one extrusion feature.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//---------------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace DeleteSmartFeature_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        FeatureManager featMgr;

	        Feature myFeature;

	        ModelDoc2 swTrainAss;

	        ModelDoc2 swSmartPart;

	        SmartComponentFeatureData swSCFD;

	        SelectionMgr selMgr;

	        Feature feat;

	        object[]
	feats;

	        object obj;

	        int i;

	        int count;

	        bool boolstatus;

	        public void Main()

	        {

	            swSmartPart = (ModelDoc2)swApp.ActiveDoc;

	            featMgr = swSmartPart.FeatureManager;

	            feats = (object[])featMgr.GetFeatures(true);

	            count = featMgr.GetFeatureCount(true);

	            for (i = 0; i <= count - 1; i++)

	            {

	                myFeature = (Feature)feats[i];

	                if (myFeature.Name == "Smart Feature")

	                {

	                    Debug.Print(myFeature.Name);

	                    swSCFD = (SmartComponentFeatureData)myFeature.GetDefinition();

	                    // Open the training
	assembly of the Smart Component

	                    //
	Open the SmartComponent PropertyManager page to access its selection lists

	                    boolstatus = swSCFD.AccessSelections(true);

	                    swTrainAss = (ModelDoc2)swApp.ActiveDoc;

	                    selMgr = (SelectionMgr)swTrainAss.SelectionManager;

	                    Debug.Print("Number of features: " + selMgr.GetSelectedObjectCount2((int)swSmartComponentSelectionTypes_e.swSmartComponentFeatures));

	                    Debug.Print("Number of components: " + selMgr.GetSelectedObjectCount2((int)swSmartComponentSelectionTypes_e.swSmartComponentComponents));

	                    // Get the first
	extrusion from the features selection list

	                    obj = selMgr.GetSelectedObject6(1,
	(int)swSmartComponentSelectionTypes_e.swSmartComponentFeatures);

	                    feat = (Feature)obj;

	                    // To delete an
	extrusion feature from a Smart Component,

	                    //
	re-select it in the Smart Features selection list

	                    boolstatus = feat.Select2(true,
	(int)swSmartComponentSelectionTypes_e.swSmartComponentFeatures);

	                    // Modify the
	definition of the Smart Feature,

	                    //
	close the training assembly, and rebuild the Smart Component

	                    boolstatus = myFeature.ModifyDefinition(swSCFD, swSmartPart, null);

	                }

	            }

	        }

	        public SldWorks swApp;

	    }

	}
```

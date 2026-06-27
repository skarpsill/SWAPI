---
title: "Get Shut-Off Surface Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Shut-Off_Surface_Data_Example_CSharp.htm"
---

# Get Shut-Off Surface Data Example (C#)

This example shows how to get a shut-off surface feature's data.

```
//----------------------------------------------------------------------------
// Preconditions: Open a model that contains a Shut-Off Surface1 feature with
// the patch type of swShutOffSurfacePatchType_e.swPatchTypeTangent = 2.
//
// Postconditions:
// 1. Gets Shut-Off Surface1 data.
// 2. Gets the tangent faces for the specified loops where to create the patches.
// 3. Creates the patches on the opposite tangent faces.
// 4. Examine the graphic area and Immediate window.
//----------------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace GetShutOffSurfaceEdgeCount_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        ModelDocExtension swModelDocExt;

	        SelectionMgr swSelMgr;

	        Feature swFeat;

	        ShutOffSurfaceFeatureData swFeatData;

	        Entity swEnt;

	        object[]
	@params;

	        bool boolstatus;

	        int i;

	        int j;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swModelDocExt = swModel.Extension;

	            swSelMgr = (SelectionMgr)swModel.SelectionManager;

	            boolstatus = swModelDocExt.SelectByID2("Shut-Off
	Surface1", "REFSURFACE",
	0, 0, 0, false,
	0, null, (int)swSelectOption_e.swSelectOptionDefault);

	            swFeat = (Feature)swSelMgr.GetSelectedObject6(1,
	-1);

	            swFeatData = (ShutOffSurfaceFeatureData)swFeat.GetDefinition();

	            boolstatus = swFeatData.AccessSelections(swModel, null);

	            Debug.Print("Status = " + swFeatData.Status());

	            Debug.Print("Knit flag = " + swFeatData.Knit);

	            Debug.Print("Edge count = " + swFeatData.GetEdgeCount());

	            Debug.Print("Loop count = " + swFeatData.GetLoopCount());

	            for (i = 0; i <= swFeatData.GetLoopCount() - 1; i++)

	            {

	                Debug.Print("Loop(" + Convert.ToString(i)
	+ ")");

	                Debug.Print("    Edge
	count = " + swFeatData.GetLoopEdgeCount(i));

	                Debug.Print("    Patch
	type = " + swFeatData.get_LoopPatchType(i));

	                @params = (object[])swFeatData.get_LoopEdges(i);

	                for (j = 0; j <= @params.GetUpperBound(0); j++)

	                {

	                    swEnt = (Entity)@params[j];

	                    boolstatus = swEnt.Select4(false, null);

	                }

	            }

	            @params = (object[])swFeatData.Edges;

	            for (i = 0; i <= @params.GetUpperBound(0); i++)

	            {

	                swEnt = (Entity)@params[i];

	                boolstatus = swEnt.Select4(false, null);

	                swEnt = (Entity)swFeatData.GetFaceTangentTo(i);

	                if ((swEnt != null))

	                {

	                    boolstatus = swEnt.Select4(true, null);

	                }

	                swFeatData.FlipFaceTangentTo(i);

	                swEnt = (Entity)swFeatData.GetFaceTangentTo(i);

	                if ((swEnt != null))

	                {

	                    boolstatus = swEnt.Select4(true, null);

	                }

	                swFeatData.FlipFaceTangentTo(i);

	            }

	            boolstatus = swFeat.ModifyDefinition(swFeatData, swModel, null);

	        }

	        public SldWorks swApp;

	    }

	}
```

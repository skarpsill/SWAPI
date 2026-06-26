---
title: "Create 360-degree Revolve Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_360-degree_Revolve_Feature_Example_CSharp.htm"
---

# Create 360-degree Revolve Feature Example (C#)

## Create 360 ° Revolve Feature Example (C#)

This example shows how to create a 360° revolve feature.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part document that contains Axis1
//    and Sketch1 features; Sketch1 must be a rectangle and Axis1
//    must have been created using an edge on the rectangle.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a 360° revolve feature.
// 2. Examine the Immediate window, graphics area, and FeatureManager
//    design tree.
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

	namespace RevolveFeatDataType_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        ModelDocExtension swModelDocExt;

	        FeatureManager swFeatMgr;

	        Feature swFeat;

	        RevolveFeatureData2 swRevolveFeat;

	        bool boolstatus;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swModelDocExt = swModel.Extension;

	            boolstatus = swModelDocExt.SelectByID2("Axis1", "AXIS", 0, 0, 0, false,
	16, null,
	0);

	            boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH",
	0, 0, 0, true,
	0, null,
	0);

	            swFeatMgr = swModel.FeatureManager;

	            swFeat = swFeatMgr.FeatureRevolve2(true, true, false, false, false, false, 0,
	0, 6.2831853071796, 0,

	            false, false,
	0.01, 0.01, 0, 0, 0, true, true, true);

	            swModel.ViewZoomtofit2();

	            swRevolveFeat = (RevolveFeatureData2)swFeat.GetDefinition();

	            // Set the type of revolve as
	defined in swRevolveType_e

	            Debug.Print("Revolve feature type before setting to 5: " + swRevolveFeat.Type.ToString());

	            swRevolveFeat.Type = 5;

	            boolstatus = swFeat.ModifyDefinition(swRevolveFeat, swModel, null);

	            Debug.Print("Revolve feature type after setting to 5: " + swRevolveFeat.Type.ToString());

	        }

	        public SldWorks swApp;

	    }

	}
```

---
title: "Get Surface Trim Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface_Trim_Feature_Data_Example_CSharp.htm"
---

# Get Surface Trim Feature Data Example (C#)

This example shows how to get surface trim feature data.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part document with a surface trim feature.
// 2. Select the surface trim feature.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets the type of surface trim feature.
// 2. Examine the Immediate window.
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

	namespace SurfaceTrimFeatureData_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        SelectionMgr swSelMgr;

	        Feature swFeat;

	        SurfaceTrimFeatureData swSurfTrimFeat;

	        int surftrimtype;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swSelMgr = (SelectionMgr)swModel.SelectionManager;

	            swFeat = (Feature)swSelMgr.GetSelectedObject6(1,
	-1);

	            swSurfTrimFeat = (SurfaceTrimFeatureData)swFeat.GetDefinition();

	            surftrimtype = swSurfTrimFeat.GetType();

	            Debug.Print("Surface trim type (swSurfaceTrimType_e): " + surftrimtype);

	        }

	        public SldWorks swApp;

	    }

	}
```

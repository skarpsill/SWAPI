---
title: "Get Type of Split Line Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Split_Line_Example_CSharp.htm"
---

# Get Type of Split Line Example (C#)

This example shows how to get the type of split line.

```
//----------------------------------------------------------
// Preconditions:
// 1. Open a part document with a split line feature.
// 2. Select the split line feature.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets the type of split line.
// 2. Examine the Immediate window.
//-----------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace GetSplitLineType_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        SelectionMgr swSelMgr;

	        Feature swFeat;

	        SplitLineFeatureData swSplitLineFeat;

	        int splittype;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swSelMgr = (SelectionMgr)swModel.SelectionManager;

	            swFeat = (Feature)swSelMgr.GetSelectedObject6(1,
	-1);

	            swSplitLineFeat = (SplitLineFeatureData)swFeat.GetDefinition();

	            splittype = swSplitLineFeat.GetType();

	            Debug.Print("Split line type (swSplitLineFeatureType_e): " + splittype);

	        }

	        public SldWorks swApp;

	    }

	}
```

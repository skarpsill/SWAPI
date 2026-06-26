---
title: "Create Exploded Views of an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Exploded_Views_Example_CSharp.htm"
---

# Create Exploded Views of an Assembly Example (C#)

This example shows how to create multiple exploded views of an assembly.

```
//-------------------------------------------------------------
// Preconditions: Open an assembly document.
//
// Postconditions:
// 1. Press F5 and inspect the Immediate window.
// 2. Press F5 and inspect the graphics area at all
//    subsequent System.Diagnostics.Debugger.Break() statements.
//--------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace CreateExplodedViews_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        AssemblyDoc swAssembly;

	        object[] vViewName;

	        string sViewName;

	        int i;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swAssembly = (AssemblyDoc)swModel;

	            // Create five exploded views

	            for (i = 0; i <= 4; i++)

	            {

	                swAssembly.CreateExplodedView();

	            }

	            vViewName = (object[])swAssembly.GetExplodedViewNames();

	            Debug.Print("Number of exploded views created:  " + swAssembly.GetExplodedViewCount());

	            for (i = 0; i <= vViewName.GetUpperBound(0); i++)

	            {

	                sViewName = (string)vViewName[i];

	                Debug.Print("  Exploded
	view name: " + sViewName);

	            }

	            System.Diagnostics.Debugger.Break();

	            for (i = 0; i <= vViewName.GetUpperBound(0); i++)

	            {

	                sViewName = (string)vViewName[i];

	                swAssembly.ShowExploded2(true, sViewName);

	            }

	            System.Diagnostics.Debugger.Break();

	            for (i = 0; i <= vViewName.GetUpperBound(0); i++)

	            {

	                sViewName = (string)vViewName[i];

	                swAssembly.ShowExploded2(false, sViewName);

	            }

	            System.Diagnostics.Debugger.Break();

	            swAssembly.ViewExplodeAssembly();

	            System.Diagnostics.Debugger.Break();

	            swAssembly.ViewCollapseAssembly();

	        }

	        public SldWorks swApp;

	    }

	}
```

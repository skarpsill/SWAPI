---
title: "Create Polygon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Polygon_Example_CSharp.htm"
---

# Create Polygon Example (C#)

This example shows how to create a polygon.

```
//-------------------------------------------------------------------
// Preconditions: Open a part document.
//
// Postconditions:
// 1. Inserts a sketch.
// 2. Creates a six-sided polygon, circumscribed with a
//    construction circle.
// 3. Examine the graphics area.
//-------------------------------------------------------------------
using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace CreatePolygon_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        ModelDocExtension swModelDocExt;

	        SketchManager swSketchMgr;

	        Object[]
	polygon;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swModelDocExt = swModel.Extension;

	            swSketchMgr = swModel.SketchManager;

	            swSketchMgr.InsertSketch(false);

	            polygon = (Object[])swSketchMgr.CreatePolygon(-2.5,
	0.88, 0.0, -2.21, -2.13, 0.0, 6, false);

	            swModel.ViewZoomtofit2();

	            // Set the selection mode to
	default

	            swModel.SetPickMode();

	            swSketchMgr.InsertSketch(true);

	        }

	        public SldWorks swApp;

	    }

	}
```

---
title: "Create Tangent Arc in a Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Tangent_Arc_Example_CSharp.htm"
---

# Create Tangent Arc in a Sketch Example (C#)

This example shows how to create a tangent arc in a sketch.

```
//---------------------------------------------------------------------------
// Preconditions: Verify that the specified template exists.
//
// Postconditions:
// 1. Creates a new part with a sketch of a tangent arc.
// 2. Examine the graphics area.
//---------------------------------------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	using System;

	namespace CreateTangentArc_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 Part;

	        public void Main()

	        {

	            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS
	2017\\templates\\Part.prtdot", 0, 0, 0);

	            Part.SketchManager.InsertSketch(true);

	            object skSegment = null;

	            skSegment = Part.SketchManager.CreateLine(-0.060928,
	0.026745, 0.0, 0.06209, 0.002933, 0.0);

	            Part.ClearSelection2(true);

	            skSegment = Part.SketchManager.CreateTangentArc(0.06209,
	0.002933, 0.0, 0.020571, -0.021799, 0.0, 1);

	            Part.ClearSelection2(true);

	            Part.SketchManager.InsertSketch(true);

	        }

	        public SldWorks swApp;

	    }

	}
```

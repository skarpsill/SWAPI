---
title: "Save File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_File_Example_CSharp.htm"
---

# Save File Example (C#)

This example shows how to save a file.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open a model.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Zooms to fit the model in the graphics area.
// 2. Saves the model.
// 3. Examine the graphics area and Immediate window.
//------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace SaveFile_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        bool boolstatus;

	        int lErrors;

	        int lWarnings;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swApp.Visible = true;

	            // Make a change

	            swModel.ViewZoomtofit2();

	            boolstatus = swModel.Save3((int)swSaveAsOptions_e.swSaveAsOptions_Silent, ref lErrors, ref lWarnings);

	            // Errors

	            Debug.Print("Errors as defined in swFileSaveError_e: " + lErrors);

	            // Warnings

	            Debug.Print("Warnings as defined in swFileSaveWarning_e: " + lWarnings);

	        }

	        public SldWorks swApp;

	    }

	}
```

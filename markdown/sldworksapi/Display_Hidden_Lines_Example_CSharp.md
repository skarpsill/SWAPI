---
title: "Display Hidden Lines Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Hidden_Lines_Example_CSharp.htm"
---

# Display Hidden Lines Example (C#)

This example shows how to set the display mode of a model.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document.
 // 2. Press F5 five times, inspecting the graphics area each time.
 //
 // Postconditions: The display mode settings for the document are modified
 // as specified.
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
 namespace DisplayHiddenLines_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Make hidden lines visible
             swModel.ViewDisplayHiddengreyed();
             System.Diagnostics.Debugger.Break();
             // Display shaded
             swModel.ViewDisplayShaded();
             System.Diagnostics.Debugger.Break();
             // Remove hidden lines
             swModel.ViewDisplayHiddenremoved();
             System.Diagnostics.Debugger.Break();
             // Display as wireframe
             swModel.ViewDisplayWireframe();
             System.Diagnostics.Debugger.Break();
             // Toggle display of surface curvature
             swModel.ViewDisplayCurvature();
             System.Diagnostics.Debugger.Break();
             // Display the facets of the shaded model
             swModel.ViewDisplayFaceted();

         }

         public SldWorks swApp;

     }
 }
```

---
title: "Get Depth of Extrusion Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Depth_of_Extrusion_Example_CSharp.htm"
---

# Get Depth of Extrusion Example (C#)

This example shows how to get the depth of an extrusion.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part containing a Boss-Extrude1 feature.
 // 2. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate window.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace DimGetSystemValue3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             Dimension swDim = default(Dimension);
             object vConfigNames = null;
             double[] vValue = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDim = (Dimension)swModel.Parameter("D1@Boss-Extrude1");

             Debug.Assert((swDim != null));

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Full name = " + swDim.FullName);
             Debug.Print("  Name = " + swDim.Name);

             vConfigNames = swModel.GetConfigurationNames();
             vValue = (double[])swDim.GetSystemValue3((int)swInConfigurationOpts_e.swThisConfiguration, (vConfigNames));

             Debug.Print("  System value = " + vValue[0] * 1000.0 +  "" +  " mm");

         }

         public SldWorks swApp;
     }
 }
```

---
title: "Get Parameters of Conical Surface Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Conical_Surface_Example_CSharp.htm"
---

# Get Parameters of Conical Surface Example (C#)

This example shows how to get the parameters of a conical surface.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document with a conical surface.
 // 2. Select the conical surface.
 // 3. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace ConeParams2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Face2 swFace = default(Face2);
             Surface swSurf = default(Surface);
             double[] vCone = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             swSurf = (Surface)swFace.GetSurface();

             if (swSurf.IsCone())
             {
                 vCone = (double[])swSurf.ConeParams2;
                 Debug.Print("Origin               = (" + vCone[0] * 1000.0 + "mm, " + vCone[1] * 1000.0 + "mm, " + vCone[2] * 1000.0 + "mm)");
                 Debug.Print("Axis                 = (" + vCone[3] + ", " + vCone[4] + ", " + vCone[5] + ")");
                 Debug.Print("Radius               = " + vCone[6] * 1000.0 + " mm");
                 // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
                 Debug.Print("Half angle           = " + vCone[7] * 57.3 + " degrees");
                 Debug.Print("Reference direction  = (" + vCone[8] * 1000.0 + "mm, " + vCone[9] * 1000.0 + "mm, " + vCone[10] * 1000.0 + "mm)");
             }

         }

         public SldWorks swApp;

     }

 }
```

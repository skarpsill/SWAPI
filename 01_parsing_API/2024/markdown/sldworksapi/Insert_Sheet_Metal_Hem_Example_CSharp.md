---
title: "Insert Sheet Metal Hem Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Hem_Example_CSharp.htm"
---

# Insert Sheet Metal Hem Example (C#)

This example shows how to insert a hem into a sheet metal part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part.
 // 2. Select the edge to which to you can add a hem.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Adds an open hem with a custom relief of type Obround and
 //    a relief ratio of 1.0.
 // 2. Gets the hem type.
 // 3. Examine the Immediate window.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace SheetMetalHem_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CustomBendAllowance CBAObject;
         Feature myFeature;
         HemFeatureData myHem;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             CBAObject = Part.FeatureManager.CreateCustomBendAllowance();
             CBAObject.Type = 2;
             CBAObject.KFactor = 0.5;

             // Insert an open hem of custom relief type Obround and relief ratio 1.0
             myFeature = Part.FeatureManager.InsertSheetMetalHem2((int)swHemTypes_e.swHemTypeOpen, (int)swHemPositionTypes_e.swHemPositionTypeOutside, false, 0.01, 0.01, 0, 0.005, 0.0011, CBAObject,  false,
             (int)swSheetMetalReliefTypes_e.swSheetMetalReliefObround, 0, true, 1.0, 0, 0);
             Part.ClearSelection2(true);

             myHem = (HemFeatureData)myFeature.GetDefinition();
             Debug.Print("Hem type as defined in swHemTypes_e: " + myHem.Type);
         }

         public SldWorks swApp;

     }

 }
```

---
title: "Get the Direction of a Bend Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Direction_of_a_Bend_Example_CSharp.htm"
---

# Get the Direction of a Bend Example (C#)

This example shows how to get the direction of a bend in sheet metal.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part with a bend feature.
 // 2. Select the bend feature.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace GetBendDirection_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature f;

         OneBendFeatureData obe;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             f = (Feature)swModel.ISelectionManager.GetSelectedObject6(1, -1);
             obe = (OneBendFeatureData)f.GetDefinition();
             if (obe.BendDirection == 1)
             {
                 Debug.Print("Direction of the selected bend is up.");
             }
             else if (obe.BendDirection == 2)
             {
                 Debug.Print("Direction of the selected bend is down.");
             }
             else
             {
                 Debug.Print("Error getting the direction of the selected bend.");
             }
         }

         public SldWorks swApp;

     }

 }
```

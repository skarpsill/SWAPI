---
title: "Get Data for Fillet Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Simple_Fillet_Example_CSharp.htm"
---

# Get Data for Fillet Feature Example (C#)

This example shows how to get the data for the selected fillet feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document with a simple fillet feature.
 // 2. Select the simple fillet feature.
 // 3. Open the Immediate window.
 // 4. Run the macro.
 //
 // Postconditions: Inspect the Immediate window.
 //---------------------------------------------------------------------------

 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace SimpleFilletFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             SimpleFilletFeatureData2 swFillet = default(SimpleFilletFeatureData2);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swFillet = (SimpleFilletFeatureData2)swFeat.GetDefinition();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("Feature = " + swFeat.Name);
             Debug.Print("   Constant width? " + swFillet.ConstantWidth);
             Debug.Print("   Curvature continuous? " + swFillet.CurvatureContinuous);
             Debug.Print("   Default radius = " + swFillet.DefaultRadius);
             Debug.Print("   Number of fillet items = " + swFillet.FilletItemsCount);
             Debug.Print("   Multiple radii? " + swFillet.IsMultipleRadius);
             Debug.Print("   Keep existing features? " + swFillet.KeepFeatures);
             Debug.Print("   Apply fillet to attachment edges? " + swFillet.OmitAttachedEdges);
             Debug.Print("   Overflow type = " + swFillet.OverflowType);
             Debug.Print("   Extend fillet to all affected parts? " + swFillet.PropagateFeatureToParts);
             Debug.Print("   Extend fillet to all tangent faces? " + swFillet.PropagateToTangentFaces);
             Debug.Print("   Reverse normal? " + swFillet.get_ReverseFaceNormal(0));
             Debug.Print("   Round fillet corners? " + swFillet.RoundCorners);
             Debug.Print("   Trim and attach to surfaces? " + swFillet.TrimAndAttachSurfaces);
             Debug.Print("   Type of fillet? " + swFillet.Type);
              Debug.Print("   Number of faces associated with this fillet = "  + swFillet.GetFaceCount((int)swSimpleFilletWhichFaces_e.swSimpleFilletSingleRadius));

         }

         public SldWorks swApp;
     }

 }
```

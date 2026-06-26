---
title: "Get Intersect Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Intersect_Feature_Data_Example_CSharp.htm"
---

# Get Intersect Feature Data Example (C#)

This example shows how to create an intersect feature and get its data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains the following intersecting features:
 //    * Boss-Extrude1
 //    * Boss-Extrude2
 //    * Boss-Extrude3
 //    * Boss-Extrude4
 //    * Surface-Extrude1
 // 2. Add reference, Microsoft.VisualBasic, to the project.
 // 3. Open an Immediate window.
 // 4. Multi-select Surface-Extrude1, Boss-Extrude3, and  Boss-Extrude4 in the
 //    FeatureManager design tree and press F5.
 //
 // Postconditions:
 // 1. When the macro stops, inspect the blue intersect regions.
 // 2. Press F5.
 // 3. Inspect the Immediate window.
 // 4. Right-click Intersect1 in the FeatureManager design tree and click
 //    Roll Forward.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
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

 namespace ModifyIntersect_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         Feature swFeat;
         FeatureManager swFeatMgr;
         IntersectFeatureData featData;

         int intStatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swFeatMgr = swModel.FeatureManager;

             object[] vResultingBodies = null;

             vResultingBodies = (object[])swFeatMgr.PreIntersect(false);
             //Do not cap planar surface openings of intersect feature
             swModel.ClearSelection2(true);

             int i = 0;
             Body2 swBody = default(Body2);

             Debug.Print("");
             //Color the intersect regions blue
             for (i = 0; i < vResultingBodies.Length; i++)
             {
                 swBody = (Body2)vResultingBodies[i];
                 Debug.Print("Intersect region " + i + 1 +  " is a temporary body? " + swBody.IsTemporaryBody());
                 intStatus = swBody.Display3(swModel, 16711680, (int)swTempBodySelectOptions_e.swTempBodySelectOptionNone);
                 Debug.Print("Intersect region " + i + 1 +  " is displayed (0 = yes)? " + intStatus);
             }

             System.Diagnostics.Debugger.Break();
             //Observe the intersect regions

             object intToExclude = null;
             bool[] boolArr = new bool[4];
             boolArr[0] = false;
             boolArr[1] = true;
             // Exclude region, vResultingBodies(2), from the intersect feature
             boolArr[2] =  false;
             boolArr[3] = false;
             intToExclude = boolArr;
             swFeat = swFeatMgr.PostIntersect(intToExclude,  true,  false);

             Debug.Print("Feature name = " + swFeat.Name);
             featData = (IntersectFeatureData)swFeat.GetDefinition();

             Debug.Print("Merge touching regions into one body? " + featData.Merge);
             Debug.Print("Consume surfaces? " + featData.Consume);
             Debug.Print("Cap planar openings on surfaces? " + featData.CapPlanar);

             Debug.Print("Number of solids, surfaces, or planes used to create the intersect feature: " + featData.GetIntersectionsToolsCount());
             Debug.Print("Number of intersect regions: " + featData.GetIntersectionsCount());

         }

         public SldWorks swApp;

     }
 }
```

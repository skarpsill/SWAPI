---
title: "Create Table Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Table_Pattern_Example_CSharp.htm"
---

# Create Table Pattern Example (C#)

This example shows how to create a table pattern feature.

```vb
  // --------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\tablepattern.sldprt.
 // 2. Delete TPattern1.
 //
 // Postconditions:
 // 1. Creates a new TPattern1.
 // 2. Inspect the FeatureManager design tree and the graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // --------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateTablePattern_CSharp
 {
     partial class SolidWorksMacro
     {

         private TablePatternFeatureData swFeatData;
         private ModelDoc2 Part;
         private Feature swFeat;
         private FeatureManager swFeatMgr;
         private bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, true, 16, null, 0);
             boolstatus = Part.Extension.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, true, 4, null, 0);
             Part.ActivateSelectedFeature();

             double[] swPointArray = new double[6];
             swPointArray[0] = 0.04;
             swPointArray[1] = 0;
             swPointArray[2] = 0;
             swPointArray[3] = -0.025;
             swPointArray[4] = 0;
             swPointArray[5] = 0;

             swFeatMgr = Part.FeatureManager;

             swFeatData = (TablePatternFeatureData)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmTablePattern);
             swFeatData.GeometryPattern = false;
             swFeatData.PointArray = swPointArray;
             swFeatData.PropagateVisualProperty = true;
             swFeatData.UseCentroid = true;
             swFeat = swFeatMgr.CreateFeature(swFeatData);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```

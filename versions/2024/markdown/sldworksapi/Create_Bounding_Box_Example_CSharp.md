---
title: "Create Bounding Box Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bounding_Box_Example_CSharp.htm"
---

# Create Bounding Box Example (C#)

This example shows how to create a bounding box.

```vb
  //----------------------------------------------------------------------------
  // Preconditions: Open an Immediate window and ensure that the specified model to open exists.
 //
 // Postconditions:
 // 1. Creates Bounding Box in the FeatureManager design tree.
 // 2. Modifies Bounding Box.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateBoundingBox_CSharp
 {
     partial class SolidWorksMacro
     {

         private BoundingBoxFeatureData swGPData;
         private BoundingBoxFeatureData featdata;
         private ModelDoc2 Part;
         private Face2 ent;
         private Feature feat;
         private FeatureManager featmgr;
         private bool boolstatus;
         private int longstatus = 0;
         private int longwarnings = 0;

         public void Main()
         {

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", longstatus, longwarnings);
             swApp.ActivateDoc2("block20.sldprt", false, longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             featmgr = Part.FeatureManager;

             boolstatus = Part.Extension.SelectByRay(0.0108472195143463, 0.0396239999998329, -0.00101823136031953, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.0011224765174324, 2, false, 0, 0);

             ent = (Face2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             swGPData = (BoundingBoxFeatureData)featmgr.CreateDefinition((int)swFeatureNameID_e.swFmBoundingBox);
             swGPData.ReferenceFaceOrPlane = 2;
             swGPData.PlanarEntity = ent;

             feat = featmgr.CreateFeature(swGPData);
             Part.ClearSelection2(true);

             featdata = (BoundingBoxFeatureData)feat.GetDefinition();
             featdata.AccessSelections(Part, null);
             boolstatus = Part.Extension.SelectByRay(-0.0103569711794194, 0.0188454182651299, 0.049345602378537, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.0011224765174324, 2, false, 0, 0);
             ent = (Face2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             featdata.PlanarEntity = ent;
             featdata.IncludeSurfaces = true;
             featdata.IncludeHiddenBodies = true;
             feat.ModifyDefinition(featdata, Part, null);
              Debug.Print( "Diameter(m) of sphere enclosing the bounding box: " + Part.Extension.GetSphericalBoxDiameter());

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

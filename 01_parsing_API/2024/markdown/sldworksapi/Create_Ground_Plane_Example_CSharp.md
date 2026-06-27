---
title: "Create Ground Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ground_Plane_Example_CSharp.htm"
---

# Create Ground Plane Example (C#)

This example shows how to create a ground plane.

```vb
  //------------------------------------------------------------------------------
  // Preconditions: Ensure that the specified model exists.
 //
 // Postconditions: Creates Ground Plane1 in the Grond Planes folder of the
 // FeatureManager design tree And modifies it.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes to it.
  //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateGroundPlane_CSharp
 {
     partial class SolidWorksMacro
     {

         private FeatureManager featmgr;
         private GroundPlaneFeatureData swGPData;
         private GroundPlaneFeatureData featdata;
         private Face2 ent;
         private Feature feat;
         private ModelDoc2 Part;
         private AssemblyDoc swAssembly;
         private bool boolstatus;
         private int longstatus = 0;
         private int longwarnings = 0;

         public void Main()
         {

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\assem2.sldasm", 2, 0, "", longstatus, longwarnings);

             swAssembly = (AssemblyDoc)Part;
             swApp.ActivateDoc2("assem2.sldasm", false, longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;
             featmgr = Part.FeatureManager;

             boolstatus = Part.Extension.SelectByRay(-0.124913770805165, 0.118854842937424, 0.0702747343940473, -0.620586476260429, -0.617739368127351, -0.482980846978724, 0.00309726603088958, 2, true, 0, 0);

             ent = (Face2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             swGPData = (GroundPlaneFeatureData)featmgr.CreateDefinition((int)swFeatureNameID_e.swFmGroundPlane);
             swGPData.PlanarEntity = ent;

             feat = featmgr.CreateFeature(swGPData);
             Part.ClearSelection2(true);
             featdata = (GroundPlaneFeatureData)feat.GetDefinition();
             boolstatus = Part.Extension.SelectByRay(0.119119826446138, 0.00516103810082313, 0.183494239718641, -0.620586476260429, -0.617739368127351, -0.482980846978724, 0.00309726603088958, 2, false, 0, 0);
             ent = (Face2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             featdata.AccessSelections(Part, null);
             featdata.PlanarEntity = ent;
             feat.ModifyDefinition(featdata, Part, null);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```

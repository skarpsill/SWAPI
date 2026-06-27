---
title: "Modify Surface-cut Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Surface_Cut_Feature_Example_CSharp.htm"
---

# Modify Surface-cut Feature Example (C#)

This example shows how to modify a surface-cut feature.

```vb
  //-------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the part to open exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Flips the direction of the surface-cut feature.
  // 2. Examine the Immediate window.
 //
  // NOTE: Because this part is used elsewhere, do not save changes.
  //-------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace SurfCutFeatureCSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeature = default(Feature);
             SurfCutFeatureData swSurfCutFeature = default(SurfCutFeatureData);
             bool status = false;
             int errors = 0;
             int warnings = 0;
             string fileName = null;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\SurfCut.sldprt";
             swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get the surface-cut feature
             status = swModelDocExt.SelectByID2("SurfaceCut1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSurfCutFeature = (SurfCutFeatureData)swFeature.GetDefinition();
             status = swSurfCutFeature.AccessSelections(swModel, null);

             // Flip direction of surface cut
             swSurfCutFeature.Flip = true;
             Debug.Print("Surface-cut feature flipped: " + status);

             // Update definition of feature
             swFeature.ModifyDefinition(swSurfCutFeature, swModel, null);

             // Rebuild part
             swModel.EditRebuild3();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;
     }

 }
```

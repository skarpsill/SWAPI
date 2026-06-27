---
title: "Get Fixed Face of Flat-Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flat-Pattern_Feature_Example_CSharp.htm"
---

# Get Fixed Face of Flat-Pattern Feature Example (C#)

This example shows how to get the fixed face of a Flat-Pattern feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a sheet metal part and select a Flat-Pattern feature.
 //
 // Postconditions:
 // 1. Inspect the graphics area to see that the fixed face
 //    of the Flat-Pattern feature is selected.
 // 2. Press F5 to run the macro to completion.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace FixedFace2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             FlatPatternFeatureData swFlatPatt = default(FlatPatternFeatureData);
             Face2 swFixedFace = default(Face2);
             Entity swFixedFaceEntity = default(Entity);
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

             swFlatPatt = (FlatPatternFeatureData)swFeat.GetDefinition();
             bRet = swFlatPatt.AccessSelections(swModel,  null);

             swFixedFace = (Face2)swFlatPatt.FixedFace2;
             swFixedFaceEntity = (Entity)swFixedFace;
             bRet = swFixedFaceEntity.Select4(true, null);    System.Diagnostics.Debugger.Break();
   // Press F5

             swFlatPatt.ReleaseSelectionAccess();

         }

         public SldWorks swApp;

     }
 }
```

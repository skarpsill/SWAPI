---
title: "Create Sheet Metal Gusset Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sheet_Metal_Gusset_Example_CSharp.htm"
---

# Create Sheet Metal Gusset Example (C#)

This example shows how to create a sheet metal gusset feature.

```vb
 // ----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\SMGussetAPI.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Inserts Sheet Metal Gusset1.
 // 2. Press F5 and observe the modified gusset.
 // 3. Inspect the Immediate window for the flatten settings of the gusset.
 // 4. Expand Flat-Pattern in the FeatureManager design tree, right-click
 //    Flat-Pattern(1), and click Unsuppress.
 // 5. Observe the center mark and profile of the gusset in its
 //    flattened state.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace CreateSheetMetalGusset_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
           public  void Main()
          {
                   ModelDoc2 Part;
                   Feature myFeature;
                   Feature swFeat;
                   SMGussetFeatureData swFeatData;
                   bool boolstatus;

                  Part = (ModelDoc2)swApp.ActiveDoc;

                  boolstatus = Part.Extension.SelectByID2("",  "FACE", -0.0538403893476698, 0.0036701308754914, 0.05530817474488,   false, 0,   null, 0);
                  boolstatus = Part.Extension.SelectByID2("",  "FACE", -0.0177780871801474, -0.0307393226379986, 0.0341128529187245,   true, 0,   null, 0);

                  swFeatData = (SMGussetFeatureData)Part.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmSMGusset);
                  swFeatData.UseOffset =   true;
                  swFeatData.OffsetDistance = 0.05;
                  swFeatData.FlipOffset =   false;
                  swFeatData.ProfileDimensionScheme = (int)swSheetMetalGussetProfileDimType_e.swSheetMetalGussetProfileDimType_IndentDepth;
                  swFeatData.IndentDepth = 0.01;
                  swFeatData.ProfileLengthDim = 0.0;
                  swFeatData.UseAngleDimForProfile =  false;
                  swFeatData.ProfileHeightDim = 0.0;
                  swFeatData.ProfileAngleDim = 0.0;
                  swFeatData.FlipDimSides =   false;
                  swFeatData.IndentWidth = 0.01;
                  swFeatData.GussetThickness = 0.003;
                  swFeatData.DraftAngle = 3 * 0.0175;
                  swFeatData.DraftSideFaces =   true;
                  swFeatData.FilletInnerCorners =   true;
                  swFeatData.InnerCornerFilletRadius = 0.002;
                  swFeatData.FilletOuterCorners =   true;
                  swFeatData.OuterCornerFilletRadius = 0.001;
                  swFeatData.GussetType = (int)swSheetMetalRibGussetType_e.swSheetMetalRibGussetType_Rounded;
                  swFeatData.FilletGussetEdges =   false;
                  swFeatData.EdgeFilletRadius = 0.0;
                  swFeatData.OverrideDocSettings =   true;
                  swFeatData.ShowProfile =   true;
                  swFeatData.ShowCenter =   true;

                  myFeature = Part.FeatureManager.CreateFeature(swFeatData);
                  Part.ClearSelection2(true);

                  System.Diagnostics.Debugger.Break();

                   // Modify type, draft, and outer corner fillet properties of the gusset
                  boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset1",   "BODYFEATURE", 0, 0, 0,   false, 0,   null, 0);
                  swFeat = (Feature)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);

                  swFeatData = (SMGussetFeatureData)swFeat.GetDefinition();
                  swFeatData.AccessSelections(Part,  null);
                  swFeatData.GussetType = (int)swSheetMetalRibGussetType_e.swSheetMetalRibGussetType_Flat;
                  swFeatData.DraftSideFaces =   false;
                  swFeatData.FilletOuterCorners =   false;
                   Debug.Print("Sheet Metal Gusset1 Flatten Settings");
                   Debug.Print("  Override document flat pattern properties? " + swFeatData.OverrideDocSettings);
                   Debug.Print("  Show center marks of the gusset in its flattened state? " + swFeatData.ShowCenter);
                   Debug.Print("  Show profile of the gusset in its flattened state? " + swFeatData.ShowProfile);

                  swFeat.ModifyDefinition(swFeatData, Part,  null);
                  swFeatData.ReleaseSelectionAccess();
              }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```

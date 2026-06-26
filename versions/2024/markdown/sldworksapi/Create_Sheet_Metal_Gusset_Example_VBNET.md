---
title: "Create Sheet Metal Gusset Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sheet_Metal_Gusset_Example_VBNET.htm"
---

# Create Sheet Metal Gusset Example (VB.NET)

This example shows how to create a sheet metal gusset feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\SMGussetAPI.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Inserts Sheet Metal Gusset1.
 ' 2. Press F5 and observe the modified gusset.
 ' 3. Inspect the Immediate window for the flatten settings of the gusset.
 ' 4. Expand Flat-Pattern in the FeatureManager design tree, right-click
 '    Flat-Pattern(1), and click Unsuppress.
 ' 5. Observe the center mark and profile of the gusset in its
 '    flattened state.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

           Dim Part  As  ModelDoc2
           Dim myFeature   As   Feature
           Dim swFeat  As  Feature
           Dim swFeatData   As   SMGussetFeatureData
           Dim boolstatus   As   Boolean
          Part = swApp.ActiveDoc

          boolstatus = Part.Extension.SelectByID2("",  "FACE", -0.0538403893476698, 0.0036701308754914, 0.05530817474488,   False, 0,   Nothing, 0)
          boolstatus = Part.Extension.SelectByID2("",  "FACE", -0.0177780871801474, -0.0307393226379986, 0.0341128529187245,  True, 0,  Nothing, 0)

          swFeatData = Part.FeatureManager.CreateDefinition(swFeatureNameID_e.swFmSMGusset)
          swFeatData.UseOffset =   True
          swFeatData.OffsetDistance = 0.05
          swFeatData.FlipOffset =   False
          swFeatData.ProfileDimensionScheme =   swSheetMetalGussetProfileDimType_e.swSheetMetalGussetProfileDimType_IndentDepth
          swFeatData.IndentDepth = 0.01
          swFeatData.ProfileLengthDim = 0#
          swFeatData.UseAngleDimForProfile =   False
          swFeatData.ProfileHeightDim = 0#
          swFeatData.ProfileAngleDim = 0#
          swFeatData.FlipDimSides =   False
          swFeatData.IndentWidth = 0.01
          swFeatData.GussetThickness = 0.003
          swFeatData.DraftAngle = 3 * 0.0175
          swFeatData.DraftSideFaces =   True
          swFeatData.FilletInnerCorners =   True
          swFeatData.InnerCornerFilletRadius = 0.002
          swFeatData.FilletOuterCorners =   True
          swFeatData.OuterCornerFilletRadius = 0.001
          swFeatData.GussetType =   swSheetMetalRibGussetType_e.swSheetMetalRibGussetType_Rounded
          swFeatData.FilletGussetEdges =   False
          swFeatData.EdgeFilletRadius = 0#
          swFeatData.OverrideDocSettings =   True
          swFeatData.ShowProfile =   True
          swFeatData.ShowCenter =   True

          myFeature = Part.FeatureManager.CreateFeature(swFeatData)
          Part.ClearSelection2(True)

           Stop

           'Modify type, draft, and outer corner fillet properties of the gusset
          boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset1",   "BODYFEATURE", 0, 0, 0,   False, 0,   Nothing, 0)
          swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)

          swFeatData = swFeat.GetDefinition
          swFeatData.AccessSelections(Part,   Nothing)
          swFeatData.GussetType =   swSheetMetalRibGussetType_e.swSheetMetalRibGussetType_Flat
          swFeatData.DraftSideFaces =   False
          swFeatData.FilletOuterCorners =   False
           Debug.Print("Sheet Metal Gusset1 Flatten Settings")
           Debug.Print("  Override document flat pattern properties? " & swFeatData.OverrideDocSettings)
           Debug.Print("  Show center marks of the gusset in its flattened state? " & swFeatData.ShowCenter)
           Debug.Print("  Show profile of the gusset in its flattened state? " & swFeatData.ShowProfile)

          swFeat.ModifyDefinition(swFeatData, Part,  Nothing)
          swFeatData.ReleaseSelectionAccess

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```

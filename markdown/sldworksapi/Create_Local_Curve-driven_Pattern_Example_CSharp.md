---
title: "Create Local Curve-Driven Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Curve-driven_Pattern_Example_CSharp.htm"
---

# Create Local Curve-Driven Pattern Example (C#)

This example shows how to create a local curve-driven pattern feature.

```
//------------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly document.
// 2. Selects the component and edge for the
//    local curve-driven pattern feature.
// 3. Creates a local curve-driven pattern feature.
// 4. Gets values and settings of the local curve-driven
//    pattern feature.
// 5. Examine the Immediate window and graphics area.
//
// NOTE: Because this assembly is used elsewhere, do not save
// changes.
//------------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FeatureLocalCurveDrivenCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
         ModelDoc2 swModel = default(ModelDoc2);
	ModelDocExtension swModelDocExt = default(ModelDocExtension);
	FeatureManager swFeatMgr = default(FeatureManager);
	Feature swFeat = default(Feature);
	LocalCurvePatternFeatureData swLocalCurvePatternFeat = default(LocalCurvePatternFeatureData);
	string fileName = null;
	bool status = false;
	int errors = 0;
	int warnings = 0;

	//Open assembly document
	fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\assem20.sldasm";
	swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

	//Select a component and an edge
	//for the local curve-driven pattern
	swModelDocExt = (ModelDocExtension)swModel.Extension;
	status = swModelDocExt.SelectByID2("block20-1@assem20", "COMPONENT", 0, 0, 0, false, 1, null, 0);
	status = swModelDocExt.SelectByID2("", "EDGE", 0.131144367102934, 0.0844607238593085, -0.124705856534547, true, 2, null, 0);

	//Create local curve-driven pattern feature
	swFeatMgr = (FeatureManager)swModel.FeatureManager;

	swLocalCurvePatternFeat = (LocalCurvePatternFeatureData)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmLocalCurvePattern);
        swLocalCurvePatternFeat.D1AlignmentMethod = 1;
        swLocalCurvePatternFeat.D1CurveMethod = 1;
        swLocalCurvePatternFeat.D1InstanceCount = 3;
        swLocalCurvePatternFeat.D1IsEqualSpaced = true;
        swLocalCurvePatternFeat.D1ReferencePoint = 1;
        swLocalCurvePatternFeat.D1ReverseDirection = false;
        swLocalCurvePatternFeat.D1Spacing = 0.05;
        swLocalCurvePatternFeat.D2InstanceCount = 1;
        swLocalCurvePatternFeat.D2IsEqualSpaced = false;
        swLocalCurvePatternFeat.D2PatternSeedOnly = false;
        swLocalCurvePatternFeat.D2ReverseDirection = false;
        swLocalCurvePatternFeat.D2Spacing = 0.05;
        swLocalCurvePatternFeat.Dir2Specified = false;
        swFeat = (Feature)swFeatMgr.CreateFeature(swLocalCurvePatternFeat);

	//Get local curve-driven pattern feature data
	swLocalCurvePatternFeat = (LocalCurvePatternFeatureData)swFeat.GetDefinition();
	Debug.Print("Local curve-driven pattern properties: ");
	Debug.Print("  Number of components: " + swLocalCurvePatternFeat.GetPatternComponentCount());
	Debug.Print("  Number of skipped items: " + swLocalCurvePatternFeat.GetSkippedItemCount());
	Debug.Print("  Direction 1: ");
	Debug.Print("     Number of pattern instances: " + swLocalCurvePatternFeat.D1InstanceCount);
	Debug.Print("     Is direction flipped: " + swLocalCurvePatternFeat.D1ReverseDirection);
	Debug.Print("     Pattern instances equal spaced: " + swLocalCurvePatternFeat.D1IsEqualSpaced);
	Debug.Print("     Spacing for pattern instances: " + swLocalCurvePatternFeat.D1Spacing);
	Debug.Print("     Curve method: " + swLocalCurvePatternFeat.D1CurveMethod);
	Debug.Print("     Alignment method: " + swLocalCurvePatternFeat.D1AlignmentMethod);
	Debug.Print("  Direction 2:");
	Debug.Print("     Is Direction 2 specified: " + swLocalCurvePatternFeat.Dir2Specified);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

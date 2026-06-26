---
title: "Insert Sweep Cut Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sweep_Cut_Feature_Example_CSharp.htm"
---

# Insert Sweep Cut Feature Example (C#)

This example shows how to create a swept-ut feature and get its properties.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open an Immediate window.
//
// Postconditions:
// 1. Creates Cut-Sweep1.
// 2. Inspect the FeatureManager design tree, graphics area,
//    and Immediate window.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//---------------------------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System;

	using System.Diagnostics;

	namespace InsertSweepCut_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 Part;

	        bool boolstatus;

	        int longstatus;

	        int longwarnings;

	        SweepFeatureData swSweep;

	        Feature swProfFeat;

	        Sketch swProfSketch;

	        Feature swPathFeat;

	        Sketch swPathSketch;

	        bool bRet;

	        public void Main()

	        {

	            Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS
	2018\\samples\\tutorial\\api\\sweepcutextrude.SLDPRT",
	1, 0, "", ref longstatus, ref longwarnings);

	            swApp.ActivateDoc2("sweepcutextrude.SLDPRT", false, ref longstatus);

	            Part = (ModelDoc2)swApp.ActiveDoc;

	            ModelView myModelView = null;

	            myModelView = (ModelView)Part.ActiveView;

	            myModelView.FrameLeft = 0;

	            myModelView.FrameTop = 0;

	            myModelView.FrameState = (int)swWindowState_e.swWindowMaximized;

	            Part.ShowNamedView2("*Isometric",
	7);

	            boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH",
	0.01948983274156, -0.02564816935317, 0, false, 1, null, 0);

	            // profile has Mark = 1

	            boolstatus =
	Part.Extension.SelectByID2("Sketch3", "SKETCH",
	-0.03797488317814, -0.02133214444164, 0, true, 4, null, 0);

	            // path sweep has Mark = 4

	            Feature myFeature = default(Feature);

	            myFeature = Part.FeatureManager.InsertCutSwept4(false, true, 0, false, false, 0,
	0, false,
	0, 0,

	            0, 0, true, true, 0, true, true, true, false);

	            swSweep = (SweepFeatureData)myFeature.GetDefinition();

	            swProfFeat = (Feature)swSweep.Profile;

	            Debug.Assert((null != swProfFeat));

	            swProfSketch = (Sketch)swProfFeat.GetSpecificFeature();

	            Debug.Assert((null != swProfSketch));

	            bRet = swSweep.AccessSelections(Part, null);

	            Debug.Assert(bRet);

	            swPathFeat = (Feature)swSweep.Path;

	            Debug.Assert((null != swPathFeat));

	            swPathSketch = (Sketch)swPathFeat.GetSpecificFeature();

	            Debug.Assert((null != swPathSketch));

	            Debug.Print("File = " + Part.GetPathName());

	            Debug.Print("
	" + myFeature.Name);

	            Debug.Print("
	Path = " + swPathFeat.Name);

	            //swTangencyType_e

	            Debug.Print("
	Path alignment type = " + swSweep.PathAlignmentType);

	            Debug.Print("
	Profile = " + swProfFeat.Name);

	            Debug.Print(" AdvancedSmoothing = " + swSweep.AdvancedSmoothing);

	            Debug.Print(" AlignWithEndFaces = " + swSweep.AlignWithEndFaces);

	            Debug.Print(" AutoSelect = " + swSweep.AutoSelect);

	            Debug.Print(" AutoSelectComponents = " + swSweep.AutoSelectComponents);

	            Debug.Print(" EndTangencyType = " + swSweep.EndTangencyType);

	            Debug.Print(" AssemblyFeatureScope = " + swSweep.AssemblyFeatureScope);

	            Debug.Print(" FeatureScope = " + swSweep.FeatureScope);

	            Debug.Print(" FeatureScopeBodiesCnt = " + swSweep.GetFeatureScopeBodiesCount());

	            //swSelectType_e

	            Debug.Print(" GetPathType = " + swSweep.GetPathType());

	            Debug.Print("
	Wall thickness foward = " + swSweep.GetWallThickness(true)
	* 1000.0 + " mm");

	            Debug.Print("
	Wall thickness reverse = " + swSweep.GetWallThickness(false)
	* 1000.0 + " mm");

	            Debug.Print(" IsBossFeature = " + swSweep.IsBossFeature());

	            Debug.Print(" IsThinFeature = " + swSweep.IsThinFeature());

	            Debug.Print(" MaintainTangency = " + swSweep.MaintainTangency);

	            Debug.Print("
	Merge = " + swSweep.Merge);

	            Debug.Print(" MergeSmoothFaces = " + swSweep.MergeSmoothFaces);

	            Debug.Print(" PropagateFeatureToParts = " + swSweep.PropagateFeatureToParts);

	            Debug.Print(" StartTangencyType = " + swSweep.StartTangencyType);

	            Debug.Print(" TangentPropagation = " + swSweep.TangentPropagation);

	            Debug.Print(" ThinWallType = " + swSweep.ThinWallType);

	            //swTwistControlType_e

	            Debug.Print(" TwistControlType = " + swSweep.TwistControlType);

	            //swCutSweepOption_e

	            Debug.Print(" CutSweepOption = " + swSweep.GetCutSweepOption());

	            swSweep.ReleaseSelectionAccess();

	        }

	        public SldWorks swApp;

	    }

	}
```

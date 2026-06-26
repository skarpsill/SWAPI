---
title: "Insert Sweep Cut Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sweep_Cut_Feature_Example_VBNET.htm"
---

# Insert Sweep Cut Feature Example (VB.NET)

This example shows how to create a swept-cut feature and get its properties.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates Cut-Sweep1.
' 2. Inspect the FeatureManager design tree, graphics area,
'    and Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'---------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim boolstatus As Boolean

	    Dim longstatus As Long, longwarnings As Long

	    Dim swSweep As SweepFeatureData

	    Dim swProfFeat As Feature

	    Dim swProfSketch As Sketch

	    Dim swPathFeat As Feature

	    Dim swPathSketch As Sketch

	    Dim bRet As Boolean

	    Sub main()

	        Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS
	2018\samples\tutorial\api\sweepcutextrude.SLDPRT",
	1, 0, "", longstatus, longwarnings)

	        swApp.ActivateDoc2("sweepcutextrude.SLDPRT", False, longstatus)

	        Part = swApp.ActiveDoc

	        Dim myModelView As Object

	        myModelView = Part.ActiveView

	        myModelView.FrameLeft = 0

	        myModelView.FrameTop = 0

	        myModelView.FrameState = swWindowState_e.swWindowMaximized

	        Part.ShowNamedView2("*Isometric",
	7)

	        boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH",
	0.01948983274156, -0.02564816935317, 0, False, 1, Nothing, 0) ' profile has Mark = 1

	        boolstatus =
	Part.Extension.SelectByID2("Sketch3", "SKETCH",
	-0.03797488317814, -0.02133214444164, 0, True, 4, Nothing, 0) ' path sweep has Mark = 4

	        Dim myFeature As Feature

	        myFeature = Part.FeatureManager.InsertCutSwept4(False, True, 0, False, False, 0,
	0, False,
	0, 0, 0, 0, True, True, 0, True, True, True, False)

	        swSweep = myFeature.GetDefinition

	        swProfFeat = swSweep.Profile : Debug.Assert(Not Nothing Is swProfFeat)

	        swProfSketch = swProfFeat.GetSpecificFeature : Debug.Assert(Not Nothing Is swProfSketch)

	        bRet = swSweep.AccessSelections(Part, Nothing) : Debug.Assert(bRet)

	        swPathFeat = swSweep.Path : Debug.Assert(Not Nothing Is swPathFeat)

	        swPathSketch = swPathFeat.GetSpecificFeature : Debug.Assert(Not Nothing Is swPathSketch)

	        Debug.Print("File = " & Part.GetPathName)

	        Debug.Print("  " & myFeature.Name)

	        Debug.Print("    Path                      =
	" & swPathFeat.Name)

	        Debug.Print("    Path alignment
	type       = " & swSweep.PathAlignmentType) 'swTangencyType_e

	        Debug.Print("    Profile
	= " & swProfFeat.Name)

	        Debug.Print("    AdvancedSmoothing
	= " & swSweep.AdvancedSmoothing)

	        Debug.Print("    AlignWithEndFaces
	= " & swSweep.AlignWithEndFaces)

	        Debug.Print("    AutoSelect                =
	" & swSweep.AutoSelect)

	        Debug.Print("    AutoSelectComponents      =
	" & swSweep.AutoSelectComponents)

	        Debug.Print("    EndTangencyType
	= " & swSweep.EndTangencyType)

	        Debug.Print("    AssemblyFeatureScope      =
	" & swSweep.AssemblyFeatureScope)

	        Debug.Print("    FeatureScope              =
	" & swSweep.FeatureScope)

	        Debug.Print("    FeatureScopeBodiesCnt
	= " & swSweep.GetFeatureScopeBodiesCount)

	        Debug.Print("    GetPathType
	= " & swSweep.GetPathType)       'swSelectType_e

	        Debug.Print("    Wall thickness foward     = " & swSweep.GetWallThickness(True)
	* 1000.0# & " mm")

	        Debug.Print("    Wall thickness
	reverse    = " & swSweep.GetWallThickness(False)
	* 1000.0# & " mm")

	        Debug.Print("    IsBossFeature
	= " & swSweep.IsBossFeature)

	        Debug.Print("    IsThinFeature
	= " & swSweep.IsThinFeature)

	        Debug.Print("    MaintainTangency          =
	" & swSweep.MaintainTangency)

	        Debug.Print("    Merge
	= " & swSweep.Merge)

	        Debug.Print("    MergeSmoothFaces          =
	" & swSweep.MergeSmoothFaces)

	        Debug.Print("    PropagateFeatureToParts
	= " & swSweep.PropagateFeatureToParts)

	        Debug.Print("    StartTangencyType
	= " & swSweep.StartTangencyType)

	        Debug.Print("    TangentPropagation        =
	" & swSweep.TangentPropagation)

	        Debug.Print("    ThinWallType              =
	" & swSweep.ThinWallType)

	        Debug.Print("    TwistControlType          =
	" & swSweep.TwistControlType)  'swTwistControlType_e

	        Debug.Print("    CutSweepOption            =
	" & swSweep.GetCutSweepOption)  'swCutSweepOption_e

	        swSweep.ReleaseSelectionAccess()

	    End Sub

	    Public swApp As SldWorks

	End Class
```

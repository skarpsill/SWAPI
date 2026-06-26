---
title: "Insert Swept-cut Feature Using Sketch Profile Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Swept_Cut_Feature_Example_VB.htm"
---

# Insert Swept-cut Feature Using Sketch Profile Example (VBA)

This example shows how to create a swept-cut feature using a sketch profile and get its properties.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates Cut-Sweep1.
' 2. Inspect the FeatureManager design tree, graphics area,
'    and Immediate window.
'
' NOTE: Because this part document is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Dim swSweep As SldWorks.SweepFeatureData
 Dim swProfFeat As SldWorks.Feature
 Dim swProfSketch As SldWorks.Sketch
 Dim swPathFeat As SldWorks.Feature
 Dim swPathSketch As SldWorks.Sketch
 Dim bRet As Boolean
 Dim myModelView As Object
 Dim myFeature As SldWorks.Feature

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\sweepcutextrude.SLDPRT", 1, 0, "", longstatus, longwarnings)
swApp.ActivateDoc2 "sweepcutextrude.SLDPRT", False, longstatus
Set Part = swApp.ActiveDoc

Set myModelView = Part.ActiveView
myModelView.FrameLeft = 0
myModelView.FrameTop = 0
myModelView.FrameState = swWindowState_e.swWindowMaximized
Part.ShowNamedView2 "*Isometric", 7
boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0.01948983274156, -0.02564816935317, 0, False, 1, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("Sketch3", "SKETCH", -0.03797488317814, -0.02133214444164, 0, True, 4, Nothing, 0)

Set swSweep = Part.FeatureManager.CreateDefinition(swFmSweepCut)

 swSweep.TwistControlType = 0

 swSweep.PathAlignmentType = 0

 swSweep.CircularProfile = False

 Set myFeature = Part.FeatureManager.CreateFeature(swSweep)
Set swSweep = myFeature.GetDefinition
Set swProfFeat = swSweep.Profile
Set swProfSketch = swProfFeat.GetSpecificFeature

bRet = swSweep.AccessSelections(Part, Nothing)
Set swPathFeat = swSweep.Path
Set swPathSketch = swPathFeat.GetSpecificFeature
Debug.Print "File = " & Part.GetPathName
Debug.Print "  " & myFeature.Name
Debug.Print "    Sweep path  = " & swPathFeat.Name
 Debug.Print "    Path type as defined in swSelectType_e  = " & swSweep.GetPathType
Debug.Print "    Path alignment type as defined in swTangencyType_e  = " & swSweep.PathAlignmentType
Debug.Print "    Sweep Profile  = " & swProfFeat.Name
 Debug.Print "    Profile type as defined in swSelectType_e  = " & swSweep.GetProfileType
 Debug.Print "    Profile orientation/twist type as defined in swTwistControlType_e  = " & swSweep.TwistControlType
Debug.Print "    Cut sweep type as defined in swCutSweepOption_e    = " & swSweep.GetCutSweepOption
Debug.Print "    Align sweep with end faces? " & swSweep.AlignWithEndFaces
Debug.Print "    Automatically select all bodies to be affected if a multibody part? " & swSweep.AutoSelect
 Debug.Print "    Start of sweep tangency type as defined in swTangencyType_e   = " & swSweep.StartTangencyType
Debug.Print "    End of sweep tangency type as defined in swTangencyType_e   = " & swSweep.EndTangencyType
Debug.Print "    Only specific bodies affected by this sweep feature? " & swSweep.FeatureScope
Debug.Print "    Feature scope bodies count = " & swSweep.GetFeatureScopeBodiesCount
Debug.Print "    Is a boss feature? " & swSweep.IsBossFeature
Debug.Print "    Is a thin-walled feature? " & swSweep.IsThinFeature
 Debug.Print "    Thin-walled type (0=1D, 1=1DReverse, 2=MidPlane, 3=2D)  = " & swSweep.ThinWallType
 Debug.Print "    Wall thickness Direction 1  = " & swSweep.GetWallThickness(True) * 1000# & " mm"
Debug.Print "    Wall thickness Direction 2  = " & swSweep.GetWallThickness(False) * 1000# & " mm"
Debug.Print "    Merge tangent faces? " & swSweep.MaintainTangency
Debug.Print "    Merge results if a multibody part? " & swSweep.Merge
Debug.Print "    Merge smooth faces if using guide curves? " & swSweep.MergeSmoothFaces
swSweep.ReleaseSelectionAccess
```

```vb
End Sub
```

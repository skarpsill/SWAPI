---
title: "Insert Swept-cut Thin-walled Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Swept-cut_Thin-walled_Feature_Example_VB.htm"
---

# Insert Swept-cut Thin-walled Feature Example (VBA)

This example shows how to create a swept-cut thin-walled feature.

```vb
 '---------------------------------------------------------------
 ' Preconditions: Verify that the specified part exists.
 '
 ' Postconditions:
 ' 1. Creates a thin-walled swept-cut feature.
 ' 2. Examine the FeatureManager design tree and graphics area.
 '---------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSketchMgr As SldWorks.SketchManager
 Dim swSketchSegment As SldWorks.SketchSegment
 Dim swFeature As SldWorks.Feature
 Dim swPathFeat As SldWorks.Feature
 Dim swFeatureMgr As SldWorks.FeatureManager
 Dim swSelectionMgr As SldWorks.SelectionMgr
 Dim swSweepFeatureData As SldWorks.SweepFeatureData
 Dim swSweep As SldWorks.SweepFeatureData
 Dim swProfileObj As Object
 Dim swProfileBody As SldWorks.Body2
 Dim swPathFeature As SldWorks.Feature
 Dim sketchLines As Variant
 Dim status As Boolean
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long

 Sub main()

     Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\sweepcutextrude.SLDPRT", 1, 0, "", longstatus, longwarnings)

    boolstatus = swModel.Extension.SelectByID2("Sketch2", "SKETCH", 0.01948983274156, -0.02564816935317, 0, False, 1, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("Sketch3", "SKETCH", -0.03797488317814, -0.02133214444164, 0, True, 4, Nothing, 0)

    Set swSweep = swModel.FeatureManager.CreateDefinition(swFmSweepCut)

    swSweep.TwistControlType = 0
     swSweep.PathAlignmentType = 0
     swSweep.ThinFeature = True
     swSweep.SetWallThickness True, 0.001 'Meters in Direction 1
     swSweep.SetWallThickness False, 0.001 'Meters in Direction 2
     swSweep.ThinWallType = 3 '2 Directions
     swSweep.TangentPropagation = False
     swSweep.AlignWithEndFaces = True
     swSweep.MaintainTangency = False
     swSweep.AdvancedSmoothing = False
     swSweep.StartTangencyType = 0
     swSweep.EndTangencyType = 0
     swSweep.FeatureScope = True
     swSweep.AutoSelect = True
     swSweep.SetTwistAngle 0#
     swSweep.MergeSmoothFaces = True
     swSweep.AssemblyFeatureScope = True
     swSweep.AutoSelectComponents = True
     swSweep.PropagateFeatureToParts = False
     swSweep.CircularProfile = False
     swSweep.CircularProfileDiameter = 0#
    Set swPathFeat = swModel.FeatureManager.CreateFeature(swSweep)

End Sub
```

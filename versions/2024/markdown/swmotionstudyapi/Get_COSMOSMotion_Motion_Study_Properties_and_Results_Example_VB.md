---
title: "Get COSMOSMotion Motion Study Properties and Results Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm"
---

# Get COSMOSMotion Motion Study Properties and Results Example (VBA)

This example shows how to get a COSMOSMotion motion study's properties
and results.

'------------------------------------------

' Preconditions: Model is open that has a COSMOSMotion
motion study

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}named
PhysSim and at least one COSMOSMotion motion study plot.

'

' Postconditions: None

'--------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swMotionMgr As SwMotionStudy.MotionStudyManager

Dim swMotionStudy1 As SwMotionStudy.MotionStudy

Dim swResults As SwMotionStudy.MotionStudyResults

Dim swMotionStudyProps As SwMotionStudy.MotionStudyProperties

Dim swCosmosMotionStudyProps As SwMotionStudy.CosmosMotionStudyProperties

Dim swCosmosMotionStudyResults As SwMotionStudy.CosmosMotionStudyResults

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the MotionManager.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionMgr = swModelDocExt.GetMotionStudyManager()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionMgr Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get motion study named PhysSim.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionStudy1 = swMotionMgr.GetMotionStudy("PhysSim")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionStudy1 Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"PhysSim is not available."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMotionStudy1.StudyType
= swMotionStudyType_e.swMotionStudyTypePhysicalSimulation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Is
the motion study active?kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
not, activate it.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swMotionStudy1.IsActiveThen
swMotionStudy1.Activate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Duration of motion study: " & swMotionStudy1.GetDuration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Timebar position on timeline: " & swMotionStudy1.GetTime

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Number of motion features: " & swMotionStudy1.GetMotionFeaturesCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Get
COSMOSMotion study properties.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionStudyProps = swMotionStudy1.GetProperties(4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCosmosMotionStudyProps = swMotionStudyProps

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"COSMOSMotion study properties: "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Animate
during simulation: " & swCosmosMotionStudyProps.AnimateDuringSimulation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Make
all mates flexible: " & swCosmosMotionStudyProps.MakeAllMatesFlexible

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Display
results graphics as wireframe: " & swCosmosMotionStudyProps.WireframeGraphics

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get COSMOSMotion study results.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swResults = swMotionStudy1.GetResults(4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCosmosMotionStudyResults = swResults

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Number
of plots: " & swCosmosMotionStudyResults.GetPlotCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Are the motion study results out of date? " & swResults.IsOutOfDate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

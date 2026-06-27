---
title: "Create Motion Studies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Motion_Studies_Example_VB.htm"
---

# Create Motion Studies Example (VBA)

This example shows how to create, rename, and delete motion studies.

'--------------------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part or assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
MotionManager tab is visible. If it is not visible,

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}click
View, MotionManager.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(3)
SOLIDWORKSnnnnMotionStudy Type
Library, where

kadov_tag{{<spaces>}}nnnnis
the version number of the release, is

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}selected
on Tools, References.

'

' Postconditions: Two motion studies exist: Motion Study
1 and TestName.

'

'-------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swMotionMgr As SwMotionStudy.MotionStudyManager

Dim swMotionStudy1 As SwMotionStudy.MotionStudy

Dim swMotionStudy2 As SwMotionStudy.MotionStudy

Dim swMotionStudy3 As SwMotionStudy.MotionStudy

Dim swSaveAVIData As SwMotionStudy.AVIParameter

Dim boolstatus As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the MotionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionMgr = swModelDocExt.GetMotionStudyManager()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionMgr Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create new motion studies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionStudy2 = swMotionMgr.CreateMotionStudy()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionStudy2 Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Motion Study 2 is not available."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionStudy3 = swMotionMgr.CreateMotionStudy()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionStudy3 Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Motion Study 3 is not available."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get number of motion studies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Number of motion studies = " & swMotionMgr.GetMotionStudyCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get motion study

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion
Study 1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swMotionStudy1 Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Motion Study 1 is not available."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get number and names of motion studies and whether they've been activated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vNames As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vNames
= swMotionMgr.GetMotionStudyNames()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vNames)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
vNames(i);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swMotionMgr.ActivateMotionStudy(vNames(i))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" activated = " & boolstatus

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Attempt to activate a non-existing motion study

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swMotionMgr.ActivateMotionStudy("Motion
Study 4") ' Should return False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Motion Study 4 activated = " & boolstatus

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Delete Motion Study2 and non-existing motion study

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swMotionMgr.DeleteMotionStudy("Motion
Study 2")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Motion Study 2 deleted = " & boolstatus

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swMotionMgr.DeleteMotionStudy("Motion
Study 4")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Motion Study 4 deleted = " & boolstatus ' Should return
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Rename Motion Study 3 to TestName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMotionStudy3.Name= "TestName"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set and save AVI parameters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSaveAVIData = swMotionMgr.CreateAVIParameter()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSaveAVIData.FramePerSecond= 7.5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSaveAVIData.SaveEntireAnimation= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSaveAVIData.OutputType= 1 ' Save as an .avi file

End Sub

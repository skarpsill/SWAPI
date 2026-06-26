---
title: "Move Selected Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Selected_Face_Example_VB.htm"
---

# Move Selected Face Example (VBA)

This example shows how to move the selected face in a part.

'-------------------------------------

'

' Preconditions: Part is open.

'

' Postconditions: The selected face is moved.

'

'-------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swFeatMgr As SldWorks.FeatureManager

Dim swFeat As SldWorks.Feature

Dim boolstatus As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeatMgr = swModel.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select face to move

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("",
"FACE", -0.06133102397996, 0.0499999999999, 0.02353079473198,
False, 1, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the direction reference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("",
"EDGE", -0.05000883624581, 0.02773250193934, 0.04000883624559,
True, 2, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Move the selected face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swFeatMgr.InsertMoveFace(1,
False, 0.034907, 0.05)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ViewZoomtofit2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

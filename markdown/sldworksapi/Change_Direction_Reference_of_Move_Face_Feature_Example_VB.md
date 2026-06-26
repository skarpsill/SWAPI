---
title: "Change Direction Reference of Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Direction_Reference_of_Move_Face_Feature_Example_VB.htm"
---

# Change Direction Reference of Move Face Feature Example (VBA)

This example shows how to change the reference direction of aMove Facefeature.

'-----------------------------------------------------

'

' Preconditions: Part is open that has a Move Face feature.

'

' Postconditions: The selected edge becomes the new

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}direction
reference for the Move Face feature.

'

'-----------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFeat As SldWorks.Feature

Dim swMoveFaceFeat As SldWorks.MoveFaceFeatureData

Dim swEntity As SldWorks.Entity

Dim boolstatus As Boolean

Dim dirType As Long

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("Move
Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMoveFaceFeat = swFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll back the Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMoveFaceFeat.AccessSelectionsswModel, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the current direction reference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEntity = swMoveFaceFeat.GetDirectionReference(dirType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEntity.Select4False, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear the selection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select a different edge for the direction reference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("",
"EDGE", -0.05047526142499, 0.03085263679878, 0.04047526142483,
False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEntity = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set the direction reference to the just-selected edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMoveFaceFeat.SetDirectionReferenceswEntity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll back the part with the modified Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeat.ModifyDefinitionswMoveFaceFeat, swModel,
Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

---
title: "Change Faces of Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Faces_of_Move_Face_Feature_Example_VB.htm"
---

# Change Faces of Move Face Feature Example (VBA)

This example shows how to modify a Move Face feature by changing the
defining faces.

'-----------------------------------------

'

' Preconditions: Part is open that has a Move Face feature.

'

' Postcondtiions: The selected new face now defines the
Move Face

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}feature.

'

'-----------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFeat As SldWorks.Feature

Dim swMoveFaceFeat As SldWorks.MoveFaceFeatureData

Dim swEnt As SldWorks.Entity

Dim vFaces As Variant

Dim pFace As Variant

Dim vNewFaces As Variant

Dim pNewFace As Variant

Dim pNewFaceArr(0) As Object

Dim boolstatus As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the Move Face feature

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Find and clear the faces that define the Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFaces
= swMoveFaceFeat.Faces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each pFace In vFaces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEnt = pFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEnt.Select4False, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select a new face for the Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("",
"FACE", 0.06393265679355, 0.04999999999984, 0.01806458069194,
False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pNewFace = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pNewFaceArr(0) = pNewFace

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vNewFaces
= pNewFaceArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set the new face for the Move Face feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMoveFaceFeat.Faces= vNewFaces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Modify the Move Face feature and roll back the feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeat.ModifyDefinitionswMoveFaceFeat, swModel,
Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

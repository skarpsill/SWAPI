---
title: "Move and Copy Body by Setting Transforms Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm"
---

# Move and Copy Body by Setting Transforms Example (VBA)

This example shows how to move and copy bodies by setting transforms.

'----------------------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part document is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Body-Move/Copy1 feature exists.

'

' Postconditions: Body is moved and copied as per transform
settings.

'

'-----------------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
part As SldWorks.PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
component As SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
moveCopyFeat As SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
moveCopy_featData As SldWorks.MoveCopyBodyFeatureData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
moveCopyFeat = part.FeatureByName("Body-Move/Copy1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
moveCopy_featData = moveCopyFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= moveCopy_featData.AccessSelections(part,
component)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}moveCopy_featData.TransformType= swTransformType_Translation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}moveCopy_featData.TransformX= 0.02

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}moveCopy_featData.TransformY= 0.03

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}moveCopy_featData.TransformZ= 0.04

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= moveCopyFeat.ModifyDefinition(moveCopy_featData,
part, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}moveCopy_featData.ReleaseSelectionAccess

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

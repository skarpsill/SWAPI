---
title: "Skip Items in Array Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Skip_Items_in_Array_Example_VB.htm"
---

# Skip Items in Array Example (VBA)

This example shows how to skip items in an array.

'------------------------------------------------------------

Private Sub CommandButton1_Click()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pSwApp = GetObject("", "SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pPart = pSwApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart.SelectByID"LPattern1", "BODYFEATURE",
0, 0, 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pSelMan = pPart.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pFeature = pSelMan.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pFeatureData = pFeature.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
skip As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
skip2(0 To 3) As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip
= pFeatureData.SkippedItemArray

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip2(0)
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip2(1)
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip2(2)
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip2(3)
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skip
= skip2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeatureData.SkippedItemArray= (skip)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeature.ModifyDefinitionpFeatureData, pPart,
Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeatureData.ReleaseSelectionAccess

End Sub

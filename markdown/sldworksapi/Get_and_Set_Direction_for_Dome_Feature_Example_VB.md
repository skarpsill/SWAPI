---
title: "Get and Set Direction for Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Direction_for_Dome_Feature_Example_VB.htm"
---

# Get and Set Direction for Dome Feature Example (VBA)

This example shows how to get and set the direction of a dome feature.
You must have a partkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}containing
a dome feature created with an edge indicating the direction of the feature
and preselect that edge.

'---------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim part As SldWorks.PartDoc

Dim component As SldWorks.Component2

Dim newEdge As SldWorks.Edge

Dim dome As SldWorks.feature

Dim dome_featData As SldWorks.DomeFeatureData2

Dim domeDirection As SldWorks.Edge

Dim boolstatus As Variant

Sub main()

'{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
newEdge = part.SelectionManager.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dome = part.FeatureByName("Dome1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dome_featData = dome.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= dome_featData.AccessSelections(part,
component)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
domeDirection = dome_featData.Direction

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not domeDirection Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dome_featData.Direction= newEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= dome.ModifyDefinition(dome_featData,
part, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dome_featData.ReleaseSelectionAccess

'}

End Sub

---
title: "Get and Set Constraint for Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm"
---

# Get and Set Constraint for Dome Feature Example (VBA)

This example shows how to get and set a constraining point for a dome
feature. A part containing a dome feature constrained by a sketch point
on the origin is open.

'---------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.PartDoc

Dim component As SldWorks.Component2

Dim newPointFeat As SldWorks.SketchPoint

Dim dome As SldWorks.feature

Dim domeConstraintPoint As SldWorks.SketchPoint

Dim dome_featData As SldWorks.DomeFeatureData2

Dim boolstatus As Variant

Sub main()

'{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID2("Point1@Sketch1",
"EXTSKETCHPOINT", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
newPointFeat = Part.SelectionManager.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dome = Part.FeatureByName("Dome1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dome_featData = dome.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= dome_featData.AccessSelections(Part,
component)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
domeConstraintPoint = dome_featData.ConstraintPointOrSketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not domeConstraintPoint Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dome_featData.ConstraintPointOrSketch= newPointFeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= dome.ModifyDefinition(dome_featData,
Part, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

dome_featData.ReleaseSelectionAccess

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

'}

End Sub

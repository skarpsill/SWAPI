---
title: "Add or Remove Curvature Combs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_or_Remove_Curvature_Combs_Example_VB.htm"
---

# Add or Remove Curvature Combs Example (VBA)

This example shows how to add or remove curvature combs to a curved
sketch segment.

'----------------------------------------------------

' Preconditions: Curved sketch segment is selected.

'

' Postconditions: Curvature combs are added or removed.

'----------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nResponsekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nResponse
= MsgBox("Add curvature combs?", vbYesNo)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nResponse = vbYes Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.InspectCurvature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.RemoveInspectCurvature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

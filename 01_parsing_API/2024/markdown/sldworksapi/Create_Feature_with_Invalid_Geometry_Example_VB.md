---
title: "Create Feature with Invalid Geometry Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Feature_with_Invalid_Geometry_Example_VB.htm"
---

# Create Feature with Invalid Geometry Example (VBA)

This example shows how to prompt the user whether to create a feature
that has invalid geometry.

'-------------------------------------

'

' Preconditions: None

'

' Postconditions: If user clicks Yes, then create a feature
that has invalid

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}geometry;
if No, then do not create a feature that has invalid

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}geometry.

'

'-------------------------------------

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nResponsekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nStatuskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nResponse
= MsgBox("Create feature that has invalid geometry?", vbYesNo)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nResponse = vbYes Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swApp.AllowFailedFeatureCreation(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swApp.AllowFailedFeatureCreation(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

'-------------------------------------

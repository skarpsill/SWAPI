---
title: "Hide or Show All Types Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_All_Types_Example_VB.htm"
---

# Hide or Show All Types Example (VBA)

This example shows how to hide or show these types in a the current
document:

(Table)=========================================================

| planes curves axes sketches temporary axes all annotations (including model dimensions and
feature dimensions) | origins points coordinate systems routing points |
| --- | --- |

'-------------------------------------------

Option Explicit

Public Enum swUserPreferenceToggle_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swViewDisplayHideAllTypes
= 198

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.modelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bShowkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nResponsekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nResponse
= MsgBox("Hide all types?", vbYesNo)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nResponse = vbYes Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bShow
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bShow
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swModel.SetUserPreferenceToggle(swViewDisplayHideAllTypes,
bShow): Debug.Assert bRet

End Sub

'-------------------------------------------

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

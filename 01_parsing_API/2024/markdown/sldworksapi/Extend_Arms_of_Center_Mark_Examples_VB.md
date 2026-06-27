---
title: "Extend Arms of Center Mark Examples (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extend_Arms_of_Center_Mark_Examples_VB.htm"
---

# Extend Arms of Center Mark Examples (VBA)

This example shows how to extend the arms (handles) of a center mark.

'------------------------------------------

'

' Preconditions: Drawing document is open and

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}has
a Drawing View1 with a center mark.

'

' Postconditions: The bottom and right-side arms are extended.

'

'------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDraw As SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocExt As SldWorks.ModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCenterMark As SldWorks.CenterMark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dExt2 As Double, dExt3 As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Active the drawing view and select the center mark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swDraw.ActivateView("Drawing
View1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("DetailItem353@Drawing
View1", "CENTERMARKSYM", 0.09197936270506, 0.1129166587377,
0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCenterMark = swSelMgr.GetSelectedObject6(1,
-1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the lengths of the bottom and right-side arms of the center mark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dExt2
= swCenterMark.GetExtendedLength(0,
swCenterMarkHandle_Down)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dExt3
= swCenterMark.GetExtendedLength(0,
swCenterMarkHandle_Right)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Length of arms before extension: " & dExt2 & ";
" & dExt3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Extend the bottom and right-side arms of the center mark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swCenterMark.SetExtendedLength(0,
swCenterMarkHandle_Down, 0.03)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swCenterMark.SetExtendedLength(0,
swCenterMarkHandle_Right, 0.02)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the revised lengths of the bottom and right-side arms of the center
mark

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dExt2
= swCenterMark.GetExtendedLength(0,
swCenterMarkHandle_Down)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dExt3
= swCenterMark.GetExtendedLength(0,
swCenterMarkHandle_Right)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Length of arms after extension: " & dExt2 & ";
" & dExt3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

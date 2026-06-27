---
title: "Insert Alternate Position View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Alternate_Position_View_Example_VB.htm"
---

# Insert Alternate Position View Example (VBA)

This example shows how to insert anAlternate Position View.

'--------------------------------------------------

'

' Preconditions: Drawing sheet is open with a

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}drawing
view selected.

'

' Postconditions: An alternate position view is created.

'

'--------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swView As SldWorks.View

Dim swSelMgr As SldWorks.SelectionMgr

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the drawing on which to superimpose

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
an Alternate Position View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert the Alternate Position View and

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
create the configuration called Configxxx

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.InsertAlternateView("Configxxx")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Print the type of view; should be 10, which

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
is an Alternate Position View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swView Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Type of view: " & swView.Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

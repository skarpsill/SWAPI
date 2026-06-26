---
title: "Get Base Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Base_Views_Example_VB.htm"
---

# Get Base Views Example (VBA)

This example shows how to get the names of the base views for all of
the views in a drawing.

'-------------------------------------

'

' Preconditions: Drawing document is open.

'

' Postconditions: None

'

'--------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBaseViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swDraw.GetFirstView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swView Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Returns NULL if no parent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBaseView = swView.GetBaseView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swView.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swBaseView Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-->
" & swBaseView.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

End Sub

'-------------------------------------

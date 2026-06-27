---
title: "Change to Isometric and Zoom to Fit View Mode Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_to_Isometric_and_Zoom_to_Fit_View_Mode_Example_VB.htm"
---

# Change to Isometric and Zoom to Fit View Mode Example (VBA)

This example shows how to change the current view mode to isometric
and Zoom to Fit.

'-----------------------------------------------

'

' Preconditions: Model document is open.

'

' Postconditions: Current view mode is changed to isometric
and Zoom to Fit.

'

'-----------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Not quite the same as when done through the user interface;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
model is zoomed out a bit further

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ShowNamedView2"*Isometric",
-1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Now view the same as done through the user interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ViewZoomtofit2

End Sub

'-----------------------------------------------

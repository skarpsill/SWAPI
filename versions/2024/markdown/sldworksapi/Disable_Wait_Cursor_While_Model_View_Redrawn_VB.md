---
title: "Disable Wait Cursor While Model View Redrawn (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/Disable_Wait_Cursor_While_Model_View_Redrawn_VB.htm"
---

# Disable Wait Cursor While Model View Redrawn (VBA)

## Disable Wait Cursor When Model View Redrawn (VBA)

This example shows how to suppress the wait cursor (also called the
hourglass) when a model view is redrawn.

'---------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Part As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
modelView As SldWorks.modelView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
modelView = Part.ActiveView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modelView.SuppressWaitCursorDuringRedraw= False

End Sub

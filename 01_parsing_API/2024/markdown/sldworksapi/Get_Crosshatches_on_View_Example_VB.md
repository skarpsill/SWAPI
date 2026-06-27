---
title: "Get Crosshatches on View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Crosshatches_on_View_Example_VB.htm"
---

# Get Crosshatches on View Example (VBA)

## Get Crosshatches on the View Example (VBA)

This example shows how to iterate the drawing views and get the crosshatches
in the current drawing view.

'----------------------------------------------

'

' Preconditions: Drawing document is open and contains
at least one drawing view.

'

' Postconditions: None

'

'----------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swDrawing As SldWorks.DrawingDoc

Dim currentView As SldWorks.View

Sub main()

Set swApp = Application.SldWorks

Set swDrawing = swApp.ActiveDoc

' Iterate the drawing views

Set currentView = swDrawing.GetFirstView

While Not currentView Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the crosshatch count on the view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
currentView.GetFaceHatchCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
currentView.GetFaceHatchCount = 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
currentView = currentView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the crosshatches on the view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
hatcharray As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hatcharray
= currentView.GetFaceHatches

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Following FaceHatch properties are accessible to you

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).Pattern

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).angle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).Color

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).Layer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).Scale2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
hatcharray(1).SolidFill

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
currentView = currentView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

Wend

End Sub

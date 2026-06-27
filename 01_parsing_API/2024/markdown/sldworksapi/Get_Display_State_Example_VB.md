---
title: "Get Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Example_VB.htm"
---

# Get Display State Example (VBA)

This example shows how to get the display state of the model.

'-------------------------------------------

'

' Preconditions: Model document is open.

'

' Postconditions: None

'

'-------------------------------------------

Option Explicit

Public Enum swViewDisplayType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewSectioned
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewPerspective
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewShaded
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewWireFrame
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewHiddenLinesRemoved
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewHiddenInGrey
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swIsViewCurvature
= 6

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModView = swModel.ActiveView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sectionedkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewSectioned)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Perspectivekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewPerspective)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Shadedkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewShaded)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}WireFramekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewWireFrame)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HiddenLinesRemovedkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewHiddenLinesRemoved)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HiddenInGreykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewHiddenInGrey)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Curvaturekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModView.GetDisplayState(swIsViewCurvature)

End Sub

'-------------------------------------------

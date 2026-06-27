---
title: "Get Blocking State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocking_State_Example_VB.htm"
---

# Get Blocking State Example (VBA)

This example shows how to get the blocking state for a model document.

'----------------------------------------------------

'

' Preconditions: Model document is open.

'

' Postconditions: None

'

'----------------------------------------------------

Option Explicit

Public Enum swBlockingStates_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swNoBlock
= &H0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFullBlock
= &H1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModifyBlock
= &H2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swPartialModifyBlock
= &H3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEditorBlock
= &H4

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"BlockingState = " & swModel.GetBlockingState

End Sub

'----------------------------------------------------

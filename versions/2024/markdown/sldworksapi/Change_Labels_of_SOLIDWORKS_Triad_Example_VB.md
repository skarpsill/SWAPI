---
title: "Change Labels of SOLIDWORKS Triad Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Labels_of_SOLIDWORKS_Triad_Example_VB.htm"
---

# Change Labels of SOLIDWORKS Triad Example (VBA)

This example shows how to change the labels of the SOLIDWORKS triad.

'---------------------------------------

'

' Preconditions: SOLIDWORKS model document is open.

'

' Postconditions: The labels of the triad are

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}changed
and then changed back to

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}their
original values.

'

'---------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim rVal As String

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rVal
= swApp.SetUserPreferenceStringValue(swReferenceTriadXLabel,
"AltX")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rVal = False Then swApp.SendMsgToUser("ERROR: Unable to change triad label.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rVal
= swApp.SetUserPreferenceStringValue(swReferenceTriadYLabel,
"AltY")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rVal = False Then swApp.SendMsgToUser("ERROR: Unable to change triad label.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rVal
= swApp.SetUserPreferenceStringValue(swReferenceTriadZLabel,
"AltZ")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rVal = False Then swApp.SendMsgToUser("ERROR: Unable to change triad label.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggleswReferenceTriadUseAlternateLabels,
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Stop
'Labels are changed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggleswReferenceTriadUseAlternateLabels,
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Stop
'Labels are changed back to original

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

---
title: "Open Advanced Dialog on Document Open Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_VB.htm"
---

# Open Advanced Dialog on Document Open Example (VBA)

This example shows how to open an advanced dialog box before opening a
document.

'----------------------------------------------------------------------
' Preconditions: Verify that the specified model document to open exists.
'
' Postconditions:
'kadov_tag{{<spaces>}}1.
Displays the Configure Document dialog box before the model
' document opens.
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2.
Click**OK**to close the dialog box.
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Close
the document without saving.
'---------------------------------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
myDoc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
openDocParams As SldWorks.DocumentSpecification

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
openDocParams = swApp.**GetOpenDocSpec**("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.DocumentType
= SwConst.swDocASSEMBLY

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.InteractiveAdvancedOpen= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
myDoc = swApp.**OpenDoc7**(openDocParams)

End Sub

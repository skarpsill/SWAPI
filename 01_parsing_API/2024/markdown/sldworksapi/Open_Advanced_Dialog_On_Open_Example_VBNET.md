---
title: "Open Advanced Dialog on Document Open Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_VBNET.htm"
---

# Open Advanced Dialog on Document Open Example (VB.NET)

This example shows how to open an advanced dialog box before opening a
document.

'---------------------------------------------------------------------- ' Preconditions: Verify that the specified model document to open exists. ' ' Postconditions: ' 1.
Displays the Configure Document dialog box before the model ' document opens. ' 2.
Click OK to close the dialog box. ' 3. Close
the document without saving. '---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
myDoc As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
openDocParams As DocumentSpecification

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams
= swApp.**GetOpenDocSpec**("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.DocumentType
= swDocumentTypes_e.swDocASSEMBLY

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocParams.InteractiveAdvancedOpen= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}myDoc
= swApp.**OpenDoc7**(openDocParams)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class

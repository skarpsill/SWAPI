---
title: "Get Locations and Names of Document Templates Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Locations_and_Names_of_Document_Templates_Example_VB.htm"
---

# Get Locations and Names of Document Templates Example (VBA)

This example shows how to get the locations and names of SOLIDWORKS
document templates for the SOLIDWORKS session.

'------------------------------------------------
' Preconditions: Open the Immediate window.
' Postconditions: Examine the Immediate window.
'------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"FileLocationsDocumentTemplates = " & swApp.GetUserPreferenceStringValue(swFileLocationsDocumentTemplates)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"FileLocationsSheetFormatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetUserPreferenceStringValue(swFileLocationsSheetFormat)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"DefaultTemplatePartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"DefaultTemplateAssemblykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetUserPreferenceStringValue(swDefaultTemplateAssembly)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"DefaultTemplateDrawingkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetUserPreferenceStringValue(swDefaultTemplateDrawing)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Draw template = " & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperAsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Part template = " & swApp.GetDocumentTemplate(swDocPART,
"", 0, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Assy template = " & swApp.GetDocumentTemplate(swDocASSEMBLY,
"", 0, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Draw templates:"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Akadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperAsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A
vertkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperAsizeVertical, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Bkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperBsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ckadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperCsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperDsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperEsize, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A4kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA4size, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A4
vertkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA4sizeVertical, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA3size, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA2size, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA1size, 0#, 0#)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A0kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApp.GetDocumentTemplate(swDocDRAWING,
"", swDwgPaperA0size, 0#, 0#)

End Sub

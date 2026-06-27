---
title: "Save Design Table as Microsoft Excel File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm"
---

# Save Design Table as Microsoft Excel File Example (VBA)

This example shows how to save a design table to a Microsoft Excel file.

'-----------------------------------

'

' Preconditions: Document that has a design table is open

'

' Postcoditions: Design table is saved as a Microsoft

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Excel
file named DesignTable.xls

'

'------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDesignTablekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DesignTable

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strFileNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDesignTable = swModel.GetDesignTable

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDesignTable.Attach

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swDesignTable.SaveAsExcelFile(swApp.GetCurrentMacroPathFolder
& "\DesignTable.xls")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Do not detach if table is not active

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(Not (swDesignTable.IsActive=
False)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDesignTable.Detach

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

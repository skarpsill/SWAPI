---
title: "Extract Embedded eDrawings Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Extract_Embedded_eDrawings_Data_Example_VB.htm"
---

# Extract Embedded eDrawings Data Example (VBA)

This example shows how to search drawings in the SOLIDWORKS Workgroup PDM
vault, check to see if the drawings of a certain lifecycle status (APPROVED),
and if both criteria are met, extract the embedded eDrawings data from
the drawings and save it to a local disk.

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}On
Error GoTo errorHandler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
connection As PDMWConnection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
connection = CreateObject("PDMWorks.PDMWConnection")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Login"pdmwadmin", "pdmwadmin",
"localhost"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
savePath As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}savePath
= "C:\edrawings\"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''Must
be a valid path

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
alldocs As PDMWDocuments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
alldocs = connection.Documents

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
adoc As PDMWDocument

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each adoc In alldocs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
LCase(Right(adoc.Name, 6)) = "slddrw"
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
adoc.GetStatus= "APPROVED"
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}adoc.SaveEmbeddedEDWsavePath

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Logout

Exit Sub

errorHandler:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Error: " & adoc.Name& " : " & Err.Description

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Resume
Next

End Sub

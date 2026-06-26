---
title: "List Assemblies Where Part Used Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/List_Assemblies_Where_Part_Used_Example_VB.htm"
---

# List Assemblies Where Part Used Example (VBA)

This example shows how to look at each part in the SOLIDWORKS Workgroup PDM
vault and list the assemblies in which the part is used.

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
connection As PDMWConnection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
connection = CreateObject("PDMWorks.PDMWConnection")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Login"pdmwadmin", "pdmwadmin",
"localhost"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
alldocs As PDMWDocuments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
alldocs = connection.Documents

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
adoc As PDMWDocument

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
msgBoxStr As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each adoc In alldocs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
LCase(Right(adoc.Name, 6)) = "sldprt"
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgBoxStr
= msgBoxStr & "Part: " & adoc.Name& vbNewLine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgBoxStr
= msgBoxStr & "Assemblies where it is used:" & vbNewLine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
whereUsedList As PDMWLinks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
whereUsedList = adoc.WhereUsed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
l As PDMWLink

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each l In whereUsedList

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
LCase(Right(l.Document.Name, 6))
= "sldasm" Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgBoxStr
= msgBoxStr & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& l.Document.Name& vbNewLine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgBoxStr
= msgBoxStr & "----" & vbNewLine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Output.Data
= msgBoxStr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Output.Show

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Logout

End Sub

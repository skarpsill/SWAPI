---
title: "Get Specific Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Get_Specific_Document_Example_VB.htm"
---

# Get Specific Document Example (VBA)

This example shows how to log into a SOLIDWORKS Workgroup PDM vault, get a
collection of documents, and get a specific document.

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
connection As PDMWConnection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
connection = CreateObject("PDMWorks.PDMWConnection")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Login"pdmwadmin", "pdmwadmin",
"localhost"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
alldocs As PDMWDocuments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
doc1 As PDMWDocument

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
doc2 As PDMWDocument

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
doc3 As PDMWDocument

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
alldocs = connection.Documents

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
doc1 = connection.Documents.Item(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
doc2 = connection.GetSpecificDocument("bracket.sldprt")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''Look
at alldocs, doc1, and doc2 in the debugger

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
doc3 = alldocs("bracket.sldprt")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}connection.Logout

End Sub

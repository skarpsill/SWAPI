---
title: "Get Paths of Open Documents(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_of_Open_Documents_Example_VBNET.htm"
---

# Get Paths of Open Documents(VB.NET)

## Get Paths of Open Documents (VB.NET)

This example shows how to get an array of the open documents, and their
paths and filenames, in the current SOLIDWORKS session.

```vb
'---------------------------------------------
' Preconditions: At least one document is
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}open in SOLIDWORKS.
'
' Postconditions: None.
----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim models As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim count As Integer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim index As Integer

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}count = swApp.GetDocumentCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Number of open documents in this SOLIDWORKS session: " & count)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}models = swApp.GetDocuments
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For index = LBound(models) To UBound(models)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = models(index)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Path and name of open document: " & swModel.GetPathName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next index

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```

---
title: "Get Paths of Open Documents (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_of_Open_Documents_Example_VB.htm"
---

# Get Paths of Open Documents (VBA)

This example shows how to get an array of the open documents, and their
paths and filenames, in the current SOLIDWORKS session.

```vb
'---------------------------------------------
' Preconditions: At least one document is
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}open in SOLIDWORKS.
'
' Postconditions: None.
----------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim vModels As Variant
Dim count As Long
Dim index As Long
Sub main()
Set swApp = Application.SldWorks
count = swApp.GetDocumentCount
Debug.Print "Number of open documents in this SolidWork session: " & count
vModels = swApp.GetDocuments
For index = LBound(vModels) To UBound(vModels)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = vModels(index)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Path and name of open document: " & swModel.GetPathName
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next index
End Sub
```

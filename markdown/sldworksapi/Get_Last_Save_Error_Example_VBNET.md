---
title: "Get Last Save Error Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Last_Save_Error_Example_VBNET.htm"
---

# Get Last Save Error Example (VB.NET)

```
This example shows how to get the last save error issued by Microsoft in the current SOLIDWORKS session.
'-------------------------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS session and cause Microsoft to issue a save error.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the last save error issued by Microsoft.
' 2. Examine the Immediate window.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
varPath As Object
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
varError As Object
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
varMessage As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}varMessage
= swApp.GetLastSaveError(varPath,
varError)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not varError = 0 Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Document generating the save error: " & varPath)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error code: " & varError)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error message: " & varMessage)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("This
SOLIDWORKS
session has not experienced a save error.")
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Subkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class

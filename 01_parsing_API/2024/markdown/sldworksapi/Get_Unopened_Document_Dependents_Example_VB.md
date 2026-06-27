---
title: "Get Unopened Document Dependents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Unopened_Document_Dependents_Example_VB.htm"
---

# Get Unopened Document Dependents Example (VBA)

This example shows how to return all of the dependent files for the
specified closed document. You can run this program on any type of SOLIDWORKS
document.

'-----------------------------------------------

Option Explicit

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
sDefaultNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String = "D:\docs\claw-mechanism.sldasm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sDocNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDependkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swModel Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDocName
= swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDocName
= sDefaultName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vDepend
= swApp.GetDocumentDependencies2(sDocName,
True, True, False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
sDocName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vDepend) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}No
dependencies"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To (UBound(vDepend) - 1) / 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ vDepend(2 * i) + " --> " + vDepend(2 * i + 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

'-----------------------------------------------

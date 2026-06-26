---
title: "Get View Mode Names for Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_View_Mode_Names_for_Model_Example_VB.htm"
---

# Get View Mode Names for Model Example (VBA)

This example shows how to get all of the view mode names for the current
part or assembly.

'-----------------------------------

'

' Preconditions: Part or assembly document is open.

'

' Postconditions: None

'

'-----------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vModelViewNameskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vModelViewNames
= swModel.GetModelViewNames

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"FileName = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelViewCount
= " & swModel.GetModelViewCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vModelViewNames)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ vModelViewNames(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

'------------------------------------------

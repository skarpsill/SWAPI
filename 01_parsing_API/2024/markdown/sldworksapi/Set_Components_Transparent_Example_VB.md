---
title: "Set Components Transparent Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Components_Transparent_Example_VB.htm"
---

# Set Components Transparent Example (VBA)

This example shows how to make one or more selected components transparent

'-------------------------------------------

'

' Preconditions: Assembly document is open and one

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}or
more components are selected.

'

' Postconditions: Selected components are transparent.

'

'-------------------------------------------

Option Explicit

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDoc As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssembly As SldWorks.AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDoc = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAssembly = swModelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set the selected component to transparent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swAssembly.SetComponentTransparent(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Set
the selected component to not transparent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'boolstatus
= swAssembly.SetComponentTransparent(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

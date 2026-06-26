---
title: "Insert New Virtual Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_VB.htm"
---

# Insert New Virtual Assembly Example (VBA)

This example shows how to insert an assembly as a virtual component into the
main assembly or selected sub-assembly.

'-------------------------------------------------------------------------

' Preconditions: Open
an assembly document.

'

' Postconditions: A
new virtual component displays in the

' FeatureManager design tree.

'---------------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks

Dim swDoc As SldWorks.ModelDoc2

Dim swADoc As SldWorks.AssemblyDoc

Dim swComp As SldWorks.Component2

Dim status As Long

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDoc = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swADoc = swDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swComp = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}status
= swADoc.InsertNewVirtualAssembly(swComp)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swComp Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
("Virtual component did not get created.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
("New virtual component:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swComp.Name2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
("Is virtual: " & swComp.IsVirtual)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

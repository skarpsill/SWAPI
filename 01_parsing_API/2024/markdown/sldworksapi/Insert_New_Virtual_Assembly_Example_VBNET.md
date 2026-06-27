---
title: "Insert New Virtual Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Virtual_Assembly_Example_VBNET.htm"
---

# Insert New Virtual Assembly Example (VB.NET)

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

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDoc As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swADoc As AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swComp As Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
status As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDoc
= swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swADoc
= swDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swComp
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}status
= swADoc.InsertNewVirtualAssembly(swComp)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swComp Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox("Virtual
component did not get created.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("New
virtual component:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swComp.Name2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Is
virtual: " & swComp.IsVirtual)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class

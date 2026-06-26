---
title: "Create and Arrange Windows Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Arrange_Windows_Example_VB.htm"
---

# Create and Arrange Windows Example (VBA)

This example shows how to create a new window containing the active
document object and how to arrange all open windows.

'-------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.CreateNewWindow

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Arrange:
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0
= Cascade

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1
= Tile horizontally

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2
= Tile vertically

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.ArrangeWindows1

End Sub

'-------------------------------------

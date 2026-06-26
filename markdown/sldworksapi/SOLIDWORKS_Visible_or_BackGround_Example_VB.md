---
title: "SOLIDWORKS Visible or BackGround Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/SOLIDWORKS_Visible_or_BackGround_Example_VB.htm"
---

# SOLIDWORKS Visible or BackGround Example (VBA)

## SOLIDWORKS Visible or Background Example (VBA)

These examples shows several situations for
running or attaching to SOLIDWORKS session through the API.

### SOLIDWORKS not running: Launch invisibly and end SOLIDWORKS session

Sub Macro1()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

' Close
the SOLIDWORKS application. If you do not perform this step, SOLIDWORKS ' continues to run. If SOLIDWORKS is running in the background, the user
is ' unaware that SOLIDWORKS is running and consuming their system resources.

swApp.ExitAppkadov_tag{{<spaces>}}

kadov_tag{{</spaces>}}Set
swApp = Nothing

End Sub

### SOLIDWORKS running: Attach to existing SOLIDWORKS session and end SOLIDWORKS
session

Sub Macro2()

kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{</spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

swApp.ExitApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Nothing

End Sub

### SOLIDWORKS not running: Launch invisibly, become visible, and end SOLIDWORKS
session

Sub Macro3()

kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{</spaces>}}Dim
Part As Object

kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.Visible= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.ExitApp

Set
swApp = Nothing

End Sub

### SOLIDWORKS not running: Launch invisibly, become visible, and leave
SOLIDWORKS running

Sub Macro4()

kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{</spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.Visible= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.UserControl= True

kadov_tag{{</spaces>}}'
Give control to the user, which leaves SOLIDWORKS running

End Sub

### SOLIDWORKS not running: Launch invisibly, create part invisibly, close
part, and end SOLIDWORKS session

Sub Macro5()

kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{</spaces>}}Dim
Part As Object

kadov_tag{{</spaces>}}'
This must be explicitly defined for ISldWorks::ActivateDoc2

kadov_tag{{</spaces>}}Dim
errors As Long

kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.NewPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActivateDoc2("Part1",True,errors)

kadov_tag{{</spaces>}}Set
Part = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.CloseDoc"Part1"

swApp.ExitApp

kadov_tag{{</spaces>}}Set
swApp = Nothing

End Sub

### SOLIDWORKS not running: Launch invisibly, create part invisibly, make
the part and SOLIDWORKS visible, and leave SOLIDWORKS running

Sub Macro6()

kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{</spaces>}}Dim
Part As Object

kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.NewPart

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActivateDoc("Part1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part.Visible= True

kadov_tag{{</spaces>}}'
Make the part and SOLIDWORKS visible

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.UserControl= True

kadov_tag{{</spaces>}}'
Give control to the user, which leaves SOLIDWORKS running

kadov_tag{{</spaces>}}Set
Part = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.CloseDoc"Part1"

End Sub

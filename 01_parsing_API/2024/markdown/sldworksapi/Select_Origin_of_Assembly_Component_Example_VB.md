---
title: "Select Origin of Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Origin_of_Assembly_Component_Example_VB.htm"
---

# Select Origin of Assembly Component Example (VBA)

This example shows how to get the origin of an assembly component.

```
'-------------------------------------------------
' Preconditions:
' 1. Open an assembly that is fully resolved.
' 2. Select a component.
'
' Postconditions:
' 1. Selects the origin of the selected component.
' 2. Examine the graphics area.
'--------------------------------------------------
Option Explicit
```

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCompModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelComp = swSelMgr.GetSelectedObjectsComponent(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCompModel = swSelComp.GetModelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelComp.FirstFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swFeat Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
"OriginProfileFeature" = swFeat.GetTypeNameThen

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swFeat.Select2(False, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Do

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swFeat.GetNextFeature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

End Sub

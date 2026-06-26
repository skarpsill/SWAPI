---
title: "Get Edge Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Points_Example_VB.htm"
---

# Get Edge Points Example (VBA)

This example shows how to get edge points.

NOTE:An edge point is a midpoint
on an edge or an endpoint or midpoint on a reference curve.

'---------------------------------------------

'

' Preconditions: Part document is open and

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}at
least one edge point is selected.

'

' Postconditions: None

'

'---------------------------------------------

Dim swApp As Object

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
edgep As SldWorks.EdgePoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelObj As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelType As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelCount As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = GetObject(, "SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelCount
= swSelMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 1 To SelCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType
= swSelMgr.GetSelectedObjectType(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
SelType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
SwConst.swSelectType_e.swSelPOINTREFS = SelType Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelObj = swSelMgr.GetSelectedObject5(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
edgep = swSelObj

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

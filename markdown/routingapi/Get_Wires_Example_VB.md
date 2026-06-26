---
title: "Get Wires Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Wires_Example_VB.htm"
---

# Get Wires Example (VBA)

This example shows how to get the wires in a route.

...

Set rtElectricalRoute = rtRouteManager.GetElectricalRoute

...

lNumWiresAccumulated = 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vWires
= rtElectricalRoute.GetWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vWires) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lNumWires
= rtElectricalRoute.GetWiresCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
aWires(lNumWires - 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lStartIdx
= lNumWiresAccumulated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lEndIdx
= lNumWiresAccumulated + lNumWires - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
lIdx = lStartIdx To lEndIdx

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
aWires(lIdx) = vWires(lIdx)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lNumWiresAccumulated
= lNumWiresAccumulated + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
lIdx

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

...

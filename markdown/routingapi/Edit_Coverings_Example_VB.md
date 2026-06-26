---
title: "Edit Coverings Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Edit_Coverings_Example_VB.htm"
---

# Edit Coverings Example (VBA)

This example shows how to edit coverings.

'----------------------------------------------

' Required reference: Microsoft Scripting Runtime

'----------------------------------------------

Sub EditCovering(ByRef rtRouteManager As SWRoutingLib.RouteManager)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vWireskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vWirekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtWirekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.Wire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vRouteSegmentIDskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lNumRouteSegmentIDkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lIdxkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtElectricalRoutekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.ElectricalRoute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtRoutePropertykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.RouteProperty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtElectricalRoutePropertykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.ElectricalRouteProperty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetValkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dictSegmentsProcessedkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Scripting.Dictionary

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtCoveringkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.Covering

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the electrical route

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtElectricalRoute = rtRouteManager.GetElectricalRoute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtElectricalRoute Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No electrical route found."kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Subkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Loop over all wires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vWires
= rtElectricalRoute.GetWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vWires) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dictSegmentsProcessed = New Scripting.Dictionary

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vWire In vWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtWire = vWire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vRouteSegmentIDs
= rtWire.GetRouteSegmentIDs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vRouteSegmentIDs) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
lIdx = LBound(vRouteSegmentIDs) To UBound(vRouteSegmentIDs)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get segment ID

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lNumRouteSegmentID
= vRouteSegmentIDs(lIdx)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Check to see if ID already processed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not dictSegmentsProcessed.Exists(lNumRouteSegmentID) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"segment id = " & lNumRouteSegmentID

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtRouteProperty = rtElectricalRoute.GetRouteProperty(lNumRouteSegmentID)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Register this property so that you know that you have already dealt with
it

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dictSegmentsProcessed.Add
lNumRouteSegmentID, rtRouteProperty

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
If a covering is present, edit it

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtRouteProperty.HasCoveringThen

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtCovering = rtRouteProperty.GetCovering

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtCovering.Name= rtCovering.Name& "-z"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtCovering.Color= RGB(255, 0, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtCovering.OuterDiameter= 1.1 * rtCovering.OuterDiameter

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtCovering.PartNumber= "0123456789ABCDEF"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
No need to call RouteManager.EditWires to commit the changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
lIdx

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
vWire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Release

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
dictSegmentsProcessed = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

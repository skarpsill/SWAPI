---
title: "Get Wires, Sketch Segments, and Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Wires_Sketch_Segments_and_Sketches_Example_VB.htm"
---

# Get Wires, Sketch Segments, and Sketches Example (VBA)

This example shows how to get the wires, route sketch segment IDs, sketch
segments, and sketches.

...

vWires = rtElectricalRoute.GetWires

...

Set rtWire = vWire

...

For Each vWire In vWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtWire = vWire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vRouteSegmentIDs
= rtWire.GetRouteSegmentIDs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vRouteSegmentIDs) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
lIdx = LBound(vRouteSegmentIDs) To UBound(vRouteSegmentIDs)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lSegmentId
= vRouteSegmentIDs(lIdx)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Segment ID = " & lSegmentId

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSketchSegments
= rtElectricalRoute.GetSketchSegments(lSegmentId)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vSketchSegments) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vSketchSegment In vSketchSegments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketchSegment = vSketchSegment

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
(Not swSketchSegment Is Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRetVal
= swSketchSegment.Select4(True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
(bRetVal)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketch = swSketchSegment.GetSketch

...

---
title: "Display Vertices Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Vertices_Example_VB.htm"
---

# Display Vertices Example (VBA)

This example shows how to display vertices.

'----------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part document is open and has one or more solid bodies.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Each solid body does not contain any circular edges.

'

' Postconditions: All vertices are highlighted.

'

'----------------------------------------

Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.PartDoc

Dim Body As SldWorks.Body2

Dim Edge As SldWorks.Edge

Dim Vertex As SldWorks.Vertex

Dim Bodyarr As Variant

Dim vbody As Variant

Dim Edgearr As Variant

Dim idx As Long

Dim vobj As Variant

Dim crgb As Long

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc

Bodyarr = Part.GetBodies2(swSolidBody,
True)

For Each vbody In Bodyarr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Body = vbody

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Edgearr
= Body.GetEdges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}idx
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vobj In Edgearr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Edge = vobj

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Vertex = Edge.GetStartVertex

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Select
Case CInt(idx Mod 8)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(0, 0, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(0, 0, 255)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(0, 255, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(0, 255, 255)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(255, 0, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(255, 0, 255)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(255, 255, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}crgb
= RGB(255, 255, 255)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}idx
= idx + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Vertex.DisplayPart, crgb, 1, True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Nextkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Next

End Sub

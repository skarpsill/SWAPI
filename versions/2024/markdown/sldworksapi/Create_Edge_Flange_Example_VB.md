---
title: "Create Edge Flange Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Edge_Flange_Example_VB.htm"
---

# Create Edge Flange Example (VBA)

This example shows how to create an edge flange.

'-----------------------------------------------

'

' Precconditions: Sheet metal part is open and

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}contains
an edge flange. Flat pattern is suppressed.

'

' Postcontitions: Another edge flange is created.

'

'-----------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swEntity As SldWorks.Entity

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swFeat As SldWorks.Feature

Dim swEdgeFlange As SldWorks.EdgeFlangeFeatureData

Dim pNewEdge(0) As Object

Dim boolstatus As Boolean

Dim bRet As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

'
Select the edge for the new flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("",
"EDGE", 0.06071758265887, -0.03627116313436, 0.05999086611155,
False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pNewEdge(0) = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the sketch for the new flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("Sketch8",
"SKETCH", 0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEntity = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the existing edge flange to get the edge flange feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("Edge-Flange1",
"BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject6(1,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEdgeFlange = swFeat.GetDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll back the model to modify it

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEdgeFlange.AccessSelectionsswModel, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEntity.Select4True, Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vEdges As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdges
= pNewEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create the new flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEdgeFlange.Edges= vEdges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Roll forward the model with the new flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeat.ModifyDefinitionswEdgeFlange, swModel,
Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

---
title: "Create Ruled Surface Body From Edge (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ruled_Surface_From_Edge_Example_VB.htm"
---

# Create Ruled Surface Body From Edge (VBA)

This example shows how to create a ruled surface body from an edge.

```vb
'--------------------------------------------------------
' Preconditions: Model document is open and an edge is
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}is selected on the model.
'
' Postconditions: Ruled surface body is created from the
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}selected edge.
'--------------------------------------------------------
Option Explicit

Public Enum swBodyType_e
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swAllBodies = 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSolidBody = 1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSheetBody = 2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swWireBody = 3
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swMinimumBody = 4
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swGeneralBody = 5
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swEmptyBody = 6
End Enum

Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim swModel As SldWorks.Modeler
Dim swSelMgr As SldWorks.SelectionMgr
Dim swEdge(0) As SldWorks.Edge
Dim swEdgeList As Variant
Dim swRuledBody As SldWorks.Body2

Sub main()

Set swApp = Application.SldWorks
Set swDoc = swApp.ActiveDoc
Set swModel = swApp.GetModeler
Set swSelMgr = swDoc.SelectionManager
Set swEdge(0) = swSelMgr.GetSelectedObject6(1, -1)
swEdgeList = swEdge
Dim error As Long
error = swModel.CreateRuledSurfaceFromEdge(swDoc, swEdgeList, 1, 0.02, True, False, True, 0#, False, 1#, 0#, 0#, False, swRuledBody)
Dim typeBody As Long
typeBody = swRuledBody.GetType()
Select Case typeBody
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swAllBodies
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "All solid and sheet bodies"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swSolidBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Solid body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swSheetBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Sheet body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swWireBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Wire body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swMinimumBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Point body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swGeneralBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "General, nonmanifold body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Case swEmptyBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "NULL body"

End Select
End Sub
```

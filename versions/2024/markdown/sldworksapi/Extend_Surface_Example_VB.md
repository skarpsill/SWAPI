---
title: "Extend Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Extend_Surface_Example_VB.htm"
---

# Extend Surface Example (VBA)

This example shows how to extend edges of a the selected surface.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a surface body.
' 2. Select an edge that you want to extend
'    on the surface body.
'
' Postconditions:
' 1. Creates and displays a temporary body using
'    the selected edge.
' 2. Examine the graphics area.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swEdge As SldWorks.Edge
Dim swBody As SldWorks.Body2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swVertex As SldWorks.Vertex
Dim swFace As SldWorks.Face2
Dim edgeArr(0) As SldWorks.Edge
Dim edgeVar As Variant
Dim bExtLin As Boolean
Dim endCond As Long
Dim newBody1 As SldWorks.Body2
```

```
Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Select an edge on the surface that you want to extend
    Set swEdge = swSelMgr.GetSelectedObject5(1)
    Set swBody = swEdge.GetBody
    Set edgeArr(0) = swEdge
    edgeVar = edgeArr
    bExtLin = True
    endCond = 0
    Set swVertex = Nothing
    Set swFace = Nothing
    Set newBody1 = swBody.ExtendSurface((edgeVar), bExtLin, endCond, 0.01, swVertex, swFace)
    newBody1.Display2 swPart, RGB(255, 0, 0), 0
```

```
End Sub
```

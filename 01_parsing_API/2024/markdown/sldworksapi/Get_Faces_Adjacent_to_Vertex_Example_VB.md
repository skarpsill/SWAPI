---
title: "Get Faces Adjacent to Vertex Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Adjacent_to_Vertex_Example_VB.htm"
---

# Get Faces Adjacent to Vertex Example (VBA)

This example shows how to get the faces adjacent to the selected vertex.

```
'-----------------------------------------------------
' Preconditions: Open a part document and select a vertex.
'
' Postconditions:
' 1. Selects the faces adjacent to the selected vertex.
' 2. Examine the graphics area.
'-----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swVert As SldWorks.Vertex
    Dim vFaceArr As Variant
    Dim vFace As Variant
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swVert = swSelMgr.GetSelectedObject6(1, -1)

    swModel.ClearSelection2 True
```

```
    vFaceArr = swVert.GetAdjacentFaces
    For Each vFace In vFaceArr
        Set swFace = vFace
        Set swEnt = swFace
        bRet = swEnt.Select4(True, Nothing)
    Next vFace
```

```
End Sub
```

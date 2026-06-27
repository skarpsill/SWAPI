---
title: "Get Tangent Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tangent_Edges_Example_VB.htm"
---

# Get Tangent Faces Example (VBA)

This examples shows how to get faces tangent to the selected face.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select a face tangent to other faces.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets all tangent faces to the selected face.
' 2. Examine the Immediate window and graphics area.
'-----------------------------------------------
Option Explicit
```

```
Sub ProcessSelections(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2)
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim nSelCount As Long
    Dim i As Long
```

```
    Set swSelMgr = swModel.SelectionManager
    nSelCount = swSelMgr.GetSelectedObjectCount
    For i = 1 To nSelCount
        Debug.Print "  Selected type of tangent entity(" & i & ") (2 = face) = " & swSelMgr.GetSelectedObjectType2(i)
    Next i
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim bRe As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Debug.Print "Selected type of entity before calling IModelDoc2::SelectTangency (2 = face):"
    ProcessSelections swApp, swModel
    swModel.SelectTangency
    Debug.Print "Selected type of tangent entities after calling IModelDoc2::SelectTangency (2 = face):"
    ProcessSelections swApp, swModel
```

```
End Sub
```

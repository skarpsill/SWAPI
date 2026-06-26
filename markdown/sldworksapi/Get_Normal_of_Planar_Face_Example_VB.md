---
title: "Get Normal of Planar Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Normal_of_Planar_Face_Example_VB.htm"
---

# Get Normal of Planar Face Example (VBA)

This example shows how to get the normal parameters of a planar face.

```
'-------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select a planar face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the normal vector of the selected planar
'    face.
' 2. Examine the Immediate window.
'-------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim vNorm As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vNorm = swFace.Normal
    Debug.Print "Normal = (" & vNorm(0) & ", " & vNorm(1) & ", " & vNorm(2) & ")"
```

```
End Sub
```

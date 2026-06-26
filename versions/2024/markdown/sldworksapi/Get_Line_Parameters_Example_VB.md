---
title: "Get Line Parameters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Line_Parameters_Example_VB.htm"
---

# Get Line Parameters Example (VBA)

This example shows how to get a line's parameters.

```
'-----------------------------------------
' Preconditions:
' 1. Open a model document and select an edge.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the parameters of the curve, which
'    is a line.
' 2. Examine the Immediate window.
'------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim vLineParam As Variant
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
    Set swCurve = swEdge.GetCurve
    vLineParam = swCurve.LineParams
    Debug.Print "Root point = (" & vLineParam(0) * 1000# & ", " & vLineParam(1) * 1000# & ", " & vLineParam(2) * 1000# & ") mm"
    Debug.Print "Direction = (" & vLineParam(3) & ", " & vLineParam(4) & ", " & vLineParam(5) & ")"
```

```
End Sub
```

---
title: "Create Ruled Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ruled_Surface_Example_VB.htm"
---

# Create Ruled Surface Example (VBA)

This example shows how to create a ruled surface.

```
'-------------------------------------------
' Preconditions:
' 1. Open a part that has two edges created
'    using b-curves.
' 2. Select those two edges.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a ruled surface.
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
    Dim swModeler As SldWorks.Modeler
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge(1) As SldWorks.Edge
    Dim swCurve(1) As SldWorks.Curve
    Dim nApex(2) As Double
    Dim vApex As Variant
    Dim swSurf As SldWorks.Surface
```

```
    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEdge(0) = swSelMgr.GetSelectedObject5(1)
    Set swCurve(0) = swEdge(0).GetCurve
    Debug.Print "Is b-curve? " & swCurve(0).IsBcurve
    Set swEdge(1) = swSelMgr.GetSelectedObject5(2)
    Set swCurve(1) = swEdge(1).GetCurve
    Debug.Print "Is b-curve? " & swCurve(1).IsBcurve
    nApex(0) = 0#: nApex(1) = 0#: nApex(2) = 0#
    vApex = nApex
    Set swSurf = swModeler.CreateRuledSurface(swCurve(0), swCurve(1), (vApex))
    Debug.Print "Type of surface? " & swSurf.Identity
    Debug.Print "Is parametric? " & swSurf.IsParametric
```

```
End Sub
```

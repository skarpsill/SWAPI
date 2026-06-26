---
title: "Sweep Planar Loop Along Vector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sweep_Planar_Loop_Along_Vector_Example_VB.htm"
---

# Sweep Planar Loop Along Vector Example (VBA)

This example shows how to sweep a planar loop along a vector.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Select a planar face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sweeps a planar loop along the specified vector.
' 2. Examine the Immediate window.
'-----------------------------------------------------
```

```
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
    Dim swLoop As SldWorks.Loop2
    Dim vSweepOutput As Variant
    Dim swBody As SldWorks.Body2
    Dim swStopFace(1) As SldWorks.Face2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swLoop = swFace.GetFirstLoop
    vSweepOutput = swLoop.SweepPlanarLoop(0#, 0#, 0.01, 0#)
    If vSweepOutput(0) Is Nothing Then
        Debug.Print "Could not create temporary body; select a different face and rerun the macro."
    Else
        Set swBody = vSweepOutput(0)
        Set swStopFace(0) = vSweepOutput(1)
        Set swStopFace(1) = vSweepOutput(2)
```

```
        Debug.Print "Original face area     = " & swFace.GetArea * 1000000# & " mm^2"
        Debug.Print "  Stop face 1 area     = " & swStopFace(0).GetArea * 1000000# & " mm^2"
        Debug.Print "  Stop face 2 area     = " & swStopFace(1).GetArea * 1000000# & " mm^2"
    End If
```

```
End Sub
```

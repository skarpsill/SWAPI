---
title: "Get Sketch Segment Length Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Length_Example_VB.htm"
---

# Get Sketch Segment Length Example (VBA)

This example shows how to get the length of a sketch segment.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open a part that has a Sketch1 feature of a parabola.
' 2. Select the sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the selected sketch.
' 2. Gets the length of the parabola.
' 3. Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim SelectionManager As SldWorks.SelectionMgr
Dim SketchSegment As SldWorks.SketchSegment
Dim Length As Double
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
    Set SelectionManager = Part.SelectionManager()
    Part.SelectByID "Parabola1@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0
    Set SketchSegment = SelectionManager.GetSelectedObject2(1)
    Length = SketchSegment.GetLength()
    Debug.Print "Length = " & Length * 1000 & " mm"
```

```
End Sub
```

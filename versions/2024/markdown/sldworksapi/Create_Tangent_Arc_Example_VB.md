---
title: "Create Tangent Arc in a Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Tangent_Arc_Example_VB.htm"
---

# Create Tangent Arc in a Sketch Example (VBA)

This example shows how to create a tangent arc in a sketch.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Creates a new part with a sketch of a tangent arc.
' 2. Examine the graphics area.
'---------------------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc

    Part.SketchManager.InsertSketch True
     Dim skSegment As Object
     Set skSegment = Part.SketchManager.CreateLine(-0.060928, 0.026745, 0#, 0.06209, 0.002933, 0#)
     Part.ClearSelection2 True
     Set skSegment = Part.SketchManager.CreateTangentArc(0.06209, 0.002933, 0#, 0.020571, -0.021799, 0#, 1)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

End Sub
```

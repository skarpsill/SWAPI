---
title: "Create 3-Point Arc Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3_Point_Arc_Example_VB.htm"
---

# Create 3-Point Arc Example (VBA)

This example shows how to create a 3-point arc in a sketch.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a new part.
 '
 ' Postconditions:
 ' 1. Creates a 3-point arc in Sketch1.
 ' 2. Examine the graphics area and FeatureManager design tree.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
 Dim boolstatus As Boolean
 Option Explicit
Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", -6.03680341302297E-02, 8.53710569474597E-03, 2.60554052320825E-02, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Set skSegment = Part.SketchManager.Create3PointArc(-0.043992, 0.026681, 0#, 0.033828, 0.037798, 0#, 0.01604, 0.014611, 0#)
     Debug.Print "The sketch is 3D? " & skSegment.GetSketch.Is3D
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
 End Sub
```

---
title: "Create Tangent Arc in a Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Tangent_Arc_Example_VBNET.htm"
---

# Create Tangent Arc in a Sketch Example (VB.NET)

This example shows how to create a tangent arc in a sketch.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Verify that the specified template exists.
 '
 ' Postconditions:
 ' 1. Creates a new part with a sketch of a tangent arc.
 ' 2. Examine the graphics area.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
         Part = swApp.ActiveDoc

         Part.SketchManager.InsertSketch(True)
         Dim skSegment As Object
         skSegment = Part.SketchManager.CreateLine(-0.060928, 0.026745, 0.0#, 0.06209, 0.002933, 0.0#)
         Part.ClearSelection2(True)
         skSegment = Part.SketchManager.CreateTangentArc(0.06209, 0.002933, 0.0#, 0.020571, -0.021799, 0.0#, 1)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```

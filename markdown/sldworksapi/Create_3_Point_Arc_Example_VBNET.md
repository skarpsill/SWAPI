---
title: "Create 3-Point Arc Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3_Point_Arc_Example_VBNET.htm"
---

# Create 3-Point Arc Example (VB.NET)

This example shows how to create a 3-point arc in a sketch.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a new part.
 '
 ' Postconditions:
 ' 1. Creates a 3-point arc in Sketch1.
 ' 2. Examine the graphics area and FeatureManager design tree.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim skSegment As SketchSegment
     Dim boolstatus As Boolean

     Sub main()
         Part = swApp.ActiveDoc
         Part.SketchManager.InsertSketch(True)
         boolstatus = Part.Extension.SelectByID2("Top Plane",  "PLANE", -0.0603680341302297, 0.00853710569474597, 0.0260554052320825,  False, 0,  Nothing, 0)
         Part.ClearSelection2(True)
         skSegment = Part.SketchManager.Create3PointArc(-0.043992, 0.026681, 0.0#, 0.033828, 0.037798, 0.0#, 0.01604, 0.014611, 0.0#)
         Debug.Print("The sketch is 3D? " & skSegment.GetSketch.Is3D)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)
     End Sub

     Public swApp As SldWorks

 End  Class
```

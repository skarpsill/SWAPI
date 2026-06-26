---
title: "Insert Conic Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Conic_Curve_Example_VB.htm"
---

# Insert Conic Curve Example (VBA)

This example shows how to create a conic curve.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Verify that the specified part document template exists.
 '
 ' Postconditions:
 ' 1. Creates a new part.
 ' 2. Inserts a conic curve in the part.
 ' 3. Examine the graphics area.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
Option Explicit
Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc
     Dim skSegment As SldWorks.SketchSegment
     Set skSegment = Part.SketchManager.CreateConic(0.109436, 0.080614, 0#, 0.048742, 0.022907, 0#, -0.017812, 0#, 0#, -0.006092, -0.069601, 0#)
     Part.SketchManager.InsertSketch True
     Part.ShowNamedView2 "*Isometric", 7
 End Sub
```

---
title: "Offset Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Offset_Example_VBNET.htm"
---

# Offset Sketch Example (VB.NET)

This example shows how to offset a sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Creates a new part.
' 2. Sketches a line.
' 3. Offsets the line 2.54 mm in both directions.
' 4. Examine the graphics area.
' ---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSketchManager As SketchManager
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModel = swApp.ActiveDoc
        swSketchManager = swModel.SketchManager
        swModelDocExt = swModel.Extension
        swSketchManager.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", -0.0770466366627886, 0.00233041566204965, 0.0390732100788036, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)

        swSketchSegment = swSketchManager.CreateLine(-0.081532, 0.028203, 0.0#, -0.029228, -0.017264, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(-0.029228, -0.017264, 0.0#, 0.035382, -0.025468, 0.0#)
        swSketchSegment = swSketchManager.CreateLine(0.035382, -0.025468, 0.0#, 0.087008, -0.070346, 0.0#)
        swModel.ClearSelection2(True)

        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, False, 1, Nothing, 0)
        status = swSketchManager.SketchOffset2(0.00254, True, True, swSkOffsetCapEndType_e.swSkOffsetArcCaps, swSkOffsetMakeConstructionType_e.swSkOffsetMakeBothConstruction, True)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

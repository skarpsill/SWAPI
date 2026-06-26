---
title: "Offset Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Offset_Example_VB.htm"
---

# Offset Sketch Example (VBA)

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
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchManager As SldWorks.SketchManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModel = swApp.ActiveDoc
    Set swSketchManager = swModel.SketchManager
    Set swModelDocExt = swModel.Extension
```

```
    swSketchManager.InsertSketch True
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", -7.70466366627886E-02, 2.33041566204965E-03, 3.90732100788036E-02, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
```

```
    Set swSketchSegment = swSketchManager.CreateLine(-0.081532, 0.028203, 0#, -0.029228, -0.017264, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.029228, -0.017264, 0#, 0.035382, -0.025468, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.035382, -0.025468, 0#, 0.087008, -0.070346, 0#)
    swModel.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, False, 1, Nothing, 0)
    status = swSketchManager.SketchOffset2(0.00254, True, True, swSkOffsetCapEndType_e.swSkOffsetArcCaps, swSkOffsetMakeConstructionType_e.swSkOffsetMakeBothConstruction, True)
```

```
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
End Sub
```

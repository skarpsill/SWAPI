---
title: "Trim Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Trim_Sketch_Entities_Example_VB.htm"
---

# Trim Sketch Entities Example (VBA)

This example shows how to trim a sketch to a corner.

```
'--------------------------------------------------------------------------
' Preconditions: Ensure the specified template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Sketches some lines.
' 3. Examine the sketch, then press
'    F5.
' 4. Selects two lines and trims them
'    to a corner.
' 5. Examine the sketch to verify.
'-----------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2018\templates\Part.prtdot", 0, 0, 0)
Set swModelDocExt = swModel.Extension
Set swSketchMgr = swModel.SketchManager
```

```
' Create sketch of lines
status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
swSketchMgr.InsertSketch True
swModel.ClearSelection2 True
Set swSketchSegment = swSketchMgr.CreateLine(-0.055275, 0.03236, 0#, 0.027405, 0.03236, 0#)
Set swSketchSegment = swSketchMgr.CreateLine(0.027405, 0.03236, 0#, 0.027405, -0.026476, 0#)
Set swSketchSegment = swSketchMgr.CreateLine(0.027405, -0.026476, 0#, -0.055275, -0.026476, 0#)
Set swSketchSegment = swSketchMgr.CreateLine(-0.055275, -0.026476, 0#, -0.055275, -0.070758, 0#)
Set swSketchSegment = swSketchMgr.CreateLine(-0.055275, -0.070758, 0#, 0.027405, -0.070758, 0#)
Set swSketchSegment = swSketchMgr.CreateLine(0.027405, -0.070758, 0#, 0.076642, 0.03236, 0#)
swModel.ClearSelection2 True
```

```
Stop
' Examine the sketch before trimming
' the selected lines to a corner
' Press F5
```

```
' Select two lines to trim to a corner
status = swModelDocExt.SelectByID2("Line6", "SKETCHSEGMENT", 3.91723509933775E-02, -4.66042594822396E-02, 0, True, 0, Nothing, 0)
status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 1.93539283564118E-02, -2.64761739915713E-02, 0, True, 0, Nothing, 0)
status = swSketchMgr.SketchTrim(swSketchTrimChoice_e.swSketchTrimCorner, 0, 0, 0)
```

```
swModel.ClearSelection2 True
```

```
End Sub
```

---
title: "Create Spiral Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Spiral_Example_VB.htm"
---

# Create Spiral Example (VBA)

This example shows how to create a spiral.

```
'----------------------------------------------------------
' Preconditions: Specified part template exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Selects Front Plane on which to create a circle.
' 3. Creates a circle.
' 4. Creates a spiral using the circle.
'----------------------------------------------------------
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
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    'Select Front Plane, create circle, and create
    'spiral using circle
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -5.17981810568133E-02, 5.05753331558577E-02, 1.2310671470727E-03, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.021866, 0.001156, 0#)
    swModel.InsertHelix False, True, False, False, swHelixDefinedBy_e.swHelixDefinedBySpiral, 0, 0.04, 2, 0, 4.712388980385
```

```
End Sub
```

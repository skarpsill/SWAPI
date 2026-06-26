---
title: "Dynamically Mirror Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dynamically_Mirror_Sketch_Entities_Example_VB.htm"
---

# Dynamically Mirror Sketch Entities Example (VBA)

This example shows how to enable dynamic sketch mirroring.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldprt.
' 2. Select the top planar face on the part and open a sketch.
' 3. Select an edge on the planar face selected in step 2.
'
' Postconditions:
' 1. Changes sketch mode to dynamic sketch mirror mode.
' 2. Creates a line and mirrors that line about the edge selected
'    in Preconditions step 3.
' 3. Examine the graphics area.
'
' NOTE: Because this part is used elsewhere, do
' not save changes.
'----------------------------------------------
```

```
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSkMgr As SldWorks.SketchManager
    Dim swSketch As SldWorks.Sketch
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim swSelMgr As SldWorks.SelectionMgr
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSkMgr = swModel.SketchManager
    Set swSelMgr = swModel.SelectionManager
```

```
    swSkMgr.SetDynamicMirror (True)
```

```
    Set swSketch = swModel.GetActiveSketch2
    Set swSketchSegment = swModel.CreateLine2(0, 0, 0, 1, 1, 1)
```

```
End Sub
```

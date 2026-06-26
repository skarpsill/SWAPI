---
title: "Split Open Sketch Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_Open_Sketch_Segment_Example_VB.htm"
---

# Split Open Sketch Segment Example (VBA)

This example shows how to split an open sketch segment.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a sketch.
' 2. Creates a line segment.
' 3. Splits the line segment into two segments.
' 4. Examine the Immediate window.
'---------------------------------------------------------------
Option Explicit
```

```vb
Dim SwApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSketchSegment As SldWorks.SketchSegment
 Dim skSegmentArray As Variant
 Dim boolstatus As Boolean
Sub main()
    Set SwApp = Application.SldWorks
     Set swModel = SwApp.ActiveDoc
   SwApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swSketchInference, False
    boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     swModel.SketchManager.InsertSketch True
     swModel.ClearSelection2 True

    'Create a line
     Set swSketchSegment = swModel.SketchManager.CreateLine(-0.055964, 0.033212, 0#, 0.102938, -0.014129, 0#)
     swModel.ViewZoomtofit2

    skSegmentArray = swModel.SketchManager.SplitOpenSegment(0.02, 0.01, 0#)
    ' Close the 3D sketch and rebuild
     swModel.SketchManager.Insert3DSketch True
    Debug.Print "Number of sketch segments = " & UBound(skSegmentArray) + 1

End Sub
```

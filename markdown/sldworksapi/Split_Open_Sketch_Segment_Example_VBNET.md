---
title: "Split Open Sketch Segment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_Open_Sketch_Segment_Example_VBNET.htm"
---

# Split Open Sketch Segment Example (VB.NET)

This example shows how to split an open sketch segment.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swAssembly As AssemblyDoc
     Dim swSketchMgr As SketchManager
     Dim swSketchSegment As SketchSegment
     Dim skSegmentArray As Object
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchInference, False)

         boolstatus = swModel.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  False, 0,  Nothing, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)

         ' Create a line
         swSketchSegment = swModel.SketchManager.CreateLine(-0.055964, 0.033212, 0.0#, 0.102938, -0.014129, 0.0#)
         swModel.ViewZoomtofit2()

         skSegmentArray = swModel.SketchManager.SplitOpenSegment(0.02, 0.01, 0.0#)

         ' Close the sketch and rebuild
         swModel.SketchManager.Insert3DSketch(True)
        Debug.Print("Number of segments in sketch = " & UBound(skSegmentArray) + 1)

     End Sub

     Public swApp As SldWorks

 End  Class
```

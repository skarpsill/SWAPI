---
title: "Split Closed Sketch Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_Closed_Sketch_Segment_Example_VB.htm"
---

# Split Closed Sketch Segment Example (VBA)

This example shows how to split a closed sketch segment.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a new part document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens a sketch.
 ' 2. Creates a closed spline.
 ' 3. Splits the spline into two segments.
 ' 4. Examine the Immediate window.
 '----------------------------------------------------------------
Option Explicit
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

    Dim pointArray As Variant
     Dim points() As Double
     ReDim points(0 To 20) As Double
     points(0) = -2.43607314462504E-02
     points(1) = 4.04155099449417E-02
     points(2) = 0
     points(3) = -8.49151208568891E-04
     points(4) = 4.70352752545802E-02
     points(5) = 0
     points(6) = 0
     points(7) = 3.95024388677502E-02
     points(8) = 0
     points(9) = -5.30037270987752E-03
     points(10) = 3.58501545589842E-02
     points(11) = 0
     points(12) = -7.12651486426054E-03
     points(13) = 2.83173181721542E-02
     points(14) = 0
     points(15) = -0.023219392599761
     points(16) = 2.95727909032925E-02
     points(17) = 0
     points(18) = -2.43607314462504E-02
     points(19) = 4.04155099449417E-02
     points(20) = 0
     pointArray = points
     Dim skSegment As Object
     Set skSegment = swModel.SketchManager.CreateSpline((pointArray))
     swModel.ViewZoomtofit2

    skSegmentArray = swModel.SketchManager.SplitClosedSegment(-2.43607314462504E-02, 4.04155099449417E-02, 0#, -0.023219392599761, 2.95727909032925E-02, 0#)
    ' Close the sketch and rebuild
     swModel.SketchManager.Insert3DSketch True
    Debug.Print "Number of segments in sketch = " & UBound(skSegmentArray) + 1
End Sub
```

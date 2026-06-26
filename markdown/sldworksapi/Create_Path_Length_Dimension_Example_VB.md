---
title: "Create Path Length Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Path_Length_Dimension_Example_VB.htm"
---

# Create Path Length Dimension Example (VBA)

This example shows how to create a path length dimension.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a new part document.
 '
 ' Postconditions: Select Sketch1 in the FeatureManager design tree to see
 ' the path length dimension of 15.75.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myDisplayDim As SldWorks.DisplayDimension
Dim boolstatus As Boolean
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swInputDimValOnCreate, False

    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
     Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-0.075, 0.05, 0, 0.05, -0.025, 0)
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.SketchManager.MakeSketchChain()
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 6.61546453402301E-03, 5.08003665223665E-02, 0, False, 0, Nothing, 0)

     Set myDisplayDim = Part.Extension.AddPathLengthDim(-5.80395474035344E-02, 8.41706952643316E-02, 0)
     Part.SketchManager.InsertSketch True

End Sub
```

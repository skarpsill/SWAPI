---
title: "Create Path Length Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Path_Length_Dimension_Example_VBNET.htm"
---

# Create Path Length Dimension Example (VB.NET)

This example shows how to create a path length dimension.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a new part document.
 '
 ' Postconditions: Select Sketch1 in the FeatureManager design tree to
 ' see the path length dimension of 15.75.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myDisplayDim As DisplayDimension
     Dim boolstatus As Boolean

     Sub main()

         swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swInputDimValOnCreate, False)

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  False, 0,  Nothing, 0)
         Part.SketchManager.InsertSketch(True)
         Part.ClearSelection2(True)
         Dim vSkLines As Object
         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.075, 0.05, 0, 0.05, -0.025, 0)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = Part.SketchManager.MakeSketchChain()
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0.00661546453402301, 0.0508003665223665, 0,  False, 0,  Nothing, 0)

         myDisplayDim = Part.Extension.AddPathLengthDim(-0.0580395474035344, 0.0841706952643316, 0)
         Part.SketchManager.InsertSketch(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```

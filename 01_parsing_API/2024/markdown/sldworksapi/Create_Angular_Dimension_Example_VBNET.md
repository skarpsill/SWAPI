---
title: "Create Angular Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Angular_Dimension_Example_VBNET.htm"
---

# Create Angular Dimension Example (VB.NET)

This example shows how to add an angular display dimension to a sketch.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\box.sldprt.
 ' 2. Press F8 repeatedly to step through the macro.
 '
 ' Postconditions:
 ' 1. Edits Sketch1.
 ' 2. Creates an angular dimension.
 ' 3. Displays the dimension for:
 '    * Angle defined by the selected sketch segment and an extension line
 '      that is drawn to the right of the selected sketch point
 '      (Direction = swSmartDimensionDirection_Right)
 '    * Explementary angle
 '    * Vertically opposite angle
 '
  ' NOTE: Because the model is used elsewhere, do not save changes to it.
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

         Part = swApp.ActiveDoc
         Stop
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         Part.EditSketch()

         boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -0.0672289031567236, 0.0180603779387131, 0.0184698306816742, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Point1", "SKETCHPOINT", -0.0811067833265636, 0.0389478433654258, 0, True, 0, Nothing, 0)

         myDisplayDim = Part.Extension.AddDimension(-0.0456250220540824, 0, 0.00150965590938767, swSmartDimensionDirection_e.swSmartDimensionDirection_Right)
         myDisplayDim.ExplementaryAngle()
         myDisplayDim.VerticallyOppositeAngle()

         Part.SketchManager.InsertSketch(True)

     End Sub

     Public swApp As SldWorks

 End Class
```

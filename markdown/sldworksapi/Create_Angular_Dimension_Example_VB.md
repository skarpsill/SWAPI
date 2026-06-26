---
title: "Create Angular Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Angular_Dimension_Example_VB.htm"
---

# Create Angular Dimension Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myDisplayDim As SldWorks.DisplayDimension
 Dim boolstatus As Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditSketch
    boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -6.72289031567236E-02, 1.80603779387131E-02, 1.84698306816742E-02, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Point1", "SKETCHPOINT", -8.11067833265636E-02, 3.89478433654258E-02, 0, True, 0, Nothing, 0)
    Set myDisplayDim = Part.Extension.AddDimension(-4.56250220540824E-02, 0, 1.50965590938767E-03, swSmartDimensionDirection_Right)
     myDisplayDim.ExplementaryAngle
     myDisplayDim.VerticallyOppositeAngle

     Part.SketchManager.InsertSketch True

End Sub
```

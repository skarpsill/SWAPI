---
title: "Create Specific Dimension in a Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Specific_Dimension_Example_VB.htm"
---

# Create Specific Dimension in a Sketch Example (VBA)

This example shows how to add an angular display dimension to a sketch.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\box.sldprt.
 '
 ' Postconditions:
 ' 1. Edits Sketch1.
 ' 2. Selects two intersecting lines.
 ' 3. Creates an angular display dimension at the specified location in the
 '    sketch.
 ' 4. Inserts Sketch1.
 ' 5. Inspect Sketch1 in the graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes to it.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myDisplayDim As SldWorks.DisplayDimension
 Dim boolstatus As Boolean
 Dim error As Long
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

    Part.EditSketch
    boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", -5.09671483361161E-02, -1.09842011554073E-02, 2.96211826739789E-02, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -7.70411440149667E-02, 4.96030150977761E-03, 3.25476150359756E-02, True, 0, Nothing, 0)
    Set myDisplayDim = Part.Extension.AddSpecificDimension(-4.56250220540824E-02, 0, 1.50965590938767E-03, swAngularDimension, error)

    Part.SketchManager.InsertSketch True

End Sub
```

---
title: "Create Specific Dimension in a Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Specific_Dimension_Example_VBNET.htm"
---

# Create Specific Dimension in a Sketch Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myDisplayDim As DisplayDimension
     Dim boolstatus As Boolean
     Dim err As Integer

     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

         Part.EditSketch

         boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", -0.0509671483361161, -0.0109842011554073, 0.0296211826739789, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", -0.0770411440149667, 0.00496030150977761, 0.0325476150359756, True, 0, Nothing, 0)
         myDisplayDim = Part.Extension.AddSpecificDimension(-0.0456250220540824, 0, 0.00150965590938767, swDimensionType_e.swAngularDimension, err)

         Part.SketchManager.InsertSketch(True)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

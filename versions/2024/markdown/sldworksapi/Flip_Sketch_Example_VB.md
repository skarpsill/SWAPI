---
title: "Flip Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Sketch_Example_VB.htm"
---

# Flip Sketch Example (VBA)

This example shows how to flip a sketch about a coordinate system axis.

```vb
 '-------------------------------------------------------------------------
 ' Preconditions: Open a model document and select a sketch.
 '
 ' Postconditions: Flips the sketch about the x axis.
 '------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
    swModel.SketchModifyFlip 1
End Sub
```

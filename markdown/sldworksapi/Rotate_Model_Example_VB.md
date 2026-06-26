---
title: "Rotate Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Model_Example_VB.htm"
---

# Rotate Model Example (VBA)

This example shows how to rotate a model in the graphics area.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Watch the graphics while the macro runs.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Inserts and extrudes a rectangular sketch.
' 3. Rotates the sketch multiple times.
'---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim myFeature As SldWorks.Feature

Dim vSkLines As Variant

Dim boolstatus As Boolean

Option Explicit

Sub main()
```

```vb
    Set swApp = Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2012\templates\Part.prtdot", 0, 0, 0)

    boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", -5.67254111166863E-02, 7.53958008310182E-03, 2.48109468921342E-02, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True

    vSkLines = Part.SketchManager.CreateCornerRectangle(-4.93169981371904E-02, 1.73783707721528E-02, 0, 5.58925978888158E-02, -4.55595125648331E-02, 0)
     Part.ShowNamedView2 "*Trimetric", 8
    boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.016256, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False

    Part.ViewRotate
     Part.ViewRotateminusx
     Part.ViewRotateminusy
     Part.ViewRotateminusz
     Part.ViewRotateplusx
     Part.ViewRotateplusy
     Part.ViewRotateplusz
     Part.ViewRotXMinusNinety
     Part.ViewRotXPlusNinety
     Part.ViewRotYMinusNinety
     Part.ViewRotYPlusNinety

End Sub
```

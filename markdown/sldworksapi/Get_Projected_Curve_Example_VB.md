---
title: "Get Projected Curve Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Projected_Curve_Example_VB.htm"
---

# Get Projected Curve Example (VBA)

This example shows how to bidirectionally project a sketch onto a face.

```
'----------------------------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Creates a thin extrusion of a circle.
' 2. Sketches a corner rectangle on the Top Plane.
' 3. Selects the sketch and the inner face of the extrusion.
' 4. Bidirectionally projects the sketch onto the inner face, creating Curve1.
' 5. Examine the FeatureManager design tree and the graphics area.
'----------------------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swPart As PartDoc
 Dim swSheetWidth As Double
 Dim swSheetHeight As Double
 Dim defTemplate As String
 Dim skSegment As SldWorks.SketchSegment
 Dim myFeature As SldWorks.Feature
 Dim swFeat As SldWorks.Feature
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim swFeatData As SldWorks.ProjectionCurveFeatureData
 Dim vSkLines As Variant
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    swSheetWidth = 0
     swSheetHeight = 0

    defTemplate = swApp.GetUserPreferenceStringValue(swDefaultTemplatePart)

    Set Part = swApp.NewDocument(defTemplate, 0, swSheetWidth, swSheetHeight)
     Set swPart = Part
     swApp.ActivateDoc2 "Part1", False, longstatus
     Set Part = swApp.ActiveDoc

    Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True

    Set skSegment = Part.SketchManager.CreateCircle(0#, 0#, 0#, 0#, 0.075937, 0#)

    boolstatus = Part.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)

    Set myFeature = Part.FeatureManager.FeatureExtrusionThin2(True, False, False, 0, 0, 0.05, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, 0.01, 0.01, 0.01, 0, 0, False, 0.005, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False
     boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     Set skSegment = Part.SketchManager.CreateLine(-0.015062, -0.011566, 0#, -0.020354, -0.032124, 0#)
     Part.SetPickMode
     Part.ClearSelection2 True
     vSkLines = Part.SketchManager.CreateCornerRectangle(0, -1.27873930746226E-02, 0, 9.77008554030195E-03, -3.21240207064702E-02, 0)
     Part.SetPickMode
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True

    boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 4.47795587263838E-03, -1.27873930746226E-02, 0, True, 2, Nothing, 0)
     boolstatus = Part.Extension.SelectByRay(8.5488248477642E-03, -0.075454504318941, 2.93545895954139E-02, 0, -0.707106781186541, 0.707106781186554, 6.92047725771388E-04, 2, True, 1, 0)

    Set swFeatMgr = Part.FeatureManager

    Set swFeatData = swFeatMgr.CreateDefinition(swFmRefCurve)
     swFeatData.Bidirectional = True
     swFeatData.Reverse = False
     Set swFeat = swFeatMgr.CreateFeature(swFeatData)
     Part.ClearSelection2 True

End Sub
```

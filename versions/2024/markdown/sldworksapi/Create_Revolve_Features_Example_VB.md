---
title: "Create Revolve Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Revolve_Features_Example_VB.htm"
---

# Create Revolve Features Example (VBA)

This example shows how to create revolve features.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a new part document.
 '
 ' Postconditions: Two revolve features and one cut-revolve feature are created.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager

    ' Create an axis
     boolstatus = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, True, 0, Nothing, swSelectOptionDefault)
     boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, swSelectOptionDefault)
     swModel.InsertAxis2 True

    ' Create a rectangle
     boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", -0.08954836342753, 4.336873289503E-04, 0.006720765739942, False, 0, Nothing, swSelectOptionDefault)
     swModel.InsertSketch2 True
     swModel.ClearSelection2 True
     swModel.SketchRectangle -0.05668466821757, -0.02198379306525, 0, -0.01330857427717, 0.03972855876814, 0, 1

    ' Create the first revolve feature
     swModel.InsertSketch2 True
     swModel.ShowNamedView2 "*Trimetric", 8

    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
     boolstatus = swModelDocExt.SelectByID2("Axis1", "AXIS", 0, 0, 0, True, 16, Nothing, swSelectOptionDefault)
     Set swFeatMgr = swModel.FeatureManager

     swFeatMgr.FeatureRevolve2 True, True, False, False, False, False, 0, 0, 6.28318530718, 0, False, False, 0.01, 0.01, 0, 0, 0, True, True, True

    ' Create a cut-revolve feature using a face on the revolve feature
     swSelMgr.EnableContourSelection = 0
     boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.03095803920934, 0.01509536510872, 0.02198379306526, False, 0, Nothing, swSelectOptionDefault)
     swModel.InsertSketch2 True
     swModel.ClearSelection2 True
     swModel.SketchRectangle -0.04194874421597, 0.01774859621099, 0, -0.01883036471929, -0.01265654504095, 0, 1
     swModel.InsertSketch2 True

    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
     boolstatus = swModelDocExt.SelectByID2("Line4@Sketch2", "EXTSKETCHSEGMENT", -0.01883036471929, 0.003802500010693, 0, True, 4, Nothing, swSelectOptionDefault)
     swFeatMgr.FeatureRevolveCut 6.26573201466, False, 0, 0, 0, 1, 1

    ' Create the second revolve feature using a face on the first revolve feature
     swSelMgr.EnableContourSelection = 0
     boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02333512246603, 0.03472018719853, 0.0219837930652, False, 0, Nothing, swSelectOptionDefault)
     swModel.InsertSketch2 True
     swModel.ClearSelection2 True
     swModel.CreateCircle2 -0.02232361399104, 0.03354683337932, 0, -0.01445073476016, 0.02795861773112, 0
     swModel.InsertSketch2 True

    boolstatus = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)

    boolstatus = swModelDocExt.SelectByRay(-1.81956067901865E-02, 1.80455411334037E-02, 2.17820530671702E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 9.91972972972973E-04, 1, False, 4, 0)

     swFeatMgr.FeatureRevolve2 True, True, False, False, False, False, 0, 0, 6.28318530718, 0, False, False, 0.01, 0.01, 0, 0, 0, True, True, True
     swSelMgr.EnableContourSelection = 0
End Sub
```

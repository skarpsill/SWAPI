---
title: "Get Rib Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Rib_Feature_Data_Example_VB.htm"
---

# Get Rib Feature Data Example (VBA)

This example shows how to get rib feature data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part document.
 ' 2. Creates Shell1, Plane1, and Rib1.
 ' 3. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myRefPlane As SldWorks.RefPlane
 Dim skSegment As SldWorks.SketchSegment
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swRibFeat As SldWorks.RibFeatureData2
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20", False, longstatus
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("", "FACE", -8.78816842651986E-03, 3.96239999998897E-02, -2.92468281514857E-02, False, 1, Nothing, 0)
     Part.InsertFeatureShell 0.00254, False

    boolstatus = Part.Extension.SelectByID2("", "FACE", 2.64031138414111E-03, 0.028407059059532, -6.13970439424634E-02, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -0.059937899786064, 2.77866864457792E-02, -8.77977980189826E-03, True, 1, Nothing, 0)

    Set myRefPlane = Part.FeatureManager.InsertRefPlane(128, 0, 128, 0, 0, 0)
     Part.ClearSelection2 True

    boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 6.64896553058725E-03, 0.109417877974863, 5.24178648701081E-02, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True
    Set skSegment = Part.SketchManager.CreateLine(-0.085797, 0.021082, 0#, -0.03423, 0.035134, 0#)
     Set skSegment = Part.SketchManager.CreateLine(-0.03423, 0.035134, 0#, 0.007726, 0.025357, 0#)
     Set skSegment = Part.SketchManager.CreateLine(0.007726, 0.025357, 0#, 0.111514, 0.039624, 0#)
     Part.ClearSelection2 True
    Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     Part.FeatureManager.InsertRib True, False, 0.00254, 0, False, False, True, 1.74532925199433E-02, False, False

    Set swSelMgr = Part.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swRibFeat = swFeat.GetDefinition
    Debug.Print "Rib feature type as defined in swRibType_e: " & swRibFeat.Type
     Debug.Print "Thickness: " & swRibFeat.Thickness
     Debug.Print "Extrusion direction as defined in swRibExtrusionDirection_e: " & swRibFeat.ExtrusionDirection
     Debug.Print "Rib has a draft? " & swRibFeat.EnableDraft
     If swRibFeat.EnableDraft Then
         Debug.Print "    Draft angle: " & swRibFeat.DraftAngle
         Debug.Print "    Draft outward? " & swRibFeat.DraftOutward
     End If
     Debug.Print "Add material to reverse side of the rib? " & swRibFeat.FlipSide
     Debug.Print "Rib is extruded on two sides of the midplane? " & swRibFeat.IsTwoSided
     If Not swRibFeat.IsTwoSided Then
         Debug.Print "Single-sided rib is extruded on the reverse side? " & swRibFeat.ReverseThicknessDir
     End If

End Sub
```

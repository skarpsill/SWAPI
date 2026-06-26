---
title: "Create Replace Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Face_Example_VB.htm"
---

# Create Replace Face Feature Example (VBA)

This example shows how to create a Replace Face feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part.
 ' 2. Creates Plane1, Surface-Extrude1, and Replace Face1.
 ' 3. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim selMgr As SldWorks.SelectionMgr
 Dim Part As SldWorks.ModelDoc2
 Dim feat As SldWorks.Feature
 Dim featData As SldWorks.ReplaceFaceFeatureData
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20", False, longstatus
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("", "FACE", 6.87152192142548E-03, 2.56655537640995E-02, 0.049345602378537, True, 0, Nothing, 0)
     Dim myRefPlane As SldWorks.RefPlane
     Set myRefPlane = Part.FeatureManager.InsertRefPlane(264, 0.05842, 0, 0, 0, 0)
     Part.ClearSelection2 True

    Dim pointArray As Variant
     Dim points() As Double
     ReDim points(0 To 14) As Double
     points(0) = -7.00496017443584E-02
     points(1) = 5.82762055241233E-02
     points(2) = 0
     points(3) = -3.57558994484748E-02
     points(4) = 8.53945497913173E-02
     points(5) = 0
     points(6) = -5.88719099721402E-03
     points(7) = 6.71372129016845E-02
     points(8) = 0
     points(9) = 2.73002628375139E-02
     points(10) = 8.78577815467452E-02
     points(11) = 0
     points(12) = 7.37626982062238E-02
     points(13) = 5.82762055241233E-02
     points(14) = 0
     pointArray = points
     Dim skSegment As SldWorks.SketchSegment
     Set skSegment = Part.SketchManager.CreateSpline((pointArray))
     Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Spline1@Sketch2", "EXTSKETCHSEGMENT", -5.49544681183813E-02, 8.75052976097064E-02, 0, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
     Part.SelectionManager.EnableContourSelection = True
     boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCHCONTOUR", 0, 0, 0, True, 4, Nothing, 0)
     Part.FeatureExtruRefSurface2 True, False, False, 0, 0, 0.14478, 0.14478, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False
     Part.SelectionManager.EnableContourSelection = False
     boolstatus = Part.Extension.SelectByID2("", "FACE", 5.85444908073214E-02, 3.96239999998329E-02, -5.18899759430838E-02, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -1.89730427370591E-02, 7.26880897401543E-02, 0.115671174990496, True, 0, Nothing, 0)
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", 5.85444908073214E-02, 3.96239999998329E-02, -5.18899759430838E-02, True, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -1.89730427370591E-02, 7.26880897401543E-02, 0.115671174990496, True, 2, Nothing, 0)
     Part.InsertFeatureReplaceFace
     boolstatus = Part.Extension.SelectByID2("", "FACE", -3.62064915135534E-02, 8.56902732399476E-02, 0.127037337239983, False, 0, Nothing, 0)
     Part.FeatureManager.HideBodies
     boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -6.93294107213475E-02, 8.72697709380442E-02, -3.00713252946179E-02, False, 0, Nothing, 0)
     Part.BlankRefGeom

    boolstatus = Part.Extension.SelectByID2("Replace Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Set selMgr = Part.SelectionManager
     Set feat = selMgr.GetSelectedObject6(1, -1)
     Set featData = feat.GetDefinition

    featData.AccessSelections Part, Nothing

    Dim vFacesToReplace As Variant
     vFacesToReplace = featData.FacesForReplacement
     Debug.Print featData.GetFacesForReplacementCount & " face replaced in " & vFacesToReplace(0).GetFeature.Name
     Debug.Print featData.GetReplacementSurfacesCount & " replacement surface "
    featData.ReleaseSelectionAccess
End Sub
```

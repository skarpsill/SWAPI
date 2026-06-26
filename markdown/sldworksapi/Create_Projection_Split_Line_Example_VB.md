---
title: "Create Projection Split Line Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Projection_Split_Line_Example_VB.htm"
---

# Create Projection Split Line Feature Example (VBA)

This example shows how to create a projection split line feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document with a feature extrusion, reference plane,
 '    and sketch of an ellipse.
 ' 2. Creates Split Line1 in the FeatureManager design tree.
 ' 3. Inspect the Immediate window.
 '----------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
 Dim myRefPlane As SldWorks.RefPlane
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swSplitLine As SldWorks.SplitLineFeatureData
 Dim vSkLines As Variant
 Dim myFeature As SldWorks.Feature
 Dim boolstatus As Boolean
 Dim longstatus As Long
Sub main()
    Set swApp = Application.SldWorks
    Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc

     Set skSegment = Part.SketchManager.CreateEllipse(-2.12512457655407E-02, 1.22505076014363E-02, 0, 2.77468345541365E-03, 7.05202391259263E-03, 0, -1.96159170237913E-02, 1.98085370103935E-02, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    Set myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.01778, 0, 0, 0, 0)
     Part.ClearSelection2 True

    Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -4.07148636658249E-02, 2.47341229458697E-02, 1.94913387248102E-02, False, 0, Nothing, 0)
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
     boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)

    vSkLines = Part.SketchManager.CreateCornerRectangle(-6.25406077424486E-02, 2.97244912047745E-02, 0, 5.84903577919818E-02, -0.018090206988802, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
     Part.SelectionManager.EnableContourSelection = False

    boolstatus = Part.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", -1.43044793836914E-02, 3.34438727079956E-03, 0, True, 4, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -1.81817275523031E-02, 1.32444059746035E-02, 1.77800000000161E-02, True, 1, Nothing, 0)

    Part.InsertSplitLineProject True, True

    Set swSelMgr = Part.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData

    boolstatus = Part.Extension.SelectByID2("Split Line1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

    Set myFeature = swSelMgr.GetSelectedObject6(1, -1)
     Set swSplitLine = myFeature.GetDefinition

    ' Get split line feature data
      boolstatus = swSplitLine.AccessSelections(Part, Nothing)

     Debug.Print myFeature.Name
     Debug.Print "    Split type as defined in swSplitLineFeatureType_e: " & swSplitLine.GetType
     Debug.Print "    Single Direction? " & swSplitLine.SingleDirection
     Debug.Print "    Reversed? " & swSplitLine.ReverseDirection

    swSplitLine.ReleaseSelectionAccess
End Sub
```

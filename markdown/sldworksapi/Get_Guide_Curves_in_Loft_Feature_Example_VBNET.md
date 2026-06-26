---
title: "Get Guide Curves in Loft Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Guide_Curves_in_Loft_Feature_Example_VBNET.htm"
---

# Get Guide Curves in Loft Feature Example (VB.NET)

This example shows how to get the guide curves in a loft feature.

```
'----------------------------------------
' Preconditions:
' 1. Verify that the specified part document
'    template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Creates a loft feature.
' 3. Prints to the Immediate window
'    the feature type and feature name of the loft
'    feature.
' 4. Accesses the guide curves in the loft feature.
' 5. Prints to the Immediate window whether the
'    loft is a boss feature, the number guide
'    curves in the loft, and the feature types of the
'    guide curves.
' 6. Releases access to the loft feature.
' 7. Examine the Immediate window.
'----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swFeatureManager As FeatureManager
    Dim swRefPlane As RefPlane
    Dim swSketchManager As SketchManager
    Dim swSketchSegment As SketchSegment
    Dim swFeature As Feature
    Dim swLoftFeatureData As LoftFeatureData
    Dim pointArray As Object
    Dim points() As Double
    Dim guideCurves As Object
    Dim guideCurve As Object
    Dim nbrGuideCurves As Integer
    Dim i As Integer
    Dim status As Boolean

    Public Sub Main()

        'Open new part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Create reference plane
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swRefPlane = swFeatureManager.InsertRefPlane(8, 0.0635, 0, 0, 0, 0)
        swModel.ClearSelection2(True)

        'Create circle for loft feature
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateCircle(-0.0#, 0.0#, 0.0#, 0.003857, -0.009744, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Create another circle for loft feature
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateCircle(-0.0#, 0.0#, 0.0#, 0.014007, -0.029232, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Create sketch for guide curve
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        ReDim points(8)
        points(0) = 0
        points(1) = 0.0324150959148675
        points(2) = 0
        points(3) = 0.02176137524458
        points(4) = 0.0209549481725162
        points(5) = 0
        points(6) = 0.0635
        points(7) = 0.0104797609372824
        points(8) = 0
        pointArray = points
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateSpline((pointArray))
        swSketchManager.InsertSketch(True)

        'Create loft feature with guide curve
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0635, 0, -0.0104797609372824, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, -0.0324150959148675, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 4098, Nothing, 0)
        swFeature = swFeatureManager.InsertProtrusionBlend2(False, True, False, 1, 0, 0, 1, 1, True, True, False, 0, 0, 0, True, True, True, swGuideCurveInfluence_e.swGuideCurveInfluenceNextGlobal)
        Debug.Print("Feature:")
        Debug.Print("  Type: " & swFeature.GetTypeName2)
        Debug.Print("  Name: " & swFeature.Name)

        'Change the orientation of the view
        swModel.ShowNamedView2("*Isometric", 7)

        'Access loft feature data, get guide curves,
        'get feature type of guide curves, and release
        'access to loft feature
        swLoftFeatureData = swFeature.GetDefinition
        Debug.Print("   Boss feature: " & swLoftFeatureData.IsBossFeature)
        nbrGuideCurves = swLoftFeatureData.GetGuideCurvesCount
        Debug.Print("   Number of guide curves: " & nbrGuideCurves)
        status = swLoftFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("    Guide curve: ")
        guideCurves = swLoftFeatureData.guideCurves
        For i = 0 To (nbrGuideCurves - 1)
            guideCurve = guideCurves(i)
            Debug.Print("        Type of feature: " & swLoftFeatureData.GetGuideCurvesType(i))
        Next i
        swLoftFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

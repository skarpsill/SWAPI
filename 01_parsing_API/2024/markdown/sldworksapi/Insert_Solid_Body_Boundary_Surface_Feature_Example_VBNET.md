---
title: "Insert Solid Body Boundary Surface Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Solid_Body_Boundary_Surface_Feature_Example_VBNET.htm"
---

# Insert Solid Body Boundary Surface Feature Example (VB.NET)

This example shows how to insert a solid body boundary surface feature.

```
'-------------------------------------------------------------
' Preconditions: Verify that the specified part template
' exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Inserts a sketch of a rectangle, Sketch1, on Front Plane.
' 3. Creates Surface-Plane1 using Sketch1.
' 4. Creates Plane1.
' 5. Creates a sketch of a circle, Sketch2, on Plane1.
' 6. Creates Surface-Plane2 using Sketch2.
' 7. Inserts a solid body boundary surface feature, Boundary-Surface1,
'    using Surface-Plane1 and Surface-Plane2.
' 8. Examine the graphics area and expand Solid Bodies(1) in the
'    FeatureManager design tree to verify step 7.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureMgr As FeatureManager
        Dim swSketchMgr As SketchManager
        Dim swRefPlane As RefPlane
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim sketchSegments As Object
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swFeatureMgr = swModel.FeatureManager

        'Create Surface-Plane1
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0687189668956523, 0.0593633502290038, 0.00936526409663904, False, 0, Nothing, 0)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchSegments = swSketchMgr.CreateCornerRectangle(-0.0399911197344551, 0.02969400507229, 0, 0.0502882343966202, -0.0299334728551311, 0)
        swSketchMgr.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModel.InsertPlanarRefSurface()
        swModel.ClearSelection2(True)

        'Create Plane1
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swRefPlane = swFeatureMgr.InsertRefPlane(swRefPlaneReferenceConstraints_e.swRefPlaneReferenceConstraint_Distance, 0.15, 0, 0, 0, 0)
        swModel.ClearSelection2(True)

        'Create Surface-Plane2
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swSketchSegment = swSketchMgr.CreateCircle(0.003592, 0.003353, 0.0#, 0.035202, -0.057233, 0.0#)
        swSketchMgr.InsertSketch(True)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
        status = swModel.InsertPlanarRefSurface()
        swModel.ClearSelection2(True)
        swModel.ViewZoomtofit2()

        'Insert a solid body boundary surface feature
        status = swModelDocExt.SelectByID2("Surface-Plane1", "SURFACEBODY", -0.0399911197344551, 0.02969400507229, 0, False, 8193, Nothing, 0)
        status = swModelDocExt.SelectByID2("Surface-Plane2", "SURFACEBODY", -0.0463651179854531, -0.0432741101197696, 0.15, True, 16385, Nothing, 0)
        swFeature = swFeatureMgr.SetNetBlendCurveData(0, 0, swTangencyType_e.swTangencyNone, 0, 1, True)
        swFeature = swFeatureMgr.SetNetBlendCurveData(0, 1, swTangencyType_e.swTangencyNone, 0, 1, True)
        swFeature = swFeatureMgr.SetNetBlendDirectionData(0, 32, 0, False, False)
        swFeature = swFeatureMgr.SetNetBlendDirectionData(1, 32, 0, False, False)
        swFeature = swFeatureMgr.InsertNetBlend2(2, 2, 0, False, 0.0001, False, True, True, True, False, -1, -1, False, -1, False, False, -1, False, -1, True, True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

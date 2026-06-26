---
title: "Insert Extruded Surface Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Extruded_Reference_Surface_Example_VBNET.htm"
---

# Insert Extruded Surface Example (VB.NET)

This example shows how to insert an extruded surface in a model.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part and inserts Surface-Extrude1.
' 2. Expand the Surface Bodies folder to verify that it contains:
'    * Surface-Extrude[1]
'    * Surface-Extrude[2]
'    * Surface-Extrude[3]
' 3. Examine the Immediate window and graphics area.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim sketchLines As Object
        Dim swSketchSegment As SketchSegment
        Dim swSelMgr As SelectionMgr
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swSurfExtrudeFeature As SurfExtrudeFeatureData
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

        'Create sketches for extruded surface feature
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.03891024234798, 0.02968528649877, 0.0003646590412283, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        sketchLines = swSketchManager.CreateCornerRectangle(-0.05517876768764, 0.008130204900836, 0, -0.02399076855985, -0.0155939995639, 0)
        swModel.ClearSelection2(True)
        sketchLines = swSketchManager.CreateCornerRectangle(-0.003731897331531, 0.008130204900836, 0, 0.0285223581767, -0.02998846069981, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateCircle(0.053579, 0.013995, 0.0#, 0.06819, 0.018462, 0.0#)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModel.ShowNamedView2("*Trimetric", 8)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

        ' Create a blind surface extrude
        ' in two directions from the selected sketch
        ' in a direction normal to the selected sketch plane
        swFeatureManager = swModel.FeatureManager
        swFeatureManager.FeatureExtruRefSurface3(False, False, swStartConditions_e.swStartSketchPlane, 0, swEndConditions_e.swEndCondBlind, swEndConditions_e.swEndCondBlind, 0.01, 0.01, True, False, False, False, 0.4, 0, False, False, False, False, False, False, False, False)
        swModel.ClearSelection2(True)

        ' Get Surface-Extrude1 feature
        swSelMgr = swModel.SelectionManager
        status = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swSurfExtrudeFeature = swFeature.GetDefinition

        'Access Surface-Extrude1 feature data
        swSurfExtrudeFeature.AccessSelections(swModel, Nothing)

        Debug.Print(swFeature.Name)
        Debug.Print("  Depth:")
        Debug.Print("    Forward direction: " & swSurfExtrudeFeature.GetDepth(True))
        Debug.Print("    Reverse direction: " & swSurfExtrudeFeature.GetDepth(False))
        Debug.Print("  End condition as defined in swSurfaceExtendEndCond_e:")
        Debug.Print("    Forward direction: " & swSurfExtrudeFeature.GetEndCondition(True))
        Debug.Print("    Reverse direction: " & swSurfExtrudeFeature.GetEndCondition(False))
        Debug.Print("  Reverse offset enabled:")
        Debug.Print("    Forward direction? " & swSurfExtrudeFeature.GetReverseOffset(True))
        Debug.Print("    Reverse direction? " & swSurfExtrudeFeature.GetReverseOffset(False))
        Debug.Print("  Translate surface setting enabled:")
        Debug.Print("    Forward direction? " & swSurfExtrudeFeature.GetTranslateSurface(True))
        Debug.Print("    Reverse direction? " & swSurfExtrudeFeature.GetTranslateSurface(False))
        Debug.Print("  Surface extruded in both directions? " & swSurfExtrudeFeature.BothDirections)
        Debug.Print("  Extrusion reversed? " & swSurfExtrudeFeature.ReverseDirection)
        Debug.Print("  Direction 1 end:")
        Debug.Print("    Capped? " & swSurfExtrudeFeature.D1CapEnd)
        Debug.Print("    Drafted? " & swSurfExtrudeFeature.D1DraftOn)
        If swSurfExtrudeFeature.D1DraftOn Then
            Debug.Print("      Angle: " & swSurfExtrudeFeature.D1DraftAngle)
            Debug.Print("      Inward (false) or outward (true)? " & swSurfExtrudeFeature.D1DraftOutward)
        End If
        Debug.Print("  Direction 2 end:")
        Debug.Print("    Capped? " & swSurfExtrudeFeature.D2CapEnd)
        Debug.Print("    Drafted? " & swSurfExtrudeFeature.D2DraftOn)
        If swSurfExtrudeFeature.D2DraftOn Then
            Debug.Print("      Angle: " & swSurfExtrudeFeature.D2DraftAngle)
            Debug.Print("      Inward (false) or outward (true)? " & swSurfExtrudeFeature.D2DraftOutward)
        End If
        Debug.Print("  Delete original face? " & swSurfExtrudeFeature.DeleteOriginalFace)
        Debug.Print("  Knit extrusion result? " & swSurfExtrudeFeature.KnitResult)

        'Release Surface-Extrude1 feature data
        swSurfExtrudeFeature.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

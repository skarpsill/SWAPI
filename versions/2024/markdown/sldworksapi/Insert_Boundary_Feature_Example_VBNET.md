---
title: "Insert Boundary Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Boundary_Feature_Example_VBNET.htm"
---

# Insert Boundary Feature Example (VB.NET)

This example shows how to insert and modify a boundary feature.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates two boss-extrude features.
' 3. Selects a face on each boss-extrude feature.
' 4. Creates a boundary feature using the the selected faces.
' 5. Gets and sets some boundary feature data.
' 6. Examine the Immediate window, FeatureManager design tree,
'    and the graphics area.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swSketchMgr As SketchManager
        Dim swBoundaryBossFeatureData As BoundaryBossFeatureData
        Dim status As Boolean
        Dim sketchLines As Object
        Dim nbrCurves As Integer
        Dim directionVectorEntity As Object
        Dim directionVectorEntityType As Integer
        Dim tangencyType As Integer
        Dim d1Curves() As Object
        Dim curveType As Integer
        Dim i As Integer

        'Open new part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Create two boss-extrude features
        'and boundary feature
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        swSketchMgr = swModel.SketchManager
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.107624731933299, 0.0371047716348016, 0, -0.083196263303762, -0.00987284730888405, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.0508, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.0391822613366912, 0.0227443468893966, 0, 0.0479123594660678, -0.0893283426445919, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.0508, 0.0508, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0831962633037051, -0.000743092842242277, 0.0342529447572133, False, 8193, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0391822613366344, -0.00670639010576224, 0.0375699693011029, True, 16385, Nothing, 0)
        swFeatureMgr.SetNetBlendCurveData(0, 0, 0, 0, 1, True)
        swFeatureMgr.SetNetBlendCurveData(0, 1, 0, 0.26179938779915, 1, True)
        swFeatureMgr.SetNetBlendDirectionData(0, 32, 0, False, False)
        swFeatureMgr.SetNetBlendDirectionData(1, 32, 0, False, False)
        swFeatureMgr.InsertNetBlend(1, 2, 0, False, 0.0001, True, True, True, True, False, -1, -1, False, -1, False, False, -1, False, -1, True)

        'Get boundary feature
        'Get and set some of its data
        status = swModelDocExt.SelectByID2("Boundary1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swBoundaryBossFeatureData = swFeature.GetDefinition
        Debug.Print("Name of feature: " & swFeature.Name)
        swModel.ClearSelection2(True)
        status = swBoundaryBossFeatureData.AccessSelections(swModel, Nothing)
        'Get number of curves
        nbrCurves = swBoundaryBossFeatureData.GetCurvesCount(swBoundaryBossDirection_e.swBoundaryBossDirection_First)
        Debug.Print("  Number of curves in Direction 1: " & nbrCurves)
        If nbrCurves >= 0 Then
            'Get tangency type
            tangencyType = swBoundaryBossFeatureData.GetGuideTangencyType(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0)
            If tangencyType = swBoundaryBossTangencyType_e.swBoundaryBossTangency_DirectionVector Then
                directionVectorEntity = swBoundaryBossFeatureData.GetDirectionVector(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0)
                status = swSelectionMgr.AddSelectionListObject(directionVectorEntity, Nothing)
                directionVectorEntityType = swSelectionMgr.GetSelectedObjectType3(1, -1)
                Debug.Print("  Type of entity selected for Direction Vector for curve 1 in Direction 1: " & directionVectorEntityType)
            Else
                Debug.Print("  Tangency type for curve 1 in Direction 1: " & tangencyType)
                Debug.Print("    NOTE: Tried to get entity for Direction Vector. Failed because")
                Debug.Print("    tangency type must be 2 (swBoundaryBossTangencyType_e.swBoundaryBossTangency_DirectionVector),")
                Debug.Print("    so type of entity used for Direction Vector is not available.")
            End If
        End If
        'Get and set draft angle
        Debug.Print("  Original draft angle for curve 1 in Direction 1: " & swBoundaryBossFeatureData.GetDraftAngle(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0))
        swBoundaryBossFeatureData.SetDraftAngle(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0, 0.015)
        Debug.Print("  Modified draft angle for curve 1 in Direction 1: " & swBoundaryBossFeatureData.GetDraftAngle(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0))
        'Flip draft angle
        swBoundaryBossFeatureData.SetDraftAngleReverseDirection(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0, True)
        Debug.Print("  Draft angle flipped for curve 1 in Direction 1: " & swBoundaryBossFeatureData.GetDraftAngleReverseDirection(swBoundaryBossDirection_e.swBoundaryBossDirection_First, 0))
        'Get curves
        swModel.ClearSelection2(True)
        d1Curves = swBoundaryBossFeatureData.D1Curves
        For i = 0 To nbrCurves - 1
            status = swSelectionMgr.AddSelectionListObject(d1Curves(i), Nothing)
            curveType = swSelectionMgr.GetSelectedObjectType3(i + 1, -1)
            Debug.Print("  Curve " & i + 1 & " type: " & curveType)
        Next i
        Debug.Print("  Is thin feature? " & swBoundaryBossFeatureData.IsThinFeature)
        status = swFeature.ModifyDefinition(swBoundaryBossFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Insert Fill-surface Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Fill-surface_Feature_Example_VBNET.htm"
---

# Insert Fill-surface Feature Example (VB.NET)

This example shows how to insert a fill-surface feature.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sketches a circle on the Front Plane.
' 2. Offsets the Front Plane to create Plane1.
' 3. Sketches a circle on Plane1.
' 4. Creates a thin-feature loft using the circles
'    created in steps 1 and 3.
' 5. Selects one of the sketches to use for
'    the fill-surface feature.
' 6. Creates a fill-surface feature named Surface-Fill1.
' 7. Gets, sets, and prints some properties of the fill-surface feature
'    to the Immediate window.
' 8. Examine the FeatureManager design, graphics area, and the
'    the Immediate window.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatMgr As FeatureManager
        Dim swRefPlane As RefPlane
        Dim swFeat As Feature
        Dim swFillSurfaceFeatureData As FillSurfaceFeatureData
        Dim selObj As Object
        Dim status As Boolean
        Dim nbrPatchEntities As Integer
        Dim patchEntities() As Object
        Dim entTypes As Object = Nothing
        Dim i As Integer

        'Open a new model document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\part.prtdot", swDwgPaperSizes_e.swDwgPaperAsize, 0, 0)

        'Select the front plane and sketch a circle
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swModel.ClearSelection2(True)
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.018863, -0.048015, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Offset the front plane to create Plane1
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatMgr = swModel.FeatureManager
        swRefPlane = swFeatMgr.InsertRefPlane(8, 0.0762, 0, 0, 0, 0)
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.005144, -0.017148, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Create a loft as a thin feature
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0120997659765269, 0.0131954647737917, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -0.0137458916138411, 0.0497220981864567, 0, True, 1, Nothing, 0)
        swFeatMgr.InsertProtrusionBlend2(False, True, False, 1, 0, 0, 1, 1, True, True, True, 0.000254, 0.000254, 0, True, True, True, swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge)

        'Get the sketch for the fill-surface feature
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0309259362651374, -0.0150632202505945, 0.0265529245975468, True, 257, Nothing, swSelectOption_e.swSelectOptionDefault)
        swSelMgr = swModel.SelectionManager
        selObj = swSelMgr.GetSelectedObject6(1, 257)
        'Insert the fill-surface feature
        swFeat = swFeatMgr.InsertFillSurface2(2, swFeatureFillSurfaceOptions_e.swOptimizeSurface, selObj, swContactType_e.swContact, Nothing, Nothing)

        'Access the fill-surface feature
        swFillSurfaceFeatureData = swFeat.GetDefinition
        status = swFillSurfaceFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Fill-surface feature: ")
        Debug.Print("  Number of constraint curves: " & swFillSurfaceFeatureData.GetConstraintCurvesCount)
        nbrPatchEntities = swFillSurfaceFeatureData.GetPatchBoundaryCount
        Debug.Print("  Number of entities used to define the patch boundary: " & nbrPatchEntities)
        If nbrPatchEntities > 0 Then
            'Get the type of patch boundary entities
            patchEntities = swFillSurfaceFeatureData.GetPatchBoundary(entTypes)
            For i = 0 To nbrPatchEntities - 1
                Debug.Print("  Type of entity for patch boundary " & (i + 1) & " (1 = edge; 9 = sketch) : " & entTypes(i))
            Next i
            Debug.Print("  Results merged? " & swFillSurfaceFeatureData.Merge)
            swFillSurfaceFeatureData.OptimizeSurface = False
            Debug.Print("  Patch optimized? " & swFillSurfaceFeatureData.OptimizeSurface)
            Debug.Print("  Original resolution control: " & swFillSurfaceFeatureData.ResolutionControl)
            If swFillSurfaceFeatureData.OptimizeSurface = False Then
                swFillSurfaceFeatureData.ResolutionControl = 1
            End If
            Debug.Print("  Updated resolution control (valid values 1, 2 and 3; setting this value only valid if patch is not optimized): " & swFillSurfaceFeatureData.ResolutionControl)
        End If
        status = swFeat.ModifyDefinition(swFillSurfaceFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

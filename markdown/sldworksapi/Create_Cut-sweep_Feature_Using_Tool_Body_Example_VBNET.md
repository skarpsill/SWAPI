---
title: "Create Cut-sweep Feature Using Tool Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Tool_Body_Example_VBNET.htm"
---

# Create Cut-sweep Feature Using Tool Body Example (VB.NET)

This example shows how to create a cut-sweep feature using a tool body.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a boss-extrude feature.
' 2. Creates a sketch.
' 3. Creates a revolve feature.
' 4. Selects the revolve feature, sketch, and extrude feature and
'    creates a cut-sweep feature.
' 5. Accesses the cut-sweep feature.
' 6. Gets the names of the cut-sweep feature's tool body and path.
' 7. Releases access of the cut-sweep feature.
' 8. Examine the Immediate window, FeatureManager design tree,
'    and graphics area.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swFeatureMgr As FeatureManager
        Dim swSelectionMgr As SelectionMgr
        Dim swSweepFeatureData As SweepFeatureData
        Dim swProfileObj As Object
        Dim swProfileBody As Body2
        Dim swPathFeature As Feature
        Dim sketchLines As Object
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        'Create extrude feature
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateCircle(-0.000361, 0.001416, 0.0#, 0.024462, -0.045092, 0.0#)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, True, 0, 0, 0.09, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

        'Create sketch
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swSelectionMgr.EnableContourSelection = False
        swSketchSegment = swSketchMgr.CreateCircle(-0.000019, 0.00051, 0.0#, 0.026716, -0.0401, 0.0#)
        swSketchMgr.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Create revolve feature
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.0266210577384013, -0.0248555003438298, 0, -0.0378465609175683, -0.0475106067599669, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", -0.0264169576805983, -0.0449999999999998, 0.0293457016154969, False, 16, Nothing, 0)
        swFeature = swFeatureMgr.FeatureRevolve2(True, True, False, False, False, False, 0, 0, 6.2831853071796, 0, False, False, 0.01, 0.01, 0, 0, 0, False, True, True)
        swSelectionMgr.EnableContourSelection = False
        swModel.ClearSelection2(True)

        'Create cut-sweep feature
        status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Revolve1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 2048, Nothing, 0)
        swFeature = swFeatureMgr.InsertCutSwept5(False, True, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, False, 0, True, True, True, False, False, 0, 0)
        Debug.Print("Feature name = " & swFeature.Name)
        swSweepFeatureData = swFeature.GetDefinition

        ' Roll back to access selections
        status = swSweepFeatureData.AccessSelections(swModel, Nothing)
        swProfileObj = swSweepFeatureData.Profile
        swProfileBody = swProfileObj
        Debug.Print("  Tool body = " & swProfileBody.Name)
        swPathFeature = swSweepFeatureData.Path
        Debug.Print("  Path = " & swPathFeature.Name)

        ' Roll forward
        swSweepFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

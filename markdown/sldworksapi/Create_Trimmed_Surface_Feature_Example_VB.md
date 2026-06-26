---
title: "Create Trimmed Surface Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Trimmed_Surface_Feature_Example_VB.htm"
---

# Create Trimmed Surface Feature Example (VBA)

This example shows how to create a trimmed surface feature.

```vb
' ---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document with two intersecting surface extrude
 '    features.
 ' 2. Selects Surface-Extrude2 as the trim tool and sets the trimming options.
 ' 3. Trims Surface-Extrude1.
 ' 4. Creates Surface-Trim1 in the FeatureManager design tree.
 ' 5. Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSketchMgr As SldWorks.SketchManager
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSketchSegment As SldWorks.SketchSegment
 Dim swFeatureMgr As SldWorks.FeatureManager
 Dim surfTrimFeatData As SldWorks.SurfaceTrimFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim status As Boolean

Sub main()
    Set swApp = Application.SldWorks

    ' Create new model document
     Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set swSketchMgr = swModel.SketchManager
     Set swModelDocExt = swModel.Extension
     Set swFeatureMgr = swModel.FeatureManager
     Set swSelMgr = swModel.SelectionManager

    ' Create two intersecting surfaces
     status = swModelDocExt.SelectByID2("Right Plane", "Plane", 0, 0, 0, False, 0, Nothing, 0)
     swSketchMgr.InsertSketch True
     Set swSketchSegment = swSketchMgr.CreateLine(-0.068922, 0.023964, 0#, 0.042733, 0.005543, 0#)
     swModel.ClearSelection2 True
     status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
     swFeatureMgr.FeatureExtruRefSurface2 True, False, False, 0, 0, 0.06604, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, False, False, False
     swSelMgr.EnableContourSelection = False

    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
     swSketchMgr.InsertSketch True
     Set swSketchSegment = swSketchMgr.CreateLine(-0.041529, 0.023059, 0#, -0.052625, -0.081662, 0#)
     swModel.ClearSelection2 True
     status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
     swFeatureMgr.FeatureExtruRefSurface2 False, False, False, 0, 0, 0.0889, 0.06604, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, False, False, False
     swSelMgr.EnableContourSelection = False

    ' Set the trimming options
     status = swFeatureMgr.PreTrimSurface(False, True, False, False)

    ' Trim the surface
     status = swModelDocExt.SelectByID2("", "SURFACEBODY", 2.89416986472588E-02, 7.81827749557351E-03, 2.90635845400971E-02, True, 0, Nothing, 0)
     Set swFeat = swFeatureMgr.PostTrimSurface(True)

    swModel.ClearSelection2 True

    Set surfTrimFeatData = swFeat.GetDefinition

    surfTrimFeatData.AccessSelections swModel, Nothing

    Debug.Print swFeat.Name
     Debug.Print "  Number of pieces to keep: " & surfTrimFeatData.GetPiecesToKeepCount
     Debug.Print "  Surface trim feature type as defined in swSurfaceTrimType_e: " & surfTrimFeatData.GetType
     Debug.Print ""

    Dim varTrimTools As Variant
     Dim i As Long

    varTrimTools = surfTrimFeatData.TrimTools
     Debug.Print "Trim tools:"
     For i = 0 To surfTrimFeatData.GetTrimToolsCount - 1
         Debug.Print "  " & varTrimTools(i).Name
     Next

    surfTrimFeatData.ReleaseSelectionAccess
End Sub
```

---
title: "Create Trimmed Surface Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Trimmed_Surface_Feature_Example_VBNET.htm"
---

# Create Trimmed Surface Feature Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSketchMgr As SketchManager
     Dim swModelDocExt As ModelDocExtension
     Dim swSketchSegment As SketchSegment
     Dim swFeatureMgr As FeatureManager
     Dim surfTrimFeatData As SurfaceTrimFeatureData
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim status As Boolean

     Sub main()

         ' Create new model document
         swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         swSketchMgr = swModel.SketchManager
         swModelDocExt = swModel.Extension
         swFeatureMgr = swModel.FeatureManager
         swSelMgr = swModel.SelectionManager

         ' Create two intersecting surfaces
         status = swModelDocExt.SelectByID2("Right Plane", "Plane", 0, 0, 0, False, 0, Nothing, 0)
         swSketchMgr.InsertSketch(True)
         swSketchSegment = swSketchMgr.CreateLine(-0.068922, 0.023964, 0.0#, 0.042733, 0.005543, 0.0#)
         swModel.ClearSelection2(True)
         status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
         swFeatureMgr.FeatureExtruRefSurface2(True, False, False, 0, 0, 0.06604, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, False, False, False)
         swSelMgr.EnableContourSelection = False

         status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
         swSketchMgr.InsertSketch(True)
         swSketchSegment = swSketchMgr.CreateLine(-0.041529, 0.023059, 0.0#, -0.052625, -0.081662, 0.0#)
         swModel.ClearSelection2(True)
         status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
         swFeatureMgr.FeatureExtruRefSurface2(False, False, False, 0, 0, 0.0889, 0.06604, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, False, False, False)
         swSelMgr.EnableContourSelection = False

         ' Set the trimming options
         status = swFeatureMgr.PreTrimSurface(False, True, False, False)

         ' Trim the surface
         status = swModelDocExt.SelectByID2("", "SURFACEBODY", 0.0289416986472588, 0.00781827749557351, 0.0290635845400971, True, 0, Nothing, 0)
         swFeat = swFeatureMgr.PostTrimSurface(True)

         swModel.ClearSelection2(True)

         surfTrimFeatData = swFeat.GetDefinition

         surfTrimFeatData.AccessSelections(swModel, Nothing)

         Debug.Print(swFeat.Name)
         Debug.Print("  Number of pieces to keep: " & surfTrimFeatData.GetPiecesToKeepCount)
         Debug.Print("  Surface trim feature type as defined in swSurfaceTrimType_e: " & surfTrimFeatData.GetType)
         Debug.Print("")

         Dim varTrimTools As Object
         Dim i As Integer

         varTrimTools = surfTrimFeatData.TrimTools
         Debug.Print("Trim tools:")
         For i = 0 To surfTrimFeatData.GetTrimToolsCount - 1
             Debug.Print("  " & varTrimTools(i).Name)
         Next

         surfTrimFeatData.ReleaseSelectionAccess()

     End Sub

     Public swApp As SldWorks

 End Class
```

---
title: "Create Surface Knit Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Surface_Knit_Feature_Example_VBNET.htm"
---

# Create Surface Knit Feature Example (VB.NET)

This example shows how to create a surface knit feature.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates two surfaces.
' 3. Creates a surface knit feature using the two
'    selected surfaces.
' 4. Examine the graphics area, FeatureManager design
'    tree, and Immediate window.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swSketchManager As SketchManager
    Dim swSketchSegment As SketchSegment
    Dim swFeatureManager As FeatureManager
    Dim swSelectionManager As SelectionMgr
    Dim swFeature As Feature
    Dim swSurfaceKnitFeature As SurfaceKnitFeatureData
    Dim boolstatus As Boolean

    Public Sub main()

        'Open new part document and create two surfaces
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchManager = swModel.SketchManager
        swFeatureManager = swModel.FeatureManager
        swSelectionManager = swModel.SelectionManager
        boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchManager.CreateEllipse(-0.0415374666666667, 0, 0, 0.0534585333333333, 0, 0, -0.0415374666666667, 0.0208618666666667, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        swFeatureManager.FeatureExtruRefSurface2(True, False, False, 0, 0, 0.05, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, False, False, False)
        swSelectionManager.EnableContourSelection = False
        boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 1, Nothing, 0)
        boolstatus = swModel.InsertPlanarRefSurface()
        swModel.ClearSelection2(True)

        ' Select both surfaces and create surface knit feature
        boolstatus = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 1, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("Surface-Plane1", "SURFACEBODY", 0, 0, 0, True, 1, Nothing, 0)
        swFeature = swFeatureManager.InsertSewRefSurface(True, False, False, 0.0001, 0.0001)

        ' Get some surface knit feature data
        swSurfaceKnitFeature = swFeature.GetDefinition
        Debug.Print("Knit-surface feature: ")
        Debug.Print("  Knit tolerance: " & swSurfaceKnitFeature.KnitTolerance * 1000 & " mm")
        Debug.Print("  Maximum value for gap range: " & swSurfaceKnitFeature.MaxValueForGapRange * 1000 & " mm")
        Debug.Print("  Minimum value for gap range: " & swSurfaceKnitFeature.MinValueForGapRange * 1000 & " mm")
        Debug.Print("  Use gap filters? " & swSurfaceKnitFeature.UseGapFilters)
        Debug.Print("  Use merge entities? " & swSurfaceKnitFeature.UseMergeEntities)
        Debug.Print("  Try to form solid? " & swSurfaceKnitFeature.UseTryToFormSolid)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

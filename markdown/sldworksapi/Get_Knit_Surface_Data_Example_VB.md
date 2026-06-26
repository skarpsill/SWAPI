---
title: "Get Knit Surface Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Knit_Surface_Data_Example_VB.htm"
---

# Get Knit Surface Data Example (VBA)

This example shows how to get a knit surface's data.

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
' 3. Creates a knit surface feature using the two
'    selected surfaces.
' 4. Examine the graphics area, FeatureManager design
'    tree, and Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swSelData As SldWorks.SelectData
Dim swFeature As SldWorks.Feature
Dim swSurfaceKnitFeature As SldWorks.SurfaceKnitFeatureData
Dim vEnt As Variant
Dim swEnt As SldWorks.Entity
Dim swFace As SldWorks.Face2
Dim swSeedFace As SldWorks.Face2
Dim swSurf As SldWorks.Surface
Dim swSurfRadFeat As SldWorks.Feature
Dim i As Long
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open new part document and create two surfaces
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    Set swSketchManager = swModel.SketchManager
    Set swFeatureManager = swModel.FeatureManager
    Set swSelectionManager = swModel.SelectionManager
    Set swSelData = swSelectionManager.CreateSelectData
    boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchManager.CreateEllipse(-4.15374666666667E-02, 0, 0, 5.34585333333333E-02, 0, 0, -4.15374666666667E-02, 2.08618666666667E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    swFeatureManager.FeatureExtruRefSurface2 True, False, False, 0, 0, 0.05, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, False, False, False
    swSelectionManager.EnableContourSelection = False
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 1, Nothing, 0)
    boolstatus = swModel.InsertPlanarRefSurface()
    swModel.ClearSelection2 True
```

```
    ' Select both surfaces and create surface knit feature
    boolstatus = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 1, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Surface-Plane1", "SURFACEBODY", 0, 0, 0, True, 1, Nothing, 0)
    Set swFeature = swFeatureManager.InsertSewRefSurface(True, False, False, 0.0001, 0.0001)
```

```
    ' Get some surface knit feature data
    Set swSurfaceKnitFeature = swFeature.GetDefinition
```

```
    ' Roll back to get to geometric entities
    boolstatus = swSurfaceKnitFeature.AccessSelections(swModel, Nothing)

    Set swSeedFace = swSurfaceKnitFeature.SeedFace
    If Not swSeedFace Is Nothing Then
        swModel.ClearSelection2 True
        Set swEnt = swSeedFace
        Debug.Print "Seed entity type: " & swEnt.GetType
        boolstatus = swEnt.Select4(True, swSelData)
    End If
```

```
    ' Get knit surface data
    boolstatus = False
    swModel.ClearSelection2 True
    vEnt = swSurfaceKnitFeature.Entities
    For i = 0 To UBound(vEnt)
        Set swEnt = vEnt(i)
        Set swSurfRadFeat = vEnt(i)
        Debug.Print "Entity type (" & i & "): " & swEnt.GetType
        If swSelectType_e.swSelFACES = swEnt.GetType Then
            boolstatus = swEnt.Select4(True, swSelData):
        Else
            ' Although not a surface-radiate feature, you cannot select
            ' a surface-radiate feature through IEntity interface, so select
            ' through IFeature interface
            Debug.Print "  Feature type: " & swSurfRadFeat.GetTypeName
            boolstatus = swSurfRadFeat.Select2(True, 0)
        End If
    Next i
```

```
    ' Apply any changes
    boolstatus = swFeature.ModifyDefinition(swSurfaceKnitFeature, swModel, Nothing)
```

```
End Sub
```

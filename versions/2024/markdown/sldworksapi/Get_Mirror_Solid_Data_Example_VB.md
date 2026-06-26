---
title: "Get Mirror Solid Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Solid_Data_Example_VB.htm"
---

# Get Mirror Solid Feature Data Example (VBA)

This example shows how to get data for a mirror solid feature.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a plane and solid body.
' 3. Mirrors the solid body.
' 4. Gets the mirror solid feature and some of its data.
' 5. Prints to the Immediate window some mirror solid feature data.
' 6. Examine the Immediate window, FeatureManager design tree, and graphics
'    area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swMirrorSolidFeatureData As SldWorks.MirrorSolidFeatureData
Dim swBody As SldWorks.Body2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swSelData As SldWorks.SelectData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim i As Long
Dim bodies As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select plane and solid body
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Top", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Top", "PLANE", 0, 0, 0, False, 2, Nothing, 0)
    status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 256, Nothing, 0)
```

```
    'Insert mirror solid feature
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.InsertMirrorFeature2(True, False, False, False, swFeatureScope_e.swFeatureScope_AllBodies)
```

```
    'Get mirror solid feature and some of its data
    Set swMirrorSolidFeatureData = swFeature.GetDefinition
    Debug.Print "  " & swFeature.Name
    Debug.Print "    Number of bodies               = " & swMirrorSolidFeatureData.GetPatternBodyCount
    Debug.Print "    Merged bodies                  = " & swMirrorSolidFeatureData.Merge
    Debug.Print "    Knit surfaces                  = " & swMirrorSolidFeatureData.KnitSurface
```

```
    'Roll back to get to the bodies
    status = swMirrorSolidFeatureData.AccessSelections(swModel, Nothing)
```

```
    Set swSelectionMgr = swModel.SelectionManager
    Set swSelData = swSelectionMgr.CreateSelectData
```

```
    bodies = swMirrorSolidFeatureData.PatternBodyArray
    For i = 0 To UBound(bodies)
        Set swBody = bodies(i)
        status = swBody.Select(True, 0)
        Debug.Print "    Body " & i + 1 & "'s type (solid body = 0) = " & swBody.GetType
    Next i
```

```
    'Release selection access
     swMirrorSolidFeatureData.ReleaseSelectionAccess
```

```
End Sub
```

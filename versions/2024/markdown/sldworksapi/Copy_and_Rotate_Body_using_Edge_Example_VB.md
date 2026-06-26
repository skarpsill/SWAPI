---
title: "Copy and Rotate Body Using Edge Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Rotate_Body_using_Edge_Example_VB.htm"
---

# Copy and Rotate Body Using Edge Example (VBA)

This example shows how to copy and rotate a body using an edge.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a solid body and two vertices.
' 3. Inserts a move/copy body feature.
' 4. Selects an edge.
' 5. Rotates the move/copy body about the selected edge.
' 6. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swMoveCopyBodyFeatureData As SldWorks.MoveCopyBodyFeatureData
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swEdge As Edge
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
```

```
    'Select solid body and vertices for move/copy body feature
    status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, True, 8, Nothing, 0)
```

```
    'Insert move/copy body feature
    Set swFeature = swFeatureManager.InsertMoveCopyBody2(0, 0, 0, 0, -0.085, 0, 0.065, 0, 0, 0, True, 1)
```

```
    'Roll forward the feature and get and set move/copy body feature data
    Set swMoveCopyBodyFeatureData = swFeature.GetDefinition
    status = swMoveCopyBodyFeatureData.AccessSelections(swModel, Nothing)
```

```
    'Rotate body about the selected edge
    swMoveCopyBodyFeatureData.TransformType = swMoveCopyBodyFeatureTransformType_e.swTransformType_Rotation
    status = swModelDocExt.SelectByID2("", "EDGE", -8.53353899645981E-02, -1.26994939741394E-02, 6.53641069000059E-02, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swEdge = swSelectionMgr.GetSelectedObject6(1, -1)
    swMoveCopyBodyFeatureData.TransformReferenceEntity = swEdge
    swMoveCopyBodyFeatureData.TransformX = 0.09
```

```
    'Roll back
    status = swFeature.ModifyDefinition(swMoveCopyBodyFeatureData, swModel, Nothing)
    swMoveCopyBodyFeatureData.ReleaseSelectionAccess
```

```
End Sub
```

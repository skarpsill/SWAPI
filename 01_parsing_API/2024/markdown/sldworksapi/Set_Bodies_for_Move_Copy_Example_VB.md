---
title: "Set Bodies for Move/Copy Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Bodies_for_Move_Copy_Example_VB.htm"
---

# Set Bodies for Move/Copy Example (VBA)

This example shows how to set a body for a move/copy.

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
' 4. Sets the body to move, copy, or rotate.
' 5. Examine the FeatureManager design tree, the graphics area, and
'    the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swMoveCopyBodyFeatureData As SldWorks.MoveCopyBodyFeatureData
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim bodyArr(0) As Object
Dim aBody As SldWorks.Body2
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
    Set swSelectionMgr = swModel.SelectionManager
    Set swPart = swModel
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
    Set swFeature = swPart.FeatureByName("Body-Move/Copy1")
```

```
    'Roll forward the feature and get and set move/copy body feature data
    Set swMoveCopyBodyFeatureData = swFeature.GetDefinition
    status = swMoveCopyBodyFeatureData.AccessSelections(swModel, Nothing)
```

```
    'Get the body to set
    status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set bodyArr(0) = swSelectionMgr.GetSelectedObject6(1, -1)
    swModel.ClearSelection2 True
    swMoveCopyBodyFeatureData.bodies = bodyArr(0)
    If IsEmpty(bodyArr) Then
        Debug.Print "Body not set."
    Else
        Debug.Print "Body set."
        aBody = bodyArr(0)
        Debug.Print "Name of body set: " & aBody.Name
    End If
```

```
    'Roll back the feature
    swMoveCopyBodyFeatureData.ReleaseSelectionAccess
```

```
    swModel.ViewZoomtofit2
```

```
End Sub
```

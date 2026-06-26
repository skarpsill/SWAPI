---
title: "Change Number of Copies for Move/Copy Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Number_of_Copies_for_Move_Copy_Example_VB.htm"
---

# Change Number of Copies for Move/Copy Example (VBA)

This example shows how to change the number of copies for a move/copy.

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
' 4. Modifies the move/copy body (increases number of copies
'    from 1 to 4)
' 5. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
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
Dim copyStatus As Boolean
Dim number As Long
```

```
Sub main()

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
    copyStatus = swMoveCopyBodyFeatureData.Copy
    Debug.Print "Can copy? " & copyStatus
    number = swMoveCopyBodyFeatureData.NumberOfCopies
    Debug.Print "Number of copies of move/copy body before copy: " & number
    If number < 4 Then
        swMoveCopyBodyFeatureData.NumberOfCopies = 4
    End If
    number = swMoveCopyBodyFeatureData.NumberOfCopies
    Debug.Print "Number of copies of move/copy body after copy: " & number
```

```
    'Roll back
    status = swFeature.ModifyDefinition(swMoveCopyBodyFeatureData, swModel, Nothing)
    swMoveCopyBodyFeatureData.ReleaseSelectionAccess
```

```
    swModel.ViewZoomtofit2
```

```
End Sub
```

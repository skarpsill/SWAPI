---
title: "Get and Set Parting Line Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm"
---

# Get and Set Parting Line Feature Data Example (VBA)

This example shows how to get and set parting line feature data.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains a parting line feature.
' 2. Select the parting line feature in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets parting line feature data.
' 2. Examine the Immediate window.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swPartingLineFeatureData As SldWorks.PartingLineFeatureData
Dim state As Boolean

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Get parting line feature
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swPartingLineFeatureData = swFeature.GetDefinition
```

```
    'Roll back to get and set parting line feature data
    state = swPartingLineFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print " Feature name: " & swFeature.Name
    Debug.Print "    Parting line status as defined by swPartingLineFeatureStatus_e: " & swPartingLineFeatureData.status
    Debug.Print "    Draft angle: " & swPartingLineFeatureData.Angle
```

```
    'Reverse pull direction of part line
    Debug.Print "    Pull direction before reversing: " & swPartingLineFeatureData.PullDirection
    If swPartingLineFeatureData.PullDirection Then
        swPartingLineFeatureData.PullDirection = False
    Else
        swPartingLineFeatureData.PullDirection = True
    End If
    Debug.Print "    Pull direction after reversing: " & swPartingLineFeatureData.PullDirection
```

```
    Debug.Print "    Pull direction type as defined by swSelectType_e: " & swPartingLineFeatureData.PullDirectionType
    Debug.Print "    Split faces: " & swPartingLineFeatureData.SplitFaces
    If swPartingLineFeatureData.SplitFaces Then
        Debug.Print "    Split faces options as defined by swSplitFacesOption_e: " & swPartingLineFeatureData.SplitFacesOption
    End If
    Debug.Print "    Core/cavity split: " & swPartingLineFeatureData.CoreCavitySplit
    Debug.Print "    Number of entities to split: " & swPartingLineFeatureData.GetEntitiesToSplitCount
```

```
    'Modify and roll forward parting line feature
    swFeature.ModifyDefinition swPartingLineFeatureData, swModel, Nothing
```

```
End Sub
```

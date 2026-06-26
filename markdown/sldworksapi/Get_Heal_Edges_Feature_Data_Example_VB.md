---
title: "Get Heal Edges Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Heal_Edges_Feature_Data_Example_VB.htm"
---

# Get Heal Edges Feature Data Example (VBA)

This example shows how to get some data of a heal edges feature.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a HealEdge1 feature.
' 2. Select the HealEdge1 feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets HealEdge1 feature data.
' 2. Examine the Immediate window.
'----------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swHealEdgesFeature As SldWorks.HealEdgesFeatureData
Dim swFeature As SldWorks.Feature
Dim before As Long
Dim after As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Get and print HealEdge1 feature data
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, 0)
    Set swHealEdgesFeature = swFeature.GetDefinition
    swModel.ClearSelection2 True
    swHealEdgesFeature.AccessSelections swModel, Nothing
    Debug.Print "Number of faces in this heal edges feature: " & swHealEdgesFeature.GetFacesCount
    Debug.Print "Number of edges before and after healing: "
    swHealEdgesFeature.GetEdgeInformation before, after
    Debug.Print "  Before: " & before
    Debug.Print "  After : " & after
    Debug.Print " Maximum angle betweeen the merged edges: " & swHealEdgesFeature.AngularTolerance
    Debug.Print " Maximum length of the merged edges: " & swHealEdgesFeature.EdgeLengthTolerance
    swHealEdgesFeature.ReleaseSelectionAccess
```

```
End Sub
```

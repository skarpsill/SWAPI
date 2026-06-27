---
title: "Update FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_FeatureManager_Design_Tree_Example_VB.htm"
---

# Update FeatureManager Design Tree Example (VBA)

This example shows how to update the FeatureManager design tree.

```
'------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a feature.
'
' Postconditions:
' 1. Adds a comment to the selected feature.
' 2. At Stop, examine the FeatureManager design tree
'    to verify that a Comments folder is not shown in
'    the FeatureManager design tree, then press F5.
' 3. Updates the FeatureManager design tree.
' 4. Examine the FeatureManager design tree
'    again to verify that the Comments folder
'    is shown in the FeatureManager design tree.
'------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swFeature As SldWorks.Feature
    Dim swSelectionMgr As SldWorks.SelectionMgr
    Dim swComment As SldWorks.Comment
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swComment = swFeature.AddComment("Comment for feature")
```

```
    Stop
    'Examine the FeatureManager design tree
    'to verify that a Comments folder is not shown in
    'the FeatureManager design tree, then press F5
```

```
    Set swFeatMgr = swModel.FeatureManager
    swFeatMgr.UpdateFeatureTree
```

```
End Sub
```

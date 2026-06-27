---
title: "Create Thicken Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Thicken_Feature_Example_VB.htm"
---

# Create Thicken Feature Example (VBA)

This example shows how to create a thicken feature in a multibody part.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates an offset plane and offset surface.
' 2. Selects a face on one body and the offset surface.
' 3. Creates a thicken feature.
' 4. Accesses the thicken feature and gets some property values.
' 5. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swRefPlane As SldWorks.RefPlane
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swPlane As SldWorks.RefPlane
Dim swFeatureThicken As SldWorks.Feature
Dim swFeatureThicken_DEF As SldWorks.ThickenFeatureData
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Create offset surface
    status = swModelDocExt.SelectByID2("Top", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swRefPlane = swFeatureMgr.InsertRefPlane(264, 0.01, 0, 0, 0, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "FACE", 2.35573770133328E-02, 0, -2.4476412300487E-03, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -5.61529049190312E-02, 0, -2.56278005667809E-03, True, 0, Nothing, 0)
    swModel.InsertOffsetSurface 0.01, False
```

```
    swModel.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Surface-Offset1[1]", "SURFACEBODY", 3.19724221122328E-02, -9.99999999999091E-03, -1.04277742429417E-02, False, 1, Nothing, 0)
```

```
    ' Thicken the selected reference surface and then generate a boss
    Set swFeatureThicken = swFeatureMgr.FeatureBossThicken(0.01, 0, 96, False, True, False, True)
```

```
    swModel.ClearSelection2 True
```

```
    ' Set the property values for the selected feature
    swModel.SelectedFeatureProperties 0, 0, 0, 0, 0, 0, 0, 1, 0, "Thicken1"
```

```
    ' Get the thicken feature definition object
    Set swFeatureThicken_DEF = swFeatureThicken.GetDefinition
    swFeatureThicken_DEF.AccessSelections swModel, Nothing
```

```
    ' Display whether a boss feature
    Debug.Print "Boss feature? " & swFeatureThicken_DEF.IsBossFeature
```

```
    ' Display whether the results of this thicken feature are merged
    Debug.Print "Merged? " & swFeatureThicken_DEF.Merge
```

```
    ' Display whether all or only specific bodies were
    ' automatically selected for the thicken feature
    Debug.Print "All bodies automatically selected? " & swFeatureThicken_DEF.AutoSelect
```

```
    swFeatureThicken_DEF.ReleaseSelectionAccess
```

```
End Sub
```

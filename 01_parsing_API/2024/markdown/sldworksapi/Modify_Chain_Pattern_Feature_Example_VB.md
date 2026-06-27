---
title: "Modify Chain Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Chain_Pattern_Feature_Example_VB.htm"
---

# Modify Chain Pattern Feature Example (VBA)

This example shows how to modify a chain pattern feature.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Verify that these files exist in public_documents\samples\tutorial\api:
'    * cam roller.sldprt
'    * distance linkage.sldasm
'    * mount base.sldasm
'    * mount plate.sldprt
' 2. Open distance linkage.sldasm.
'    a. Click Insert > Component Pattern > Chain Pattern.
'       1. Click Distance Linkage in Pitch Method.
'       2. Click Belt Drive Path in the FeatureManager design tree
'          for Path.
'       3. Set Number of Instances to 4.
'       4. Click Mount Base<1> in the FeatureManager design tree
'          for Component to Pattern.
'       5. Set Spacing to approximately 10.
'       6. Click the cylindrical face on Cam Roller<3> (left-front cam)
'          in the graphics area for Path Link1. Zoom in if necessary.
'       7. Click the cylindrical face on Cam Roller<1> (right-front cam)
'          in the graphics area for Path Link2.
'       8. Expand Mount Base<1> and click its Right Plane in the
'          FeatureManager design tree for Path Alignment Plane.
'    b. Click OK to create ChainPattern1 feature.
'    c. Click Zoom to Fit.
' 3. Examine the FeatureManager design tree and graphics area.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Selects the ChainPattern1 feature.
' 2. Gets and sets some ChainPattern1 data.
' 3. Click Zoom to fit.
' 4. Examine the Immediate window and graphics area.
'
' NOTE: Because these models are used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swChainPatternFeatureData As SldWorks.ChainPatternFeatureData
Dim swModelView As SldWorks.ModelView
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelView = swModel.ActiveView
```

```
    'Get ChainPattern1 feature
    'Get and set some of its data
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("ChainPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swChainPatternFeatureData = swFeature.GetDefinition
    status = swChainPatternFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print "Name of feature: " & swFeature.Name
    'Get pitch type
    Debug.Print "  Pitch type: " & swChainPatternFeatureData.PitchMethod
    'Get align method
    Debug.Print "  Align method: " & swChainPatternFeatureData.AlignMethod
    'Get whether Fill Path selected
    Debug.Print "  Original Fill Path: " & swChainPatternFeatureData.FillPath
    'Get number of pattern instances and spacing
    Debug.Print "  Original number of instances: " & swChainPatternFeatureData.InstanceCount
    Debug.Print "  Original distance between each pattern instance: " & swChainPatternFeatureData.Spacing
    'Set Fill Path to true
    swChainPatternFeatureData.FillPath = True
    Debug.Print "  Modified Fill Path: " & swChainPatternFeatureData.FillPath
    'Change spacing
    swChainPatternFeatureData.Spacing = 0.2
    Debug.Print "  Modified distance between each pattern instance: " & swChainPatternFeatureData.Spacing
```

```
    swFeature.ModifyDefinition swChainPatternFeatureData, swModel, Nothing
```

```
End Sub
```

---
title: "Get Imported Curve Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Imported_Curve_Feature_Data_Example_VB.htm"
---

# Get Imported Curve Feature Data Example (VBA)

This example shows how to get the number of curves in an imported curve feature.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open a part document that has an ImportedCurve1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the ImportedCurve1 feature.
' 2. Gets the number of curves in ImportedCurve1.
' 3. Examine the Immediate window.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swImportedCurveFeatureData As SldWorks.ImportedCurveFeatureData
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Select ImportedCurve1 and get the number of curves in the feature
    status = swModelDocExt.SelectByID2("ImportedCurve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swImportedCurveFeatureData = swFeature.GetDefinition
    Debug.Print "Number of curves: " & swImportedCurveFeatureData.GetCurveCount
```

```
End Sub
```

---
title: "Get Feature Type and Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Feature_Type_and_Name_Example_VB.htm"
---

# Get Feature Type and Name Example (VBA)

This example shows how to get the feature type and name of the selected feature for use with IModelDocExtension::SelectByID2.

```
'----------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Expand any component in the FeatureManager design tree
'    and select one of its features.
'
' Postconditions:
' 1. Gets the selected feature's type and name.
' 2. Examine the Immediate window.
'
' NOTE: Because this assembly document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim featName As String, featType As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    ' Get the selected feature
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
```

```
    swModel.ClearSelection2 True
```

```
    ' Get the feature's type and name
    featName = swFeat.GetNameForSelection(featType)
    swModelDocExt.SelectByID2 featName, featType, 0, 0, 0, True, 0, Nothing, 0
```

```
    ' Print the feature's type and name
    ' to the Immediate window
    Debug.Print "Feature type: " & featType
    Debug.Print "Feature name: " & featName
```

```
End Sub
```

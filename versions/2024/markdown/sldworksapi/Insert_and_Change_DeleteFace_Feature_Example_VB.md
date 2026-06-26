---
title: "Insert and Change DeleteFace Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Change_DeleteFace_Feature_Example_VB.htm"
---

# Insert and Change DeleteFace Feature Example (VBA)

This example shows how to insert a DeleteFace feature and how to modify that feature.

```
' ---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates and modifies a DeleteFace feature.
' 2. Examine the FeatureManager design tree, the graphics
'    area, and the Immediate window.
'
' NOTE: Because this part document is used elsewhere, do not save changes.
' --------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swDeleteFaceFeature As SldWorks.DeleteFaceFeatureData
Dim featureName As String
Dim boolstatus As Boolean
Dim opt As Long
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
' Select a face for the DeleteFace
' feature
boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.002251015125069, -0.001872569429423, 0.02015405789763, False, 0, Nothing, 0)
```

```
' Insert a DeleteFace feature
boolstatus = swModelDocExt.InsertDeleteFace(swFaceDelete_Default)
```

```
' Get the DeleteFace feature
Set swFeature = swModel.FirstFeature
```

```
While Not swFeature Is Nothing
 featureName = swFeature.Name
 While featureName <> "DeleteFace1"
    Set swFeature = swFeature.GetNextFeature
    featureName = swFeature.Name
 Wend
    Debug.Print "Feature name: " & featureName
    Set swDeleteFaceFeature = swFeature.GetDefinition
     boolstatus = swDeleteFaceFeature.AccessSelections(swModel, Nothing)
    Debug.Print "  Number of deleted faces: " & swDeleteFaceFeature.GetDeletedFacesCount
```

```
    ' Get the DeleteFace feature's option
    opt = swDeleteFaceFeature.options
    Debug.Print "  Before changing the option..."
    DeleteFaceOptions opt
```

```
    ' Change the DeleteFace feature's option
    swDeleteFaceFeature.options = swFaceDelete_Patch
    opt = swDeleteFaceFeature.options
    Debug.Print "  After changing the option..."
    DeleteFaceOptions opt
```

```
    ' Save modification made to DeleteFace feature
    boolstatus = swFeature.ModifyDefinition(swDeleteFaceFeature, swModel, Nothing)
```

```
    ' Get next feature until no more features
    Set swFeature = swFeature.GetNextFeature
Wend
```

```
End Sub
```

```
Sub DeleteFaceOptions(options As Long)
    Select Case options
        Case 0
            Debug.Print "    Option = swFaceDelete_Default"
        Case 1
            Debug.Print "    Option = swFaceDelete_Patch"
        Case 2
            Debug.Print "    Option = swFaceDelete_Fill"
        Case 3
            Debug.Print "    Option = swFaceDelete_FillWithTangent"
    End Select
End Sub
```

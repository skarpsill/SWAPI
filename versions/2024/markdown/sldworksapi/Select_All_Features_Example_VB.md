---
title: "Select All Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Features_Example_VB.htm"
---

# Select All Features Example (VBA)

This example shows how to select all of the features in a part.

```
'------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects all selectable features.
' 2. Examine the FeatureManager design tree, graphics
'    area, and Immediate window.
'
' NOTE: Some features are not selectable.
'------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swFeatMgr                   As SldWorks.FeatureManager
    Dim swFeat                      As SldWorks.Feature
    Dim swSubFeat                   As SldWorks.Feature
    Dim swSubSubFeat                As SldWorks.Feature
    Dim swSubSubSubFeat             As SldWorks.Feature
    Dim i                           As Long
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
```

```
    ' Disable FeatureManager design tree to increase performance
    swFeatMgr.EnableFeatureTree = False
```

```
    swModel.ClearSelection2 True
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Set swFeat = swModel.FirstFeature
    Do While Not swFeat Is Nothing
        bRet = swFeat.Select2(True, 0)
        Debug.Print "  " & swFeat.Name & " [" & swFeat.GetTypeName & "]"
        Set swSubFeat = swFeat.GetFirstSubFeature
        Do While Not swSubFeat Is Nothing
            bRet = swSubFeat.Select2(True, 0)
            Debug.Print "    " & swSubFeat.Name & " [" & swSubFeat.GetTypeName & "]"
            Set swSubSubFeat = swSubFeat.GetFirstSubFeature
            Do While Not swSubSubFeat Is Nothing
                bRet = swSubSubFeat.Select2(True, 0)
                Debug.Print "      " & swSubSubFeat.Name & " [" & swSubSubFeat.GetTypeName & "]"
                Set swSubSubSubFeat = swSubFeat.GetFirstSubFeature
                Do While Not swSubSubSubFeat Is Nothing
                    bRet = swSubSubSubFeat.Select2(True, 0)
                    Debug.Print "        " & swSubSubSubFeat.Name & " [" & swSubSubSubFeat.GetTypeName & "]"
                    Set swSubSubSubFeat = swSubSubSubFeat.GetNextSubFeature
                Loop
                Set swSubSubFeat = swSubSubFeat.GetNextSubFeature
            Loop
            Set swSubFeat = swSubFeat.GetNextSubFeature
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    'bRet = swModel.DeleteSelection(False)
```

```
    ' Re-enable FeatureManager design tree to show new selections
    swFeatMgr.EnableFeatureTree = True
```

```
End Sub
```

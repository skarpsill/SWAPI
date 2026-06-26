---
title: "Insert Scale Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Scale_Feature_Example_VB.htm"
---

# Insert Scale Feature Example (VBA)

This example shows how to insert a scale feature.

```
'------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions
' 1. Scales the part by a factor of 3.
' 2. Examine the Immediate window and graphics
'    area.
'-------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swScaleFeat As SldWorks.Feature
    Dim swScale As SldWorks.ScaleFeatureData
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    Set swFeatMgr = swModel.FeatureManager
    Set swScaleFeat = swFeatMgr.InsertScale(swScaleAboutOrigin, True, 3, 3, 3)
    If swScaleFeat Is Nothing Then Exit Sub
```

```
    Set swScale = swScaleFeat.GetDefinition
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Scale = " & swScaleFeat.Name
    Debug.Print "    Error (0 = no errors) = " & swScaleFeat.GetErrorCode
```

```
End Sub
```

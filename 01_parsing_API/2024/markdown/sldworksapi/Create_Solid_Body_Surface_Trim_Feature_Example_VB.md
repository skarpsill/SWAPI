---
title: "Create Solid Body Surface Trim Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm"
---

# Create Solid Body Surface Trim Feature Example (VBA)

This example shows how to create a solid body surface trim feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Creates Surface-Trim1.
' 3. Expand and examine Solid Bodies(1) in the FeatureManager design tree
'    and examine the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim status As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SurfaceTrimFeature.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
```

```
    ' Select surface features
    status = swModelDocExt.SelectByID2("", "SURFACEBODY", -4.46486526100784E-02, 2.18350174377093E-02, 1.23754341749418E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "SURFACEBODY", -8.15686270678384E-03, 4.15839719953865E-02, 2.42402652081068E-02, True, 0, Nothing, 0)
```

```
    ' Select trimming surfaces to create solid body surface trim feature
    status = swFeatureManager.PreTrimSurface(True, True, False, True)
    status = swModelDocExt.SelectByID2("", "SURFACEBODY", 5.9504253577245E-03, 4.13800871671199E-02, 2.48740287174201E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.037205042299604, 3.43527327176432E-02, 1.23446167727934E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "SURFACEBODY", -1.04497983190015E-02, -4.72172176775487E-02, 2.33436625590571E-02, True, 0, Nothing, 0)
    Debug.Print "Solid body surface trim feature? " & swFeatureManager.SolidForTrim
    swFeatureManager.SolidForTrim = True
    Debug.Print "Solid body surface trim feature? " & swFeatureManager.SolidForTrim
    Set swFeature = swFeatureManager.PostTrimSurface(True)
```

```
End Sub
```

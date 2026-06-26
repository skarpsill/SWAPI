---
title: "Modify Surface-cut Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Surface_Cut_Feature_Example_VB.htm"
---

# Modify Surface-cut Feature Example (VBA)

This example shows how to modify a surface-cut feature.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Flips the direction of the surface-cut feature.
' 2. Examine the the Immediate.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'-------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swSurfCutFeature As SldWorks.SurfCutFeatureData
Dim status As Boolean
Dim errors As Long, warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SurfCut.sldprt"
swApp.OpenDoc6 fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
```

```
' Get the surface-cut feature
status = swModelDocExt.SelectByID2("SurfaceCut1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
Set swSelMgr = swModel.SelectionManager
Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
Set swSurfCutFeature = swFeature.GetDefinition
status = swSurfCutFeature.AccessSelections(swModel, Nothing)
```

```
' Flip direction of surface cut
swSurfCutFeature.Flip = True
Debug.Print ("Surface-cut feature flipped: " & status)
```

```
' Update definition of feature
swFeature.ModifyDefinition swSurfCutFeature, swModel, Nothing
```

```
' Rebuild part
swModel.EditRebuild3
```

```
End Sub
```

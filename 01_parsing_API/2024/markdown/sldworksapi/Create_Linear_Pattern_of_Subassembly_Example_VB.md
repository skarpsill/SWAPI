---
title: "Create Linear Pattern of Subassembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Pattern_of_Subassembly_Example_VB.htm"
---

# Create Linear Pattern of Subassembly Example (VBA)

This example shows how to create a linear pattern of a subassembly.

```
'--------------------------------------------------
' Preconditions: Verify that the assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects an edge for Direction 1.
' 3. Selects a subassembly to pattern.
' 4. Creates a linear pattern.
' 5. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because the assembly is used elsewhere, do
' not save changes.
'---------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\distance linkage.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
    status = swModelDocExt.SelectByID2("", "EDGE", 0.222723097227572, -0.193386735236572, -0.10172211746567, False, 2, Nothing, 0)
    status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
    Set swFeature = swFeatureManager.FeatureLinearPattern5(4, 0.254, 1, 0.05, False, False, "NULL", "NULL", False, False, False, False, False, False, True, True, False, False, 0, 0, False, False)
    swModel.ClearSelection2 True
    swModel.ViewZoomtofit2
```

```
End Sub
```

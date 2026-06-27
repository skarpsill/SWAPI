---
title: "Set Component State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Component_State_Example_VB.htm"
---

# Set Component State Example (VBA)

This example shows how to set the suppression state of the selected assembly components.

```
'-----------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select one or more components.
'
' Postconditions:
' 1. Sets the states of the selected components to
'    suppressed.
' 2. Examine the graphics area and FeatureManager
'    design tree.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim i As Long
    Dim nSelCount As Long
    Dim swCompArr() As SldWorks.Component2
    Dim vCompArr As Variant
    Dim sConfName As String
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConf = swConfigMgr.ActiveConfiguration
```

```
    sConfName = swConf.Name
```

```
    ReDim swCompArr(0)
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
    For i = 1 To nSelCount
        If Not swSelMgr.GetSelectedObjectsComponent2(i) Is Nothing Then
            Set swCompArr(i - 1) = swSelMgr.GetSelectedObjectsComponent4(i, -1)
            ReDim Preserve swCompArr(UBound(swCompArr) + 1)
        End If
    Next i
```

```
    Debug.Assert UBound(swCompArr) > 0
    ReDim Preserve swCompArr(UBound(swCompArr) - 1)
    vCompArr = swCompArr
```

```
    bRet = swAssy.SetComponentState(swComponentSuppressed, (vCompArr), swThisConfiguration, sConfName, False): Debug.Assert bRet
```

```
End Sub
```

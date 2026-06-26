---
title: "Rename Assembly Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Assembly_Components_Example_VB.htm"
---

# Rename Assembly Components Example (VBA)

This example shows how to rename assembly components.

```
'---------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Appends 123 to the end of each assembly component's
'    name.
' 2. Examine the FeatureManager design tree and the
'    Immediate window.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConfig As SldWorks.Configuration
    Dim swRootComp  As SldWorks.Component2
    Dim Children As Variant
    Dim swChild As SldWorks.Component2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim ChildCount As Long
    Dim OldName As String
    Dim NewName As String
    Dim bOldSetting As Boolean
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
```

```
    bOldSetting = swApp.GetUserPreferenceToggle(swExtRefUpdateCompNames)
```

```
    swApp.SetUserPreferenceToggle swExtRefUpdateCompNames, False
```

```
    Children = swRootComp.GetChildren
    ChildCount = UBound(Children)
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    For i = 0 To ChildCount
        Set swChild = Children(i)
        ' Changing component name requires component to be selected
        bRet = swChild.Select4(False, swSelData, False)
        OldName = swChild.Name2
        NewName = OldName & " 123"
        Debug.Print "Old name = " + OldName
        Debug.Print "New name = " + NewName
        Debug.Print ""
        swChild.Name2 = NewName
    Next i
```

```
    swApp.SetUserPreferenceToggle swExtRefUpdateCompNames, bOldSetting
```

```
End Sub
```

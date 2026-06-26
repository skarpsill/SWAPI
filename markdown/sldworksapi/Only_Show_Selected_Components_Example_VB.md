---
title: "Only Show Selected Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Only_Show_Selected_Components_Example_VB.htm"
---

# Only Show Selected Components Example (VBA)

This example shows how to only show the selected components in an assembly.

```
'----------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select one or more components.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Hides all components except the selected components.
' 2. Examine the Immediate window, graphics area, and the
'    FeatureManager design tree.
'
' NOTES:
' * If a subassembly is selected, then all child components
'   (parts and sub-subassemblies) are shown.
' * If a sub-subassembly is selected, all parents are recursively
'   shown at the top-level assembly.
'-----------------------------------------------------
Option Explicit
```

```
Function IsCompInSelList(swSelCompArr() As SldWorks.Component2, swComp As SldWorks.Component2) As Boolean
```

```
    Dim vSelCompArr As Variant
    Dim vSelComp As Variant
```

```
    vSelCompArr = swSelCompArr
    For Each vSelComp In vSelCompArr
        If vSelComp Is swComp Then
            IsCompInSelList = True
            Exit Function
        End If
    Next vSelComp
```

```
    IsCompInSelList = False
```

```
End Function
```

```
Sub ShowParentComp(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2)
```

```
    Dim swParentComp As SldWorks.Component2

    Set swParentComp = swComp.GetParent
    If Not swParentComp Is Nothing Then
        ' This is a component in a subassembly, so set
        ' subassembly to be visible because subassembly's visibility
        ' overrides component's visibility; that is, show parent
        swParentComp.Visible = swComponentVisible
        ' Show grandparent; that is, recurse up assembly tree
        ShowParentComp swApp, swModel, swParentComp
```

```
    End If
```

```
End Sub
```

```
Sub ShowComp(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2)
```

```
    Dim vChildArr As Variant
    Dim vChild As Variant
    Dim swChildComp As SldWorks.Component2
```

```
    ' Show this component
    swComp.Visible = swComponentVisible
```

```
    vChildArr = swComp.GetChildren
    For Each vChild In vChildArr
        Set swChildComp = vChild
        ' Show all children
        swChildComp.Visible = swComponentVisible
        ' Show all grandchildren; that is, recurse down assembly tree
        ShowComp swApp, swModel, swChildComp
    Next vChild
```

```
End Sub
```

```
Sub HideAllComp(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2)
```

```
    Dim vChildArr As Variant
    Dim vChild As Variant
    Dim swChildComp As SldWorks.Component2
```

```
    ' Hide this component
    swComp.Visible = swComponentHidden
```

```
    vChildArr = swComp.GetChildren
    For Each vChild In vChildArr
        Set swChildComp = vChild
        ' Hide each child component; that is, recurse down assembly tree
        HideAllComp swApp, swModel, swChildComp
    Next vChild
```

```
End Sub
```

```
Function GetSelCompList(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2) As SldWorks.Component2()
```

```
    Dim swSelCompArr() As SldWorks.Component2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim nSelCount As Long
    Dim i As Long
```

```
    ReDim swSelCompArr(0)
    Set swSelMgr = swModel.SelectionManager
    nSelCount = swSelMgr.GetSelectedObjectCount2(-1): Debug.Assert nSelCount >= 1
    For i = 1 To nSelCount
        Set swComp = swSelMgr.GetSelectedObjectsComponent4(i, -1)
        If Not swComp Is Nothing Then
            Set swSelCompArr(UBound(swSelCompArr)) = swComp
            ReDim Preserve swSelCompArr(UBound(swSelCompArr) + 1)
        End If
    Next i
```

```
    Debug.Assert UBound(swSelCompArr) > 0
    ReDim Preserve swSelCompArr(UBound(swSelCompArr) - 1)
```

```
    GetSelCompList = swSelCompArr
```

```
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDocExt As SldWorks.ModelDocExtension
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConfig As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim swSelCompArr() As SldWorks.Component2
    Dim vSelCompArr As Variant
    Dim vSelComp As Variant
    Dim swSelComp As SldWorks.Component2
    Dim nSelCount As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDocExt = swModel.Extension
    Set swFeatMgr = swModel.FeatureManager
    Set swAssy = swModel
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
```

```
    ' Temporarily disable FeatureManager design tree updates to increase performance
    swFeatMgr.EnableFeatureTree = False
```

```
    swSelCompArr = GetSelCompList(swApp, swModel)
    vSelCompArr = swSelCompArr
```

```
    HideAllComp swApp, swModel, swRootComp
```

```
    For Each vSelComp In vSelCompArr
        Set swSelComp = vSelComp
        ShowComp swApp, swModel, swSelComp
        ShowParentComp swApp, swModel, swSelComp
    Next vSelComp
```

```
    ' Restore selected components
    nSelCount = swDocExt.MultiSelect2(vSelCompArr, True, Nothing): Debug.Assert UBound(vSelCompArr) + 1 = nSelCount
```

```
    swFeatMgr.EnableFeatureTree = True
```

```
End Sub
```

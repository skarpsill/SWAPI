---
title: "Show All Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_All_Components_Example_VB.htm"
---

# Show All Components Example (VBA)

This example shows how to show all of the components in an assembly.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Hide one or more components (right-click the component
'    and click the Hide Components button)
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Shows all hidden components.
' 2. Examine the graphics area, FeatureManager design tree,
'    and the Immediate window.
'-----------------------------------------------------------
Option Explicit
```

```
Sub SetCompVisib(swComp As SldWorks.Component2)
```

```
    Dim vChildArray As Variant
    Dim swChildComp As SldWorks.Component2
    Dim i As Long
```

```
    ' Root component has no name; it is an empty string
    Debug.Print swComp.Name2 & "; [" & swComp.Visible & "] (0 hidden; 1 visible); # of children --> " & swComp.IGetChildrenCount
```

```
    swComp.Visible = swComponentVisible
```

```
    vChildArray = swComp.GetChildren
    For i = 0 To UBound(vChildArray)
        Set swChildComp = vChildArray(i)
        SetCompVisib swChildComp
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConfig  As SldWorks.Configuration
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swRootComp As SldWorks.Component2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
```

```
    SetCompVisib swRootComp
```

```
End Sub
```

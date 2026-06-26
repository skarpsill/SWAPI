---
title: "Get Component for Selected Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_for_Selected_Entity_Example_VB.htm"
---

# Get Component for Selected Entity Example (VBA)

This example shows how to get the component for the selected entity.

```
'--------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select an entity in the graphics area.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the component.
' 2. Examine the Immediate window.
'--------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEnt As SldWorks.Entity
    Dim swComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEnt = swSelMgr.GetSelectedObject6(1, -1)
    Set swComp = swEnt.GetComponent
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    If Not swComp Is Nothing Then
        Debug.Print "  " & swComp.Name2 & " --> " & swComp.GetPathName
    Else
        Debug.Print "  Could not get component."
    End If
```

```
End Sub
```

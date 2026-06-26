---
title: "Change Name of Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Name_of_Component_Example_VB.htm"
---

# Change Name of Component Example (VBA)

This example shows how to change the name of a component.

```
'-------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component in the assembly.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. The selected component's name is
'    changed to SW.
' 2. Examine the Immediate window and
'    FeatureManager design tree to verify.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swComp                      As SldWorks.Component2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
    If swComp Is Nothing Then
        Debug.Print "Select a component and run the macro again."
        Exit Sub
     Else
```

```
        ' swUserPreferenceToggle_e.swExtRefUpdateCompNames must be set to
        ' False to change the name of a component using IComponent2::Name2
        swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swExtRefUpdateCompNames, False
```

```
        ' Print original name of component
        Debug.Print ("  Original name of component = " & swComp.Name2)
```

```
        ' Change name of component
        swComp.Name2 = "SW"
```

```
        ' Print new name of component
        Debug.Print ("  New name of component      = " & swComp.Name2)
    End If
End Sub
```

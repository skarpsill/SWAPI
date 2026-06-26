---
title: "Select Drawing Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Drawing_Component_Example_VB.htm"
---

# Select Drawing Component Example (VBA)

This example shows how to select an assembly component in a drawing.

```
'--------------------------------------------
' Preconditions:
' 1. Open a drawing of an assembly.
' 2. Select an assembly component in the drawing.
'
' Postconditions: Displays a message box
' containing the name of the selected assembly
' component.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swComponent As SldWorks.Component2
Dim swDrawingComponent As SldWorks.DrawingComponent
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModelDoc = swApp.ActiveDoc
    If swModelDoc Is Nothing Then
        Exit Sub
    End If
    Set swSelMgr = swModelDoc.SelectionManager
```

```
    If swSelMgr.GetSelectedObjectCount2(0) = 0 Then
        MsgBox "No selections detected."
        Exit Sub
    End If
```

```
    If swSelMgr.GetSelectedObjectType3(1, 0) = swSelectType_e.swSelCOMPONENTS Then
        Set swDrawingComponent = swSelMgr.GetSelectedObjectsComponent4(1, 0)
        If swDrawingComponent Is Nothing Then
            MsgBox "The component is empty."
            Exit Sub
        Else
            Set swComponent = swDrawingComponent.Component
            MsgBox swComponent.Name2
        End If
    Else
        MsgBox "The selection is not an assembly component."
        Exit Sub
    End If
```

```
End Sub
```

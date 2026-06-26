---
title: "Set Display State of Referenced Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Active_Display_State_of_Referenced_Component_Example_VB.htm"
---

# Set Display State of Referenced Component Example (VBA)

## Set Active Display State of Referenced Component Example (VBA)

This example shows how to set the active display state of a referenced component.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects leg<1>.
' 2. Gets the selected referenced component's active display state.
' 3. Sets the selected referenced component's active display state.
' 4. Examine the Immediate window, FeatureManager design tree,
'    and graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'---------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swComponent As SldWorks.Component2
Dim swSelectionManager As SldWorks.SelectionMgr
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExtension = swModel.Extension
    status = swModelDocExtension.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionManager = swModel.SelectionManager
    Set swComponent = swSelectionManager.GetSelectedObjectsComponent4(1, -1)
    Debug.Print "Get active display state: " & swComponent.ReferencedDisplayState2
    swComponent.ReferencedDisplayState2 = "<Default<As Machined>>_Display State 1"
    Debug.Print "Set active display state: " & swComponent.ReferencedDisplayState2
```

```
End Sub
```

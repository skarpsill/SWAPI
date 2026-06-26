---
title: "Set Display State of Referenced Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Active_Display_State_of_Referenced_Component_Example_VBNET.htm"
---

# Set Display State of Referenced Component Example (VB.NET)

## Set Active Display State of Referenced Component Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swComponent As Component2
        Dim swSelectionManager As SelectionMgr
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExtension = swModel.Extension
        status = swModelDocExtension.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionManager = swModel.SelectionManager
        swComponent = swSelectionManager.GetSelectedObjectsComponent4(1, -1)
        Debug.Print("Get active display state: " & swComponent.ReferencedDisplayState2)
        swComponent.ReferencedDisplayState2 = "<Default<As Machined>>_Display State 1"
        Debug.Print("Set active display state: " & swComponent.ReferencedDisplayState2)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Resolve All Lightweight Components and Fix a Component (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Resolve_All_Components_Fix_A_Component_Example_VB.htm"
---

# Resolve All Lightweight Components and Fix a Component (VBA)

This example shows how to:

- resolve all lightweight components
- fix a component

in the an assembly.

```
'-----------------------------------
' Preconditions:
' 1. Specified file to open exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Resolves all lightweight components
'    in the assembly.
' 2. Fixes the selected component.
' 3. Examine the Immediate window to verify.
'
' NOTE: Because this assembly is used elsewhere,
' do not save any changes when closing it.
'-------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssy As SldWorks.AssemblyDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swComp As SldWorks.Component2
Dim swSelMgr As SldWorks.SelectionMgr
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\key pad_1.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssy = swModel
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Resolve all lightweight components
    errors = swAssy.ResolveAllLightWeightComponents(True)
    Debug.Print ("All lightweight components resolved (0 = All components resolved)? " & errors)
```

```
    ' Fix the selected component
    status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swAssy.FixComponent
    status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
    Debug.Print ("Selected component fixed? " & swComp.IsFixed)
```

```
End Sub
```

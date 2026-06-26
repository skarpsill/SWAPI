---
title: "Link Display States to Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Display_States_to_Configurations_Example_VB.htm"
---

# Link Display States to Configurations Example (VBA)

This example shows how to link and unlink display states to and from configurations.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document
'    to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Follow the instructions in the macro at
'    each Stop statement, which gets and sets whether
'    display states are linked to the active configuration.
' 3. Closes the assembly document without saving
'    any changes.
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swConfigMgr As SldWorks.ConfigurationManager
Dim assemblyFile As String
Dim errors As Long
Dim warnings As Long
Dim assemblyName As String
```

```
Sub main()
```

```
    ' Open assembly document
    assemblyFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm"
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6(assemblyFile, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
    Stop
    ' 1. Click the ConfigurationManager tab in the Manager Pane
    '    in the assembly document.
    ' 2. Right-click the active display state and click Properties.
    ' 3. Verify that the "Link display states to configurations" check box
    '    is selected and click OK.
    ' 4. Click the Continue button in the IDE.
```

```
    Set swConfigMgr = swModel.ConfigurationManager
    swConfigMgr.LinkDisplayStatesToConfigurations = False
    Debug.Print "Are display states linked to configurations? " & swConfigMgr.LinkDisplayStatesToConfigurations
    If Not swConfigMgr.LinkDisplayStatesToConfigurations Then
        Debug.Print "All display states are available to the active configuration."
    End If
    Debug.Print ""
    Stop
    ' 1. Click the ConfigurationManager tab again.
    ' 2. Right-click the active display state and click Properties.
    ' 3. Verify that the "Link display states to configurations" check box
    '    is not selected and click OK.
    ' 4. Click the Continue button in the IDE.
```

```
    swConfigMgr.LinkDisplayStatesToConfigurations = True
    Debug.Print "Are display states linked configurations? " & swConfigMgr.LinkDisplayStatesToConfigurations
    If swConfigMgr.LinkDisplayStatesToConfigurations Then
        Debug.Print "All display states are not available to the active configuration."
    End If
    Stop
    ' 1. Click the ConfigurationManager tab again.
    ' 2. Right-click the active display state and click Properties.
    ' 3. Verify that the "Link display states to configurations" check box
    '    is selected and click OK.
    ' 4. Click the Continue button in the IDE.

    assemblyName = swModel.GetTitle
    swApp.QuitDoc assemblyName
```

```
End Sub
```

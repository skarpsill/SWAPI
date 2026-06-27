---
title: "Update All Toolbox Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_All_Toolbox_Components_Example_VB.htm"
---

# Update All Toolbox Components Example (VBA)

This example shows how to update all SOLIDWORKS Toolbox components in an assembly.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Updates all SOLIDWORKS Toolbox components in the assembly.
' 2. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim errors As Long
Dim warnings As Long
Dim updateToolboxComponents As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    ' Open the assembly
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\lens_mount.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssembly = swModel
```

```
    ' Update all SOLIDWORKS Toolbox components in the assembly
    updateToolboxComponents = swAssembly.updateToolboxComponent(swAssemblyLevelToUpdate_e.swAssemblyLevelToUpdate_AllLevels)
    Debug.Print ("Update SOLIDWORKS Toolbox components status: " & updateToolboxComponents)
```

```
End Sub
```

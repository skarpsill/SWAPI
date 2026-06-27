---
title: "Update All Toolbox Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_All_Toolbox_Components_Example_VBNET.htm"
---

# Update All Toolbox Components Example (VB.NET)

This example shows how to update all SOLIDWORKS Toolbox components in an assembly.

```
'----------------------------------------------------------------
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
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssembly As AssemblyDoc
        Dim errors As Integer
        Dim warnings As Integer
        Dim updateToolboxComponents As Integer

        ' Open the assembly
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\lens_mount.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssembly = swModel

        ' Update all SOLIDWORKS Toolbox components in the assembly
        updateToolboxComponents = swAssembly.UpdateToolboxComponent(swAssemblyLevelToUpdate_e.swAssemblyLevelToUpdate_AllLevels)
        Debug.Print("Update SOLIDWORKS Toolbox components status: " & updateToolboxComponents)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

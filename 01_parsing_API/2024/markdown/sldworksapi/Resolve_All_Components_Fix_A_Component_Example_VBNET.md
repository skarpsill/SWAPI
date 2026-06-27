---
title: "Resolve All Lightweight Components and Fix a Component (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Resolve_All_Components_Fix_A_Component_Example_VBNET.htm"
---

# Resolve All Lightweight Components and Fix a Component (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swAssy As AssemblyDoc
    Dim swModelDocExt As ModelDocExtension
    Dim swComp As Component2
    Dim swSelMgr As SelectionMgr
    Dim fileName As String
    Dim errors As Integer
    Dim warnings As Integer
    Dim status As Boolean

    Sub Main()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\key pad_1.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssy = swModel
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        ' Resolve all lightweight components
        errors = swAssy.ResolveAllLightWeightComponents(True)
        Debug.Print("All lightweight components resolved (0 = All components resolved)? " & errors)

        ' Fix the selected component
        status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swAssy.FixComponent()
        status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
        Debug.Print("Selected component fixed? " & swComp.IsFixed)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

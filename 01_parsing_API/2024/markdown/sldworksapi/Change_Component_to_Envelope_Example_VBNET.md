---
title: "Change Component to Envelope Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Component_to_Envelope_Example_VBNET.htm"
---

# Change Component to Envelope Example (VB.NET)

This example shows how to change a component to an envelope.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects the shaft washer-4 component.
' 3. Gets whether the component is an envelope.
' 4. Changes the component to an envelope.
' 5. Gets whether the component is an envelope.
' 6. Examine the Immediate window and FeatureManager design tree.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swAssembly As AssemblyDoc
        Dim swComponent As Component2
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select shaft washer-4 component
        swModelDocExtension = swModel.Extension
        status = swModelDocExtension.SelectByID2("shaft washer-4@98food processor", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swComponent = swSelectionMgr.GetSelectedObjectsComponent4(1, -1)

        'Get whether selected component is an envelope
        Debug.Print("Before calling IAssemblyDoc::CompConfigProperties5:")
        Debug.Print("   Is component an envelope? " & swComponent.IsEnvelope)

        'Change the selected component to an envelope
        swAssembly = swModel
        status = swAssembly.CompConfigProperties6(swComponentSuppressionState_e.swComponentFullyResolved, swComponentSolvingOption_e.swComponentRigidSolving, True, True, "Default", False, True, swASMSLDPRTCompPref_e.swAlwaysInclude)

        'Get whether the selected component is an envelope
        Debug.Print("After calling IAssemblyDoc::CompConfigProperties5:")
        Debug.Print("  Is component an envelope? " & swComponent.IsEnvelope)

        swModel.EditRebuild3()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

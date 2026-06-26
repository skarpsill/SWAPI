---
title: "Change Name of Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Name_of_Component_Example_VBNET.htm"
---

# Change Name of Component Example (VB.NET)

This example shows how to change the name of a component.

```
'-------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component in the assembly.
' 3. Open the Immediate window.
' 4. Press F5.
'
' Postconditions:
' 1. The selected component's name is
'    changed to "SW".
' 2. Examine the Immediate window and
'    FeatureManager design tree to verify.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swComp As Component2

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
        If swComp Is Nothing Then
            Debug.Print("Select a component and run the macro again.")
            Exit Sub
        Else

            ' swUserPreferenceToggle_e.swExtRefUpdateCompNames must be set to
            ' False to change the name of a component using IComponent2::Name2
            swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swExtRefUpdateCompNames, False)

            ' Print original name of component
            Debug.Print("  Original name of component = " & swComp.Name2)

            ' Change name of component
            swComp.Name2 = "SW"

            ' Print new name of component
            Debug.Print("  New name of component      = " & swComp.Name2)
        End If
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

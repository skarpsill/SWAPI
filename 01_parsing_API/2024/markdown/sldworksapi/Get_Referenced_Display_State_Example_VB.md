---
title: "Get Referenced Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Referenced_Display_State_Example_VB.htm"
---

# Get Referenced Display State Example (VBA)

This example shows how to get the active display state of a component.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly that contains two instances of the same
 '    component in different display states.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the display states.
 '---------------------------------------------------------------------------
Option Explicit

Sub main()
     Dim swApp As SldWorks.SldWorks
     Set swApp = Application.SldWorks

    Dim assem As AssemblyDoc
     Set assem = swApp.ActiveDoc

    Dim model As ModelDoc2
     Set model = assem

    Dim assemConfig As Configuration
     Set assemConfig = model.ConfigurationManager.ActiveConfiguration

    Dim root As Component2
     Set root = assemConfig.GetRootComponent3(False)

    Dim comps
     comps = root.GetChildren

    Dim vComp
     For Each vComp In comps
         Dim comp As Component2
         Set comp = vComp

        Dim refConfigName As String
         refConfigName = comp.ReferencedConfiguration

        Dim compModel As ModelDoc2
         Set compModel = comp.GetModelDoc2

        compModel.Visible = True

        Dim cmActiveConfig As Configuration
         Set cmActiveConfig = compModel.ConfigurationManager.ActiveConfiguration

        Debug.Print comp.Name2
         Debug.Print "  " & cmActiveConfig.Name & " <" & comp.ReferencedDisplayState & ">"

         compModel.Visible = False
     Next
 End Sub
```

---
title: "Get Referenced Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Referenced_Display_State_Example_VBNET.htm"
---

# Get Referenced Display State Example (VB.NET)

This example shows how to get the active display state of a component.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly that contains two instances of the same
'    component in different display states.
' 2. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window for the display states.
'---------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim assem As AssemblyDoc
         assem = swApp.ActiveDoc

         Dim model As ModelDoc2
         model = assem

         Dim assemConfig As Configuration
         assemConfig = model.ConfigurationManager.ActiveConfiguration

         Dim root As Component2
         root = assemConfig.GetRootComponent3(False)

         Dim comps As Object
         comps = root.GetChildren

         Dim vComp As Object
         For Each vComp In comps
             Dim comp As Component2
             comp = vComp

             Dim refConfigName As String
             refConfigName = comp.ReferencedConfiguration

             Dim compModel As ModelDoc2
             compModel = comp.GetModelDoc2

             compModel.Visible = True

             Dim cmActiveConfig As Configuration
             cmActiveConfig = compModel.ConfigurationManager.ActiveConfiguration

             Debug.Print(comp.Name2)
             Debug.Print("  " & cmActiveConfig.Name & " <" & comp.ReferencedDisplayState   ">")

             compModel.Visible = False
         Next
     End Sub

     Public swApp As SldWorks
 End  Class
```

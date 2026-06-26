---
title: "Get Explode Step Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Explode_Step_Example_VBNET.htm"
---

# Get Explode Step Example (VB.NET)

This example shows how to get an explode step and its properties.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document with an explode view.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Gets the first explode step.
' 2. Examine the Immediate window.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfigurationMgr As ConfigurationManager
        Dim swConfiguration As Configuration
        Dim swExplodeStep As ExplodeStep

        swModel = swApp.ActiveDoc

        'Get explode step
        swConfigurationMgr = swModel.ConfigurationManager
        swConfiguration = swConfigurationMgr.ActiveConfiguration
        swExplodeStep = swConfiguration.GetExplodeStep(0)
        Debug.Print("Name of explode step: " & swExplodeStep.Name)
        Debug.Print("Number of components that move in this explode step: " & swExplodeStep.GetNumOfComponents)
        Debug.Print("Is the sub-assembly rigid? " & swExplodeStep.IsSubAssemblyRigid)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Get Explode Step Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Explode_Step_Example_VB.htm"
---

# Get Explode Step Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swConfigurationMgr As SldWorks.ConfigurationManager
Dim swConfiguration As SldWorks.Configuration
Dim swExplodeStep As SldWorks.ExplodeStep
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Get explode step
    Set swConfigurationMgr = swModel.ConfigurationManager
    Set swConfiguration = swConfigurationMgr.ActiveConfiguration
    Set swExplodeStep = swConfiguration.GetExplodeStep(0)
    Debug.Print "Name of explode step: " & swExplodeStep.Name
    Debug.Print "Number of components that move in this explode step: " & swExplodeStep.GetNumOfComponents
    Debug.Print "Is the sub-assembly rigid? " & swExplodeStep.IsSubAssemblyRigid
```

```
End Sub
```

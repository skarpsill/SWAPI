---
title: "Specify Order of Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Specify_Order_of_Configurations_Example_VB.htm"
---

# Specify Order of Configurations Example (VBA)

This example shows how to specify the order in which to list configurations in the ConfigurationManager.

```
'-------------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
' 2. Click the ConfigurationManager tab and examine the order in which the
'    configurations are listed.
'
' Preconditions:
' 1. Lists the configurations in the specified order.
' 2. Examine the ConfigurationManager tab.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-------------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swConfigMgr As SldWorks.ConfigurationManager
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    swConfigMgr.SortConfigurationTree swConfigTreeSortType_e.swSortType_Literal
    swModel.EditRebuild3
```

```
End Sub
```

---
title: "Specify Order of Configurations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Specify_Order_of_Configurations_Example_VBNET.htm"
---

# Specify Order of Configurations Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfigMgr As ConfigurationManager

        swModel = swApp.ActiveDoc
        swConfigMgr = swModel.ConfigurationManager
        swConfigMgr.SortConfigurationTree(swConfigTreeSortType_e.swSortType_Literal)
        swModel.EditRebuild3()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

---
title: "Link Display States to Configurations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Display_States_to_Configurations_Example_VBNET.htm"
---

# Link Display States to Configurations Example (VB.NET)

## Link Display States to Configurations Example(VB.NET)

This example shows how to link and unlink display states to and from configurations.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets whether display states are linked to
'    the active configuration.
' 2. Closes the assembly document without saving
'    any changes.
'-----------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System.Diagnostics

	Imports System

	Partial Class SolidWorksMacro

	    Public Sub Main()

	        Dim swModel As ModelDoc2

	        Dim swConfigMgr As ConfigurationManager

	        Dim assemblyName As String

	        swModel = swApp.ActiveDoc

	        Debug.Print("")

	        swConfigMgr = swModel.ConfigurationManager

	        swConfigMgr.LinkDisplayStatesToConfigurations = False

	        Debug.Print("Are display states linked to configurations? " & swConfigMgr.LinkDisplayStatesToConfigurations)

	        If Not swConfigMgr.LinkDisplayStatesToConfigurations Then

	            Debug.Print("All display states are available to the active configuration.")

	        End If

	        swConfigMgr.LinkDisplayStatesToConfigurations = True

	        Debug.Print("Are display states linked configurations? " & swConfigMgr.LinkDisplayStatesToConfigurations)

	        If swConfigMgr.LinkDisplayStatesToConfigurations Then

	            Debug.Print("All display states are not available to the active configuration.")

	        End If

	        assemblyName = swModel.GetTitle

	        swApp.QuitDoc(assemblyName)

	    End Sub

	    ''' <summary>

	    '''
	The SldWorks swApp variable is pre-assigned for you.

	    ''' </summary>

	    Public swApp As SldWorks

	End Class
```

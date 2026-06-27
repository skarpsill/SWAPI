---
title: "Get Whether Components Are Loaded Example(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Components_Are_Loaded_Example_VBNET.htm"
---

# Get Whether Components Are Loaded Example(VB.NET)

## Get Whether Components Are Loaded Example (VB.NET)

This example gets whether the components in an assembly document are
loaded.

```vb
'----------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Loads the Magnet-1 component.
 ' 2. Examine the Immediate window.
' NOTE: Because this assembly document is used elsewhere,
 ' do not save changes.
 '-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocSpecification As DocumentSpecification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sComponents(0) As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Components As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swComponent As Component2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sName As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAssembly As AssemblyDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longstatus As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longwarnings As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swConfigMgr As ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swConfig As Configuration

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Selectively open speaker.sldasm assembly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Load only the Magnet-1 component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sComponents(0) = "Magnet-1@speaker"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Components = sComponents
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.ComponentList = Components
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.Selective = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sName = swDocSpecification.FileName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DocumentType = swDocumentTypes_e.swDocASSEMBLY
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DisplayState = "Default_Display State-1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.UseLightWeightDefault = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.LightWeight = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.Silent = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.IgnoreHiddenComponents = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc7(swDocSpecification)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}longstatus = swDocSpecification.Error
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}longwarnings = swDocSpecification.Warning

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get whether the components in the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' assembly document are loaded and suppressed; only
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Magnet-1 should be loaded and not suppressed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfigMgr = swModel.ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfig = swConfigMgr.ActiveConfiguration
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Components = swAssembly.GetComponents(True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(Components)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swComponent = Components(i)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (swComponent.IsLoaded) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component: " & swComponent.Name & " is loaded.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component: " & swComponent.Name & " is not loaded.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Suppressed: " & swConfig.GetComponentSuppressionState(swComponent.Name))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```

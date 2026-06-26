---
title: "Get Linked Display States Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Linked_Display_States_Example_VBNET.htm"
---

# Get Linked Display States Example (VB.NET)

This example gets an assembly and reports on its active
configuration and display states.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the
 '    required DLLs are registered.
 ' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
 ' kadov_tag{{</spaces>}}3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 '    interop assembly is loaded in the project.
 ' kadov_tag{{<spaces>}}   (right-click the project in Project Explorer, click
 '    Add Reference, kadov_tag{{</spaces>}}click the interop assembly in the
 '    .NET tab, or browse for the DLL in
 '    install_dir\api\redist).
 ' kadov_tag{{<spaces>}}4. Substitute your license key for your_license_key in
 '    the code.
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate Window for output.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swCf As SwDMClassFactory
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCf = New SwDMClassFactory
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocMgr As SwDMApplication

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocMgr = swCf.GetApplication("your_license_key")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer, j As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDoc12 As SwDMDocument14
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim res As SwDmDocumentOpenError
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim dt As SwDmDocumentType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}dt = SwDmDocumentType.swDmDocumentAssembly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim filename As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Opening an assembly...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\motor casing.sldasm"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc12 = swDocMgr.GetDocument(filename, dt, False, res)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swDoc12 Is Nothing Or (res <> SwDmDocumentOpenError.swDmDocumentOpenErrorNone) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Error opening file....")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim activeConfig As SwDMConfiguration12
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim activeConfigName As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim configMgr As SwDMConfigurationMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}configMgr = swDoc12.ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}activeConfigName = configMgr.GetActiveConfigurationName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Getting the active configuration: " & activeConfigName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}activeConfig = configMgr.GetConfigurationByName(activeConfigName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If activeConfig Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Error getting the active configuration...")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("ID of " & activeConfig.Name2 & ": " & activeConfig.GetID)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim numLinkedDisplayStates As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ldsVariant As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim lds As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim compVisibleList As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim compFileDirectory As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ldsVariant = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}numLinkedDisplayStates = activeConfig.GetLinkedDisplayStates(ldsVariant)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Number of linked display states of " & activeConfigName & ": " & numLinkedDisplayStates)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Getting all the components for one linked display state
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}compVisibleList = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}compFileDirectory = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}lds = ldsVariant(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}activeConfig.GetComponentVisibleByDisplayStateName(lds, compVisibleList, compFileDirectory)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Getting the paths and file names of all of the components in the linked display state, " & lds & ": ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To UBound(compFileDirectory)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Component: " & compFileDirectory(j))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Is visible? " & compVisibleList(j))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next 'component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Getting all the components in the configuration
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Getting the names of all of the components in the FeatureManager design tree for " & activeConfig.Name2 & ": ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vComponents As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vComponents = activeConfig.GetComponents
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not (IsNothing(vComponents)) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim swDmComponent As SwDMComponent11
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To UBound(vComponents)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swDmComponent = vComponents(i)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Component name: " & swDmComponent.Name3)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For a selective open with OpenDoc7, use: " & swDmComponent.SelectName2)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next 'component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc12.CloseDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```

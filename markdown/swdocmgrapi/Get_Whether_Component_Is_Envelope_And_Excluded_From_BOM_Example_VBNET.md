---
title: "Get Whether Component Is Envelope And Excluded From BOM (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm"
---

# Get Whether Component Is Envelope And Excluded From BOM (VB.NET)

This example shows how to find out if a component is an envelope and
whether the component is included in the bill of materials (BOM).

```vb
 '---------------------------------------------------------------------------
' Preconditions: kadov_tag{{<spaces>}}
' 1. Open SOLIDWORKS and copy the code below to a VB.NET macro.
' 2. Ensure that the kadov_tag{{</spaces>}} specified file exists.
' 3. Specify your_license_key.
' 4. Open an Immediate window.
'
' Postconditions: Inspect the Immediate window.
'
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTE: ISwDMComponent5::ExcludeFromBom and ISwDMComponent5::IsEnvelope print
' kadov_tag{{</spaces>}}to the Immediate Window for each component.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports SwDocumentMgr
Imports System.Diagnostics
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swClassFact As SwDocumentMgr.SwDMClassFactory
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocMgr As SwDocumentMgr.SwDMApplication
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDoc As SwDocumentMgr.SwDMDocument7
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swCfgMgr As SwDocumentMgr.SwDMConfigurationMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swConfiguration7 As SwDMConfiguration7
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swComponents As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sDocFileName As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nDocType As SwDocumentMgr.SwDmDocumentType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nRetVal As SwDocumentMgr.SwDmDocumentOpenError
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sLicenseKey As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sLicenseKey = "your_license_key"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sDocFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nDocType = SwDocumentMgr.SwDmDocumentType.swDmDocumentAssembly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocMgr = swClassFact.GetApplication(sLicenseKey)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCfgMgr = swDoc.ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SWConfigNames() As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SWConfigNames = swCfgMgr.GetConfigurationNames
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j As Integer = 0 To UBound(SWConfigNames)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swConfiguration7 = swCfgMgr.GetConfigurationByName(SWConfigNames(j))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swComponents = swConfiguration7.GetComponents
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Configuration Name = " & SWConfigNames(j))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For I As Integer = 0 To UBound(swComponents)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim comp As SwDMComponent5
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}comp = swComponents(I)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component Name = " & comp.Name)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}IsEnvelope = " & comp.IsEnvelope)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}ExcludeFromBOM = " & comp.ExcludeFromBOM)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("_______________________________________________________")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc.CloseDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```

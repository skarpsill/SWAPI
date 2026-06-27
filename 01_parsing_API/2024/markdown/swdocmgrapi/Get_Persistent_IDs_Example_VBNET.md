---
title: "Get IDs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Persistent_IDs_Example_VBNET.htm"
---

# Get IDs Example (VB.NET)

## Get Sheet IDs Example (VB.NET)

This example shows how to get the IDs of
drawing sheets.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Read the SOLIDWORKS Document Manager API
 '    Help Getting Started topic and ensure that
 '    the required DLLs are registered.
 ' 2. Open SOLIDWORKS and copy the code below to a VB.NET macro.
 ' kadov_tag{{</spaces>}}3. Convert the drawing document specified
 '    in sDocFileName to the latest supported
 '    version by opening and saving it to another name
 '    in SOLIDWORKS.
 '
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Because this document is used elsewhere, do not
 '    save any changes when closing it.
 '
 ' kadov_tag{{</spaces>}}4. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 '    interop assembly is loaded in the project. (Right-click
 '    the project in Project Explorer, click Add Reference,
 '    kadov_tag{{</spaces>}}click the interop assembly in the .NET tab, or browse
 '    for the DLL in install_dir\api\redist.)
 ' kadov_tag{{</spaces>}}5. Substitute your license key for your_license_key in the code.
 '
 ' Postconditions: kadov_tag{{</spaces>}}Inspect the Immediate Window for the sheet IDs.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swdocumentmgr
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swClassFact As SwDMClassFactory
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDocMgr As SwDMApplication
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDoc As SwDMDocument14
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sDocFileName As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nDocType As SwDmDocumentType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nRetVal As SwDmDocumentOpenError
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim sLicenseKey As String

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Specify your license key
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sLicenseKey = "your_license_key"

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If this drawing document doesn't exist on your system,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' then substitute the name of drawing document that does
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sDocFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nDocType = SwDmDocumentType.swDmDocumentDrawing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocMgr = swClassFact.GetApplication(sLicenseKey)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swDoc Is Nothing) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Unable to open document. Correct path to file or register Document Manager DLL.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Sheet As SwDMSheet3
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Sheets As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Sheets = swDoc.GetSheets
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(Sheets)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sheet = Sheets(i)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(Sheet.Name & " ID: " & Sheet.GetID)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDoc.CloseDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```

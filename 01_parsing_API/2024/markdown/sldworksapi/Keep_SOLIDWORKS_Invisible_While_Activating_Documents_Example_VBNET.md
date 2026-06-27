---
title: "Keep SOLIDWORKS Invisible While Activating Documents Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm"
---

# Keep SOLIDWORKS Invisible While Activating Documents Example (VB.NET)

This example shows how to keep SOLIDWORKS invisible while activating SOLIDWORKS
documents, including assembly component files, and saving those documents
as PDF files.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly file exists.
' 2. Verify that c:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Saves the specified assembly file and its
'    component files as PDF files to the c:\temp.
' 2. Examine the Immediate window and c:\temp.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swModel As ModelDoc2
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swExtension As ModelDocExtension

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim pFrame As Frame
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Document As String
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Output As String

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}On Error GoTo Fail

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Allow SOLIDWORKS to run in the background
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and be invisible
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.UserControl = False

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If the following property is true, then the
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' SOLIDWORKS frame will be visible on a call to
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' ISldWorks::ActivateDoc2; so, set it to false
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.Visible = False

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Keep SOLIDWORKS frame invisible when
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' ISldWorks::ActivateDoc2 is called
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pFrame = swApp.Frame
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pFrame.KeepInvisible = True

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\blade shaft.sldasm"
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Output = "c:\temp\"

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("--- Save files as PDF ---")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SaveToPDF(Document, Output)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.CloseAllDocuments(True)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("--- Done ---")

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show SOLIDWORKS frame and SOLIDWORKS
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pFrame.KeepInvisible = False
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.Visible = True
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
 Fail:
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Execution failed with error " & Err.Number & ": '" & Err.Description & "'")

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub SaveToPDF(ByVal docFileName As String, ByVal outputpath As String)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAssembly As AssemblyDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim doctype As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errors As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim warnings As Integer
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim modelpath As String = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim modelFileName As String = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim convFileName As String = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Success As Boolean
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vComponents As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Determine the type of SOLIDWORKS file based on
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' its filename extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If LCase(Right(docFileName, 7)) = ".sldprt" Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}doctype = swDocumentTypes_e.swDocPART
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf LCase(Right(docFileName, 7)) = ".sldasm" Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}doctype = swDocumentTypes_e.swDocASSEMBLY
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf LCase(Right(docFileName, 7)) = ".slddrw" Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}doctype = swDocumentTypes_e.swDocDRAWING
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}doctype = swDocumentTypes_e.swDocNONE
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open document
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.OpenDoc6(docFileName, doctype, swOpenDocOptions_e.swOpenDocOptions_Silent Or swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swModel Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Failed to open document " + modelpath + ". Errors: " & errors)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Activate the document, which should remain invisible
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' due to earlier call to IFrame::KeepInvisible
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActivateDoc2(docFileName, True, errors)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Build destination filename
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelpath = swModel.GetPathName()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelFileName = Mid(modelpath, InStrRev(modelpath, "\") + 1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelFileName = Left(modelFileName, InStrRev(modelFileName, ".") - 1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}convFileName = outputpath + modelFileName + ".pdf"

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Save document as PDF
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swExtension = swModel.Extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Success = swExtension.SaveAs(convFileName, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Success Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Document, " + modelpath + ", saved as " + convFileName + ". ")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Document not saved: ")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Errors: " & errors + modelpath + " as " + convFileName + ". ")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Process all components
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If doctype = swDocumentTypes_e.swDocASSEMBLY Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssembly = swModel
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vComponents = swAssembly.GetComponents(True)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To UBound(vComponents)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim swComponent As Component2
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swComponent = vComponents(i)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SaveToPDF(swComponent.GetPathName(), outputpath)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next i
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```

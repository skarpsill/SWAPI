---
title: "Keep SOLIDWORKS Invisible While Activating Documents Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm"
---

# Keep SOLIDWORKS Invisible While Activating Documents Example VB

## Keep SOLIDWORKS Invisible While Activating Documents Example (VBA)

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
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swExtension As SldWorks.ModelDocExtension
 Dim swAssembly As SldWorks.AssemblyDoc
 Dim doctype As Long
 Dim errors As Long
 Dim warnings As Long
 Dim modelpath As String
 Dim modelFileName As String
 Dim convFileName As String
 Dim Success As Boolean
 Dim vComponents As Variant
 Dim i As Long
 Dim outputpath As String

Sub SaveToPDF(docFileName As String, outputpath As String)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Determine the type of SOLIDWORKS file based on
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' its filename extension
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If LCase(Right(docFileName, 7)) = ".sldprt" Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doctype = swDocPART
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf LCase(Right(docFileName, 7)) = ".sldasm" Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doctype = swDocASSEMBLY
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ElseIf LCase(Right(docFileName, 7)) = ".slddrw" Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doctype = swDocDRAWING
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}doctype = swDocNONE
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Open document
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.OpenDoc6(docFileName, doctype, swOpenDocOptions_Silent Or swOpenDocOptions_ReadOnly, "", errors, warnings)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swModel Is Nothing Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Failed to open document " + modelpath + ". Errors: " & errors
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Activate the document, which should remain invisiblekadov_tag{{<spaces>}}
     kadov_tag{{</spaces>}}' due to earlier call to IFrame::KeepInvisible
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActivateDoc2(docFileName, True, errors)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Build destination file name
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}modelpath = swModel.GetPathName()
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}modelFileName = Mid(modelpath, InStrRev(modelpath, "\") + 1)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}modelFileName = Left(modelFileName, InStrRev(modelFileName, ".") - 1)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}convFileName = outputpath + modelFileName + ".pdf"
 kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Save document as PDF
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swExtension = swModel.Extension
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Success = swExtension.SaveAs(convFileName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, Nothing, errors, warnings)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Success Then
 kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Debug.Print "Document, " + modelpath + ", saved as " + convFileName + ". "
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Debug.Print "Document not saved: "
 kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Errors: " & errors + modelpath + " as " + convFileName + ". "
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Process all components
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If doctype = swDocASSEMBLY Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swAssembly = swModel
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vComponents = swAssembly.GetComponents(True)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(vComponents)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim swComponent As SldWorks.Component2
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swComponent = vComponents(i)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SaveToPDF swComponent.GetPathName(), outputpath
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Sub

Sub main() kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}On Error GoTo Fail:

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get SOLIDWORKS
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Allow SOLIDWORKS to run in the background
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' and be invisible
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.UserControl = False
 kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' If the following property is true, then the
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' SOLIDWORKS frame will be visible on a call to
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' ISldWorks::ActivateDoc2; so set it to false
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.visible = False
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Keep SOLIDWORKS frame invisible when
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' ISldWorks::ActivateDoc2 is called
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim pFrame As Frame
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set pFrame = swApp.Frame
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}pFrame.KeepInvisible = True

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim Document As String
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim Output As String kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\blade shaft.sldasm"
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Output = "c:\temp\"
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "--- Save files as PDF ---"
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SaveToPDF Document, Output
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.CloseAllDocuments True
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "--- Done ---"
 kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Show SOLIDWORKS frame and SOLIDWORKS
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}pFrame.KeepInvisible = False
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.visible = True
     kadov_tag{{</spaces>}}Exit Sub
     kadov_tag{{</spaces>}}
Fail:
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Execution failed with error " & Err.Number & ": '" & Err.Description & "'"

End Sub
```

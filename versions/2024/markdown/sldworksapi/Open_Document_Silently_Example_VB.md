---
title: "Open Document Silently Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Document_Silently_Example_VB.htm"
---

# Open Document Silently Example (VBA)

This example shows how to open a document silently; that is, without
dialog boxes.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the document specified to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document silently (i.e., no dialogs
'    are displayed).
' 2. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
sDocFileNamekadov_tag{{</spaces>}}As String =
"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
kadov_tag{{<spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{</spaces>}}As
SldWorks.SldWorks
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{</spaces>}}As
SldWorks.modelDoc
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nDocTypekadov_tag{{</spaces>}}As
Long
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nErrorskadov_tag{{</spaces>}}As
Long
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nWarningskadov_tag{{</spaces>}}As
Longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Determine type of SOLIDWORKS file based on file extension
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
InStr(LCase(sDocFileName), "sldprt") > 0 Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocType
= swDocPART
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
InStr(LCase(sDocFileName), "sldasm") > 0 Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocType
= swDocASSEMBLY
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
InStr(LCase(sDocFileName), "slddrw") > 0 Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocType
= swDocDRAWING
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Probably not a SOLIDWORKS file
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocType
= swDocNONE
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
So cannot open the file
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Ifkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.OpenDoc6(sDocFileName,
nDocType,kadov_tag{{</spaces>}}swOpenDocOptions_Silent,
"", nErrors, nWarnings)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Errorkadov_tag{{<spaces>}}(0 = no errors)kadov_tag{{</spaces>}}=
" & nErrors

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Warnings
(2 = document is read-only)
= " & nWarnings

End Sub

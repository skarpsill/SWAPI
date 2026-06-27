---
title: "Get Hidden Components Filenames Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hidden_Components_Filenames_Example_VBNET.htm"
---

# Get Hidden Components Filenames Example (VB.NET)

This example shows how to get the filenames of the hidden components in an
assembly.

```
'-----------------------------------------------------------
' Preconditions:
' 1. In SOLIDWORKS, click File > Open, and browse to
'    public_documents\samples\tutorial\routing-pipes.
' 2. Click ball valve with flanges.sldasm > Mode >
'    Large Design Review > Open > OK.
'
'    NOTE: If the path to the Design Library does not exist,
'    then multiple dialogs informing you that SOLIDWORKS is unable
'    to locate might be displayed some components. Click No or OK
'    to close these dialogs.
'
' 3. Click ball valve-1 in the FeatureManager design tree
'    and click Selective Open > Selective Open > Selected components >
'    Open Selected > OK.
'
'    NOTE: Only the selected components are loaded. Components
'    not selected are not loaded and not visible in the
'    SOLIDWORKS graphics area.
'
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Does not load the slip on weld flange components because
'    they are hidden.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this assembly elsewhere, do not save changes.
'-----------------------------------------------------------
```

```vb
Option Explicit On
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAssembly As AssemblyDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swAssembly.HasUnloadedComponents Then

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim oPaths As Object = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim oRefdConfigs As Object = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim oReasons As Object = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim oDocTypes As Object = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim oNames As Object = Nothing

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oNames = swAssembly.GetUnloadedComponentNames(oPaths, oRefdConfigs, oReasons, oDocTypes)

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim Paths() As String = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim RefdConfigs() As String = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim Reasons() As Integer = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim DocTypes() As Integer = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim Names() As String = Nothing

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Paths = oPaths
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RefdConfigs = oRefdConfigs
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Reasons = oReasons
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DocTypes = oDocTypes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Names = oNames

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not (IsArray(Paths) And IsArray(RefdConfigs) And IsArray(Reasons) And IsArray(DocTypes) And IsArray(Names)) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MsgBox("Error: Non-array parameter!")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Assert(False)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (LBound(Paths) <> LBound(RefdConfigs)) Or (LBound(Paths) <> LBound(Reasons)) Or (LBound(Paths) <> LBound(DocTypes) Or (LBound(Paths) <> LBound(Names))) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MsgBox("Error: Array lower bounds do not match!")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Assert(False)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (UBound(Paths) <> UBound(RefdConfigs)) Or (UBound(Paths) <> UBound(Reasons)) Or (UBound(Paths) <> UBound(DocTypes) Or (UBound(Paths) <> UBound(Names))) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MsgBox("Error: Array upper bounds do not match!")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Assert(False)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim index As Integer
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For index = LBound(Paths) To UBound(Paths)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim debugMessage As String
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}debugMessage = index & ": "

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim eDocType As swDocumentTypes_e
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}eDocType = DocTypes(index)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case eDocType
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDocumentTypes_e.swDocNONE
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The document "
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDocumentTypes_e.swDocPART
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The part "
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDocumentTypes_e.swDocASSEMBLY
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The assembly "
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDocumentTypes_e.swDocDRAWING
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The drawing "
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDocumentTypes_e.swDocSDM
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The SDM "
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case Else
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage & "The document is an unknown type "
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}debugMessage = debugMessage & Paths(index) & " was not loaded because it is "

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim bUnloadedBecauseHidden As Boolean
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bUnloadedBecauseHidden = Reasons(index)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If bUnloadedBecauseHidden Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}debugMessage = debugMessage & "hidden."
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}debugMessage = debugMessage & "suppressed."
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(debugMessage)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```

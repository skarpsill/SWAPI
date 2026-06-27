---
title: "Copy and Paste Drawing Sheet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm"
---

# Copy and Paste Drawing Sheet Example (VB.NET)

This example shows how to copy and paste drawing sheets.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a drawing document containing one sheet
'    named Sheet1.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Activates Sheet1.
' 2. Copy and pastes Sheet1 as Sheet1(2) and activates Sheet1(2).
' 3. Copy and pastes Sheet1 as Sheet1(3) and activates Sheet1(3).
' 4. Examine the FeatureManager design tree and Immediate window.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim Part As DrawingDoc
        Dim swModel As ModelDoc2
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        Part = swModel
        If (Part Is Nothing) Then
            MsgBox(" Please open a drawing document. ")
            Exit Sub
        End If

        Dim currentsheet As Sheet
        currentsheet = Part.GetCurrentSheet
        Part.ActivateSheet(currentsheet.GetName)
        Debug.Print("Active sheet: " & currentsheet.GetName)

        boolstatus = swModel.Extension.SelectByID2("Sheet1", "SHEET", 0.09205356547875, 0.10872368523, 0, False, 0, Nothing, 0)
        swModel.EditCopy()
        boolstatus = Part.PasteSheet(swInsertOptions_e.swInsertOption_BeforeSelectedSheet, swRenameOptions_e.swRenameOption_No)
        currentsheet = Part.GetCurrentSheet
        Part.ActivateSheet(currentsheet.GetName)
        Debug.Print("Active sheet: " & currentsheet.GetName)

        boolstatus = swModel.Extension.SelectByID2("Sheet1", "SHEET", 0.09205356547875, 0.10872368523, 0, False, 0, Nothing, 0)
        swModel.EditCopy()
        boolstatus = Part.PasteSheet(swInsertOptions_e.swInsertOption_AfterSelectedSheet, swRenameOptions_e.swRenameOption_No)
        currentsheet = Part.GetCurrentSheet
        Part.ActivateSheet(currentsheet.GetName)
        Debug.Print("Active sheet: " & currentsheet.GetName)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

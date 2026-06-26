---
title: "Copy and Paste Drawing Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Drawing_Sheet_Example_VB.htm"
---

# Copy and Paste Drawing Sheet Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As DrawingDoc
Dim swModel As ModelDoc2
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set Part = swModel
```

```
    If (Part Is Nothing) Then
        MsgBox " Please open a drawing document. "
        End
    End If
```

```
    Dim currentsheet As Sheet
    Set currentsheet = Part.GetCurrentSheet
    Part.ActivateSheet (currentsheet.GetName)
    Debug.Print "Active sheet: " & currentsheet.GetName
```

```
    boolstatus = Part.Extension.SelectByID2("Sheet1", "SHEET", 0.09205356547875, 0.10872368523, 0, False, 0, Nothing, 0)
    swModel.EditCopy
    boolstatus = Part.PasteSheet(swInsertOption_BeforeSelectedSheet, swRenameOption_No)
    Set currentsheet = Part.GetCurrentSheet
    Part.ActivateSheet (currentsheet.GetName)
    Debug.Print "Active sheet: " & currentsheet.GetName
```

```
    boolstatus = Part.Extension.SelectByID2("Sheet1", "SHEET", 0.09205356547875, 0.10872368523, 0, False, 0, Nothing, 0)
    swModel.EditCopy
    boolstatus = Part.PasteSheet(swInsertOption_AfterSelectedSheet, swRenameOption_No)
    Set currentsheet = Part.GetCurrentSheet
    Part.ActivateSheet (currentsheet.GetName)
    Debug.Print "Active sheet: " & currentsheet.GetName
```

```
End Sub
```

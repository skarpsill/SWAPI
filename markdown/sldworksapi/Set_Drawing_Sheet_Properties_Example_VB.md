---
title: "Set Drawing Sheet Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Drawing_Sheet_Properties_Example_VB.htm"
---

# Set Drawing Sheet Properties Example (VBA)

This example shows how to set the properties of a drawing sheet.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Create a new drawing document.
' 2. Add another sheet to the drawing.
' 3. Select the Tools > Options > Document Properties >
'    Drawing Sheets > Use custom property values from the sheet
'    check box if it is not selected.
' 4. Right-click Sheet2, click Properties, clear the Same as sheet
'    specified in Document Properties check box if it is selected, and
'    click OK to close the Sheet Properties dialog.
'
' Postconditions:
' 1. Selects the Same as sheet specified in Document Properties
'    check box on the Sheet Properties dialog.
' 2. Right-click Sheet2 and click Properties to verify step 1.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim sheetProperties As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swDrawing = swApp.ActiveDoc
```

```
    ' Active sheet is Sheet2
    Set swSheet = swDrawing.GetCurrentSheet
    sheetProperties = swSheet.GetProperties2
    sheetProperties(7) = 1#
    swSheet.SetProperties2 sheetProperties(0), sheetProperties(1), sheetProperties(2), sheetProperties(3), sheetProperties(4), sheetProperties(5), sheetProperties(6), sheetProperties(7)
```

```
End Sub
```

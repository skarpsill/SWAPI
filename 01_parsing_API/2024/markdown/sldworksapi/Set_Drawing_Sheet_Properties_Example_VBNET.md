---
title: "Set Drawing Sheet Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Drawing_Sheet_Properties_Example_VBNET.htm"
---

# Set Drawing Sheet Properties Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swDrawing As DrawingDoc
        Dim swSheet As Sheet
        Dim sheetProperties As Object

        swDrawing = swApp.ActiveDoc

        ' Active sheet is Sheet2
        swSheet = swDrawing.GetCurrentSheet
        sheetProperties = swSheet.GetProperties2
        sheetProperties(7) = 1.0#
        swSheet.SetProperties2(sheetProperties(0), sheetProperties(1), sheetProperties(2), sheetProperties(3), sheetProperties(4), sheetProperties(5), sheetProperties(6), sheetProperties(7))

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

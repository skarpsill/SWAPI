---
title: "Get Name of Drawing Sheet Template Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Name_and_Properties_of_Drawing_Sheet_Template_Example_VB.htm"
---

# Get Name of Drawing Sheet Template Example (VBA)

This example shows how to get the name of a drawing sheet template.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a drawing document that contains at least one sheet.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the current sheet, drawing's path and file name,
'    sheet's name, template's path and file name, and sheet's
'    properties.
' 2. Examine the Immediate window.
'-----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim vSheetProps As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Sheet = " & swSheet.GetName
    Debug.Print "    Template = " & swSheet.GetTemplateName
```

```
    ' Get current sheet settings
    vSheetProps = swSheet.GetProperties
    Debug.Print "      PaperSize      = " & vSheetProps(0)
    Debug.Print "      TemplateIn     = " & vSheetProps(1)
    Debug.Print "      Scale1         = " & vSheetProps(2)
    Debug.Print "      scale2         = " & vSheetProps(3)
    Debug.Print "      FirstAngle     = " & vSheetProps(4)
    Debug.Print "      Width          = " & vSheetProps(5)
    Debug.Print "      Height         = " & vSheetProps(6)
```

```
End Sub
```

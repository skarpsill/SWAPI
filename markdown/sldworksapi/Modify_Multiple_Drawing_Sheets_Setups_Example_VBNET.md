---
title: "Modify Multiple Drawing Sheets Setups Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Multiple_Drawing_Sheets_Setups_Example_VBNET.htm"
---

# Modify Multiple Drawing Sheets Setups Example (VB.NET)

This example shows how to modify the setups of multiple drawing sheets.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing and sheet format files exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Sets Sheet1, Sheet2 and Sheet3 drawing sheet formats
'    to portrait.
' 3. Rebuilds the drawing.
' 4. Click each sheet tab, click Zoom to Fit, and examine
'    the sheet.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawing As DrawingDoc
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim sheetNameArray As Object
        Dim sheetNames(1) As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swDrawing = swModel
        sheetNames(0) = "Sheet2"
        sheetNames(1) = "Sheet3"
        sheetNameArray = sheetNames
        swDrawing.SetSheetsSelected(sheetNameArray)
        status = swDrawing.SetupSheet6("Sheet3", swDwgPaperSizes_e.swDwgPapersUserDefined, swDwgTemplates_e.swDwgTemplateCustom, 1, 1, True, "C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\lang\english\sheetformat\a4 - portrait.slddrt", 0.2794, 0.2159, "Default", True, 0, 0, 0, 0, 0, 0)

        swModel.ForceRebuild3(True)
        swModel.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

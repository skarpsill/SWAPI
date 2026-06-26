---
title: "Modify Multiple Drawing Sheets Setups Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Multiple_Drawing_Sheets_Setups_Example_VB.htm"
---

# Modify Multiple Drawing Sheets Setups Example (VBA)

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
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim sheetNameArray As Variant
Dim sheetNames(1) As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swDrawing = swModel
```

```
    sheetNames(0) = "Sheet2"
    sheetNames(1) = "Sheet3"
    sheetNameArray = sheetNames
    swDrawing.SetSheetsSelected (sheetNameArray)
    status = swDrawing.SetupSheet6("Sheet3", swDwgPaperSizes_e.swDwgPapersUserDefined, swDwgTemplates_e.swDwgTemplateCustom, 1, 1, True, "C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\lang\english\sheetformat\a4 - portrait.slddrt", 0.2794, 0.2159, "Default", True, 0, 0, 0, 0, 0, 0)

    swModel.ForceRebuild3 True
    swModel.ViewZoomtofit2
```

```
End Sub
```

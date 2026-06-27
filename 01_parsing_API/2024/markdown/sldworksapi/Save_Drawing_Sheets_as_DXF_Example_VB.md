---
title: "Save Drawing Sheets as DXF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Drawing_Sheets_as_DXF_Example_VB.htm"
---

# Save Drawing Sheets as DXF Example (VBA)

This example shows how to save multiple drawings sheets as DXF files.

```
'----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Verify that C:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Generates a DXF file for each sheet, overwriting any existing file,
'    and bases the names of the DXF files on the sheet names; for example
'    Sheet1 is saved as Sheet1.dxf, Sheet2 is saved as Sheet2.dxf, and so on.
' 2. Examine the Immediate window and C:\temp.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim vSheetName As Variant
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim nRetval As Long
    Dim bShowMap As Boolean
    Dim nNumSheet As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    ' Current settings
    Debug.Print "DxfMapping             = " & swApp.GetUserPreferenceToggle(swDxfMapping)
    Debug.Print "DXFDontShowMap         = " & swApp.GetUserPreferenceToggle(swDXFDontShowMap)
    Debug.Print "DxfVersion             = " & swApp.GetUserPreferenceIntegerValue(swDxfVersion)
    Debug.Print "DxfOutputFonts         = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputFonts)
    Debug.Print "DxfMappingFileIndex    = " & swApp.GetUserPreferenceIntegerValue(swDxfMappingFileIndex)
    Debug.Print "DxfOutputLineStyles    = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputLineStyles)
    Debug.Print "DxfOutputNoScale       = " & swApp.GetUserPreferenceIntegerValue(swDxfOutputNoScale)
    Debug.Print "DxfOutputScaleFactor   = " & swApp.GetUserPreferenceDoubleValue(swDxfOutputScaleFactor)
    Debug.Print "DxfMappingFiles        = " & swApp.GetUserPreferenceStringListValue(swDxfMappingFiles)
    Debug.Print ""
```

```
    ' Turn off showing of map
    swApp.SetUserPreferenceToggle swDXFDontShowMap, True
```

```
    vSheetName = swDraw.GetSheetNames
    For i = 0 To UBound(vSheetName)
        bRet = swDraw.ActivateSheet(vSheetName(i))
        bRet = swModel.SaveAs4("C:\temp\" & vSheetName(i) & ".dxf", swSaveAsCurrentVersion, swSaveAsOptions_Silent, nErrors, nWarnings)
    Next i
    ' Switch back to first sheet
    bRet = swDraw.ActivateSheet(vSheetName(0))
    ' Restore old setting
    swApp.SetUserPreferenceToggle swDXFDontShowMap, bShowMap
```

```
End Sub
```

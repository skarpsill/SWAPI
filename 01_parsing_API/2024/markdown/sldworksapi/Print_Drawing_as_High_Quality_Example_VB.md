---
title: "Print Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Print_Drawing_as_High_Quality_Example_VB.htm"
---

# Print Drawing Example (VBA)

This example shows how to print the active drawing document.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Prints the drawing to your default printer using the
'    specified page setup and print specification.
' 2. Inspect the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'-----------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swPageSetup As SldWorks.PageSetup
 Dim printSpec As SldWorks.PrintSpecification
 Dim drawing As String
 Dim errors As Long
 Dim warnings As Long
 Dim footerTextNumber As String
 Dim footerTextCount As String
 Dim footerText as String

Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     drawing = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
     Set swModel = swApp.OpenDoc6(drawing, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Set up page's footer text
    Set swModelDocExt = swModel.Extension
    swModelDocExt.UsePageSetup = swPageSetupInUse_e.swPageSetupInUse_Document
    Set swPageSetup = swModel.PageSetup
    footerTextNumber = swPageSetup.GetHeaderFooterString(swStandardHeaderFooterPageSetupTexts_e.swHeaderFooterText_PageNumber)
    footerTextCount = swPageSetup.GetHeaderFooterString(swStandardHeaderFooterPageSetupTexts_e.swHeaderFooterText_PageCount)
    footerText = (footerTextNumber & " of " & footerTextCount)
    swPageSetup.CenterFooter = footerText
```

```vb
    'Create a print specification
     Set printSpec = swModelDocExt.GetPrintSpecification
     printSpec.ConvertToHighQuality = True
     printSpec.AddPrintRange 1, 1
     printSpec.FromScale = 1.5
     printSpec.ToScale = 0.5
     printSpec.ScaleMethod = swPrintSelection
     printSpec.PrinterQueue = ""
     printSpec.PrintToFile = False
    Debug.Print "Printing specifications:"
     Debug.Print "  Collate: " & printSpec.Collate
     Debug.Print "  Convert to high quality: " & printSpec.ConvertToHighQuality
     Debug.Print "  Current sheet: " & printSpec.CurrentSheet
     Debug.Print "  From scale: " & printSpec.FromScale
     Debug.Print "  To scale: " & printSpec.ToScale
     Debug.Print "  Number of copies: " & printSpec.NumberOfCopies
     Debug.Print "  Print background: " & printSpec.PrintBackground
     Debug.Print "  Print cross hatch on out-of-date views: " & printSpec.PrintCrossHatchOnOutOfDateViews
     Debug.Print "  Printer queue: " & printSpec.PrinterQueue
     Debug.Print "    File: " & printSpec.PrintFile
     Debug.Print "  Print white items black: " & printSpec.PrintWhiteItemsBlack
     Debug.Print "  Selection as defined in swPrintSelectionScaleFactor_e: " & printSpec.ScaleMethod
     Debug.Print "  Total sheet count: " & printSpec.SheetCount
     Debug.Print "  X origin: " & printSpec.XOrigin
     Debug.Print "  Y origin: " & printSpec.YOrigin
```

```
    ' Print the drawing to your default printer
    swModelDocExt.PrintOut4 "", "", printSpec
```

```vb
    printSpec.RestoreDefaults
     printSpec.ResetPrintRange

End Sub
```

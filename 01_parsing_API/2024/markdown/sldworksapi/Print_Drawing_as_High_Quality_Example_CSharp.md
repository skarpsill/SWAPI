---
title: "Print Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Print_Drawing_as_High_Quality_Example_CSharp.htm"
---

# Print Drawing Example (C#)

This example shows how to print the active drawing document.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Prints the drawing to your default printer using the
//    specified page setup and print specification.
// 2. Inspect the Immediate window.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//-----------------------------------------------------------------
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
namespace PrintSpecification_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        PrintSpecification printSpec;
        PageSetup swPageSetup;
        string drawing;
        int errors;
        int warnings;
        string footerTextNumber;
        string footerTextCount;
        string footerText;

        public void Main()
        {
            drawing = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swModel = swApp.OpenDoc6(drawing, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Set up page's footer text
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swModelDocExt.UsePageSetup = (int)swPageSetupInUse_e.swPageSetupInUse_Document;
            swPageSetup = (PageSetup)swModel.PageSetup;
            footerTextNumber = swPageSetup.GetHeaderFooterString((int)swStandardHeaderFooterPageSetupTexts_e.swHeaderFooterText_PageNumber);
            footerTextCount = swPageSetup.GetHeaderFooterString((int)swStandardHeaderFooterPageSetupTexts_e.swHeaderFooterText_PageCount);
            footerText = (footerTextNumber + " of " + footerTextCount);
            swPageSetup.CenterFooter = footerText;

            //Create a print specification
            printSpec = (PrintSpecification)swModelDocExt.GetPrintSpecification();
            printSpec.ConvertToHighQuality = true;
            printSpec.AddPrintRange(1, 1);
            printSpec.FromScale = 1.5;
            printSpec.ToScale = 0.5;
            printSpec.ScaleMethod = (int)swPrintSelectionScaleFactor_e.swPrintSelection;
            printSpec.PrinterQueue = "";
            printSpec.PrintToFile = false;

            Debug.Print("Printing specifications:");
            Debug.Print("  Collate: " + printSpec.Collate);
            Debug.Print("  Convert to high quality: " + printSpec.ConvertToHighQuality);
            Debug.Print("  Current sheet: " + printSpec.CurrentSheet);
            Debug.Print("  From scale: " + printSpec.FromScale);
            Debug.Print("  To scale: " + printSpec.ToScale);
            Debug.Print("  Number of copies: " + printSpec.NumberOfCopies);
            Debug.Print("  Print background: " + printSpec.PrintBackground);
            Debug.Print("  Print cross hatch on out-of-date views: " + printSpec.PrintCrossHatchOnOutOfDateViews);
            Debug.Print("  Printer queue: " + printSpec.PrinterQueue);
            Debug.Print("  Print white items black: " + printSpec.PrintWhiteItemsBlack);
            Debug.Print("  Selection as defined in swPrintSelectionScaleFactor_e: " + printSpec.ScaleMethod);
            Debug.Print("  Total sheet count: " + printSpec.SheetCount);
            Debug.Print("  X origin: " + printSpec.XOrigin);
            Debug.Print("  Y origin: " + printSpec.YOrigin);

            //Print the drawing to your default printer
            swModelDocExt.PrintOut4("", "", printSpec);

            printSpec.RestoreDefaults();
            printSpec.ResetPrintRange();

        }

        public SldWorks swApp;

    }

}
```

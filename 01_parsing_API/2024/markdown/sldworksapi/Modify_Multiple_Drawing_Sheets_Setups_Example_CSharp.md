---
title: "Modify Multiple Drawing Sheets Setups Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Multiple_Drawing_Sheets_Setups_Example_CSharp.htm"
---

# Modify Multiple Drawing Sheets Setups Example (C#)

This example shows how to modify the setups of multiple drawing sheets.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that the drawing and sheet format files exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Sets Sheet1, Sheet2 and Sheet3 drawing sheet formats
//    to portrait.
// 3. Rebuilds the drawing.
// 4. Click each sheet tab, click Zoom to Fit, and examine
//    the sheet.
//
// NOTE: Because the drawing is used elsewhere, do not
// save changes.
//---------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            object sheetNameArray = null;
            string[] sheetNames = new string[2];

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swDrawing = (DrawingDoc)swModel;
            sheetNames[0] = "Sheet2";
            sheetNames[1] = "Sheet3";
            sheetNameArray = sheetNames;
            swDrawing.SetSheetsSelected(sheetNameArray);
            status = swDrawing.SetupSheet6("Sheet3", (int)swDwgPaperSizes_e.swDwgPapersUserDefined, (int)swDwgTemplates_e.swDwgTemplateCustom, 1, 1, true, "C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2017\\lang\\english\\sheetformat\\a4 - portrait.slddrt", 0.2794, 0.2159, "Default",
            true, 0, 0, 0, 0, 0, 0);

            swModel.ForceRebuild3(true);
            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

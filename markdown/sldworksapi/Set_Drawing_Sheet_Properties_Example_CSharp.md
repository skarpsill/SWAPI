---
title: "Set Drawing Sheet Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Drawing_Sheet_Properties_Example_CSharp.htm"
---

# Set Drawing Sheet Properties Example (C#)

This example shows how to set the properties of a drawing sheet.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Create a new drawing document.
// 2. Add another sheet to the drawing.
// 3. Select the Tools > Options > Document Properties >
//    Drawing Sheets > Use custom property values from the sheet
//    check box if it is not selected.
// 4. Right-click Sheet2, click Properties, clear the Same as sheet
//    specified in Document Properties check box if it is selected, and
//    click OK to close the Sheet Properties dialog.
//
// Postconditions:
// 1. Selects the Same as sheet specified in Document Properties
//    check box on the Sheet Properties dialog.
// 2. Right-click Sheet2 and click Properties to verify step 1.
//-----------------------------------------------------------------
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
            DrawingDoc swDrawing = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            double[] sheetProperties = null;

            swDrawing = (DrawingDoc)swApp.ActiveDoc;

            // Active sheet is Sheet2
            swSheet = (Sheet)swDrawing.GetCurrentSheet();
            sheetProperties = (double[])swSheet.GetProperties2();
            int prop1;
            int prop2;
            bool prop5;
            bool prop8;
            prop1 = (int)System.Convert.ToInt32(sheetProperties[0]);
            prop2 = (int)System.Convert.ToInt32(sheetProperties[1]);
            prop5 = (bool)System.Convert.ToBoolean(sheetProperties[4]);
            prop8 = (bool)System.Convert.ToBoolean(sheetProperties[7]);
            prop8 = true;
            swSheet.SetProperties2(prop1, prop2, sheetProperties[2], sheetProperties[3], prop5, sheetProperties[5], sheetProperties[6], prop8);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

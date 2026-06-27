---
title: "Get Loaded Sheets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_CSharp.htm"
---

# Get Loaded Sheets Example (C#)

This example shows how to determine which sheets in a drawing are loaded.

```
//----------------------------------------------
// Preconditions:
// 1. Click File > Open.
// 2. Browse to public_documents\samples\tutorial\advdrawings.
// 3. Select foodprocessor.slddrw.
// 4. Click Select sheets to open > Selected > Sheet1* (Load) > OK > Open.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Loads Sheet1 only.
// 2. Mouse over the Sheet2, Sheet3, and Sheet4 tabs and
//    examine the Immediate window to verify step 1.
//
// NOTE: Because this drawing is used elsewhere, do not save
// changes.
//----------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace IsLoadedSheetCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DrawingDoc swDraw = default(DrawingDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vSheetName = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool bRet = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sheetName;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDraw = (DrawingDoc)swModel;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the sheets in the drawing document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vSheetName = (object[])swDraw.GetSheetNames();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Traverse the sheets and determine whether
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// they're loaded
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i < vSheetName.Length; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}sheetName = (string)vSheetName[i];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bRet = swDraw.ActivateSheet(sheetName);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Sheet swSheet = default(Sheet);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swSheet = (Sheet)swDraw.GetCurrentSheet();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((swSheet.IsLoaded()))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(vSheetName[i] + " is loaded.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(vSheetName[i] + " is not loaded.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

---
title: "Get Text Items in GTol Frame Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Text_Items_in_GTol_Frame_Example_CSharp.htm"
---

# Get Text Items in GTol Frame Example (C#)

```vb
This example shows how to get text items, values, and symbols in a GTol frame.
```

```
//-------------------------------------------------------------
// Preconditions:
// 1. Open document with a GTol frame and select that GTol
//    frame.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the text items, values, and symbols in the
//    selected GTol frame.
// 2. Examine the Immediate window.
//-------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            SelectionMgr swSelMgr;
            Gtol swGtol;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swGtol = (Gtol)swSelMgr.GetSelectedObject6(1, -1);

            Debug.Print("GetTextCount = " + swGtol.GetTextCount().ToString());

            for (int idx = 0; idx < swGtol.GetTextCount(); idx++)
            {
                Debug.Print("GetTextAtIndex(" + idx.ToString() + ") = " + swGtol.GetTextAtIndex(idx));
            }
            int count = 0;
            count = swGtol.GetFrameCount();
            count = count - 1;
            Debug.Print("GetFrameCount = " + count.ToString());
            for (int idx = 1; idx <= (swGtol.GetFrameCount() - 1); idx++)
            {
                Object myParams;
                Object mySymbols;
                myParams = swGtol.GetFrameValues((short)idx);
                if (myParams != null)
                {
                    Array myParamArray = (Array)myParams;
                    Debug.Print("GetFrameValues(" + idx.ToString() + ") = " + myParamArray.GetValue(0) + "," + myParamArray.GetValue(1) + "," + myParamArray.GetValue(2) + "," + myParamArray.GetValue(3) + "," + myParamArray.GetValue(4));
                    mySymbols = swGtol.GetFrameSymbols3((short)idx);
                    Array mySymbolsArray = (Array)mySymbols;
                    Debug.Print("  GetFrameSymbols3(" + idx.ToString() + ") = " + mySymbolsArray.GetValue(0) + "," + mySymbolsArray.GetValue(1) + "," + mySymbolsArray.GetValue(2) + "," + mySymbolsArray.GetValue(3) + "," + mySymbolsArray.GetValue(4) + "," + mySymbolsArray.GetValue(5));

                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

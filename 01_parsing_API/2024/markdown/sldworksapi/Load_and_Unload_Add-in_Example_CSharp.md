---
title: "Load and Unload Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Load_and_Unload_Add-in_Example_CSharp.htm"
---

# Load and Unload Add-in Example (C#)

This example shows how to prompt the user to load or unload an add-in.

```
//---------------------------------------------
// Preconditions:
// 1. Create a C# add-in in Microsoft Visual Studio
//    2010, or later, in C:\test, following the instructions in
//    Add Shortcut Menu to Add-ins Example (C#).
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Click Yes to load SwCSharpAddin1 or click No to unload
//    SwCSharpAddin1.
// 2. Examine the Immediate window.
//---------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Windows.Forms;
using System.Diagnostics;

namespace LoadUnloadAddinsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            //Path to add-in
            const string sAddinName = "C:\\test\\SwCSharpAddin1\\SwCSharpAddin1\\bin\\Debug\\SwCSharpAddin1.dll";
            int status = 0;

            if (MessageBox.Show("Load add-in?", "Add-ins load/unload", MessageBoxButtons.YesNo) == System.Windows.Forms.DialogResult.Yes)
            {
                Debug.Print("Loading: " + sAddinName);
                status = swApp.LoadAddIn(sAddinName);
            }
            else
            {
                Debug.Print("Unloading: " + sAddinName);
                status = swApp.UnloadAddIn(sAddinName);
            }

            Debug.Print("  Status = " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Rebuild All Features in All Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_All_Features_in_All_Configurations_Example_CSharp.htm"
---

# Rebuild All Features in All Configurations Example (C#)

This example shows how to rebuild all features in all configurations without activating each configuration.

```
//------------------------------------------------------------
// Preconditions:
// 1. Copy public_documents\samples\tutorial\PDMWorks to c:\temp.
// 2. Open c:\temp\membrane.sldprt.
//    a. Expand Revolve-Thin1, click Sketch1 > Edit Sketch.
//    b. Click R30 and change 30 to 60.
//    c. Click File > Save All > Rebuild and save document
//       (recommended).
//    d. Click File > Close.
// 3. Open c:\temp\speaker.sldasm.
// 4. Click Don't rebuild.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Rebuilds all features in all configurations without
//    activating each configuration.
// 2. Examine the Immediate window.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        bool bRebuild;
        int ret;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            ret = swModelDocExt.NeedsRebuild2;
            Debug.Print("Features need to be rebuilt (1 = needs rebuild)? " + ret);

            if (ret == 1)
            {
                bRebuild = swModelDocExt.ForceRebuildAll();
                Debug.Print("    All features rebuilt in all configurations without activating each configuration? " + bRebuild);
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

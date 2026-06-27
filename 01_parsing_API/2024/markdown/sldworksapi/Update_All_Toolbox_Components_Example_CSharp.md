---
title: "Update All Toolbox Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_All_Toolbox_Components_Example_CSharp.htm"
---

# Update All Toolbox Components Example (C#)

This example shows how to update all SOLIDWORKS Toolbox components in an assembly.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Updates all SOLIDWORKS Toolbox components in the assembly.
// 2. Examine the Immediate window.
//
// NOTE: Because this assembly is used elsewhere, do not save
// changes.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1.CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            int errors = 0;
            int warnings = 0;
            int updateToolboxComponents = 0;

            // Open the assembly
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\toolbox\\lens_mount.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssembly = (AssemblyDoc)swModel;

            // Update all SOLIDWORKS Toolbox components in the assembly
            updateToolboxComponents = swAssembly.UpdateToolboxComponent((int)swAssemblyLevelToUpdate_e.swAssemblyLevelToUpdate_AllLevels);
            Debug.Print("Update SOLIDWORKS Toolbox components status: " + updateToolboxComponents);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

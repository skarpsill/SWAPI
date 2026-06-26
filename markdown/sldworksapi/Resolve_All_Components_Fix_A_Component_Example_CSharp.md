---
title: "Resolve All Lightweight Components and Fix a Component (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Resolve_All_Components_Fix_A_Component_Example_CSharp.htm"
---

# Resolve All Lightweight Components and Fix a Component (C#)

This example shows how to:

- resolve all lightweight components
- fix a component

in the an assembly.

```
//-----------------------------------
// Preconditions:
// 1. Specified file to open exists.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Resolves all lightweight components
//    in the assembly.
// 2. Fixes the selected component.
// 3. Examine the Immediate window to verify.
//
// NOTE: Because this assembly is used elsewhere,
// do not save any changes when closing it.
//-------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ResolveLightWeightFixAssemblyCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            AssemblyDoc swAssy;
            ModelDocExtension swModelDocExt;
            Component2 swComp;
            SelectionMgr swSelMgr;
            string fileName;
            int errors = 0;
            int warnings = 0;
            bool status;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\key pad_1.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssy = (AssemblyDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            // Resolve all lightweight components
            errors = swAssy.ResolveAllLightWeightComponents(true);
            Debug.Print("All lightweight components resolved (0 = All components resolved)? " + errors);

            // Fix the selected component
            status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swAssy.FixComponent();
            status = swModelDocExt.SelectByID2("Pad_1-1@key pad_1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1);
            Debug.Print("Selected component fixed? " + swComp.IsFixed());

            /// <summary>
            /// The SldWorks swApp variable is pre-assigned for you.
            /// </summary>

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

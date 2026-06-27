---
title: "Fire Notification After Adding a Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_After_Adding_a_Mate_Example_CSharp.htm"
---

# Fire Notification After Adding a Mate Example (C#)

This example shows how to fire a post-notify event when adding mates.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open exists.
// 2. Click Tools > Options > clear the Stop VSTA debugger
//    on macro exit check box if it is selected.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Interactively add a mate between two entities
//    (Click Insert > Mate). For example, add a lock mate
//    between the toaster base and the cup.
// 3. Adds a mate between the selected entities.
// 4. Examine the Immediate window.
// 5. Click Debug > Stop Debugging in SOLIDWORKS Visual
//    Studio Tools for Applications.
// 6. Click Tools > Options > Stop VSTA debugger on macro exit
//    check box in SOLIDWORKS.
//
// NOTE: Because this assembly is used elsewhere, do not save
// changes.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Collections;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public AssemblyDoc swAssem;

        public void Main()
        {

            ModelDoc2 swModel;
            int errors = 0;
            int warnings = 0;
            Hashtable openAssem;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\toaster_scene.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Set up events
            swAssem = (AssemblyDoc)swModel;
            openAssem = new Hashtable();
            AttachEventHandlers();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {

            swAssem.AddMatePostNotify2 += this.swAssem_AddMatePostNotify2;
        }

        private int swAssem_AddMatePostNotify2(ref object mates)
        {
            Debug.Print("One or more mates were added to the assembly.");
            return 1;
        }
    }
}
```

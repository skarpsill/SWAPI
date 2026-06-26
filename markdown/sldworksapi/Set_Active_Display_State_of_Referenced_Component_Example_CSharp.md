---
title: "Set Display State of Referenced Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Active_Display_State_of_Referenced_Component_Example_CSharp.htm"
---

# Set Display State of Referenced Component Example (C#)

## Set Active Display State of Referenced Component Example (C#)

This example shows how to set the active display state of a referenced component.

```
//--------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects leg<1>.
// 2. Gets the selected referenced component's active display state.
// 3. Sets the selected referenced component's active display state.
// 4. Examine the Immediate window, FeatureManager design tree,
//    and graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not
// save changes.
//---------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            Component2 swComponent = default(Component2);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExtension = (ModelDocExtension)swModel.Extension;
            status = swModelDocExtension.SelectByID2("leg-1@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swComponent = (Component2)swSelectionManager.GetSelectedObjectsComponent4(1, -1);
            Debug.Print("Get active display state: " + swComponent.ReferencedDisplayState2);
            swComponent.ReferencedDisplayState2 = "<Default<As Machined>>_Display State 1";
            Debug.Print("Set active display state: " + swComponent.ReferencedDisplayState2);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

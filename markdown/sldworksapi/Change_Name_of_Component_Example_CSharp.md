---
title: "Change Name of Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Name_of_Component_Example_CSharp.htm"
---

# Change Name of Component Example (C#)

This example shows how to change the name of a component.

```
//-------------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Select a component in the assembly.
// 3. Open the Immediate window.
// 4. Press F5.
//
// Postconditions:
// 1. The selected component's name is
//    changed to SW.
// 2. Examine the Immediate window and
//    FeatureManager design tree to verify.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ComponentName2CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swComp = default(Component2);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent3(1, 0);
            if (swComp == null)
            {
                Debug.Print("Select a component and run the macro again.");
                return;

            }
            else
            {
                // swUserPreferenceToggle_e.swExtRefUpdateCompNames must be set to
                // false to change the name of a component using IComponent2::Name2
                swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swExtRefUpdateCompNames, false);

                // Print original name of component
                Debug.Print("  Original name of component = " + swComp.Name2);

                // Change name of component
                swComp.Name2 = "SW";

                // Print new name of component
                Debug.Print("  New name of component      = " + swComp.Name2);
            }
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```

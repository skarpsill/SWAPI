---
title: "Replace Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Component_Example_CSharp.htm"
---

# Replace Component Example (C#)

This example shows how to replace all instances of a component with a different component.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\assem1.sldasm.
// 2. Select testpart1<1> in the FeatureManager design tree.
// 3. Verify that the specified part exists.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Replaces all instances of the selected component with the
//    specified replacement component.
// 2. Examine the Immediate window, FeatureManager design tree,
//    and assembly.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
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
            const string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swSelComp = default(Component2);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelComp = (Component2)swSelMgr.GetSelectedObjectsComponent4(1, -1);
            Debug.Print("Old component = " + swSelComp.Name2);
            status = swAssy.ReplaceComponents2(fileName, "", true, 0, true);
            Debug.Print("Replacement component = " + swSelComp.Name2);
            Debug.Print("All instances of old component replaced? " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

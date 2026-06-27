---
title: "Disable Equation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Equation_Example_CSharp.htm"
---

# Disable Equation Example (C#)

This example shows how to disable an equation.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\partequations.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Disables an equation.
// 2. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//------------------------------------------------------------------

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
            ModelDoc2 swModel = default(ModelDoc2);
            EquationMgr swEqnMgr = default(EquationMgr);
            int i = 0;
            int count = 0;
            int disabledCount = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swEqnMgr = (EquationMgr)swModel.GetEquationMgr();
            count = swEqnMgr.GetCount();
            Debug.Print("Number of equations in part = " + count);
            for (i = 0; i < count; i++)
            {
                Debug.Print("  Eqn(" + i + ")  = " + swEqnMgr.get_Equation(i));
            }

            Debug.Print("");

            disabledCount = swEqnMgr.GetDisabledEquationCount();
            Debug.Print("Number of disabled equations in part before running macro = " + disabledCount);

            swEqnMgr.set_Disabled((count - 1), true);
            Debug.Print("Eqn(" + (count - 1) + ") disabled? " + swEqnMgr.get_Disabled(count - 1));

            disabledCount = swEqnMgr.GetDisabledEquationCount();
            Debug.Print("Number of disabled equations in part after running macro = " + disabledCount);

            Debug.Print("");

            count = swEqnMgr.GetCount();
            Debug.Print("Number of equations in part = " + count);
            for (i = 0; i < count; i++)
            {
                Debug.Print("  Eqn(" + i + ")  = " + swEqnMgr.get_Equation(i));
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

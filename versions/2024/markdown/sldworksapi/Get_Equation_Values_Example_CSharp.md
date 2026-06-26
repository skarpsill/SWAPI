---
title: "Get Equation Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Equation_Values_Example_CSharp.htm"
---

# Get Equation Values Example (C#)

This example shows how to get the values of equations.

```
//-----------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\partequations.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets each equation's value and index and whether the
//    equation is a global variable.
// 2. Examine the Immediate window.
//------------------------------------------
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
            int nCount = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swEqnMgr = (EquationMgr)swModel.GetEquationMgr();
            Debug.Print("File = " + swModel.GetPathName());
            nCount = swEqnMgr.GetCount();
            for (i = 0; i < nCount; i++)
            {
                Debug.Print("  Equation(" + i + ")  = " + swEqnMgr.get_Equation(i));
                Debug.Print("    Value = " + swEqnMgr.get_Value(i));
                Debug.Print("    Index = " + swEqnMgr.Status);
                Debug.Print("    Global variable? " + swEqnMgr.get_GlobalVariable(i));
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

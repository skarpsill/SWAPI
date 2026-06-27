---
title: "Repair Mates Missing Same Mate Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Repair_Mates_Missing_Same_Mate_Entity_Example_CSharp.htm"
---

# Repair Mates Missing Same Mate Entity Example (C#)

This example shows how to repair all mates missing the same mate entity.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\RepairAssemMates.sldasm.
// 2. Click Close.
//
// Postconditions:
// 1. Selects the Concentric1 mate.
// 2. Selects a face on BoltHolder<1> and a face on Bolt<1>.
// 3. Edits and repairs all mates missing the same mate entity.
// 4. Examine the FeatureManager design tree.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            bool status = false;
            int errors = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swAssembly = (AssemblyDoc)swModel;

            status = swModelDocExt.SelectByID2("Concentric1", "MATE", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0562994754449733, -0.000769308980977712, 0.0081518960735707, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0516662570718722, 0.0153992319276881, 0.0199034517498262, true, 1, null, 0);
            swAssembly.EditMate4((int)swMateType_e.swMateCONCENTRIC, (int)swMateAlign_e.swMateAlignALIGNED, false, 0.001, 0.001, 0.001, 0.001, 0.001, 0, 0.5235987755983,
            0.5235987755983, false, false, 0, true, out errors);
            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

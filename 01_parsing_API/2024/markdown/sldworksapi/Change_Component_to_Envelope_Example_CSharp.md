---
title: "Change Component to Envelope Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Component_to_Envelope_Example_CSharp.htm"
---

# Change Component to Envelope Example (C#)

This example shows how to change a component to an envelope.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects the shaft washer-4 component.
// 3. Gets whether the component is an envelope.
// 4. Changes the component to an envelope.
// 5. Gets whether the component is an envelope.
// 6. Examine the Immediate window and FeatureManager design tree.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-------------------------------------------------------------------
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
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            Component2 swComponent = default(Component2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\98food processor.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select shaft washer-4 component
            swModelDocExtension = (ModelDocExtension)swModel.Extension;
            status = swModelDocExtension.SelectByID2("shaft washer-4@98food processor", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swComponent = (Component2)swSelectionMgr.GetSelectedObjectsComponent4(1, -1);

            //Get whether selected component is an envelope
            Debug.Print("Before calling IAssemblyDoc::CompConfigProperties5:");
            Debug.Print("   Is component an envelope? " + swComponent.IsEnvelope());

            //Change the selected component to an envelope
            swAssembly = (AssemblyDoc)swModel;
            status = swAssembly.CompConfigProperties6((int)swComponentSuppressionState_e.swComponentFullyResolved, (int)swComponentSolvingOption_e.swComponentRigidSolving, true, true, "Default", false, true, (int)swASMSLDPRTCompPref_e.swAlwaysInclude);

            //Get whether the selected component is an envelope
            Debug.Print("After calling IAssemblyDoc::CompConfigProperties5:");
            Debug.Print("  Is component an envelope? " + swComponent.IsEnvelope());

            swModel.EditRebuild3();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

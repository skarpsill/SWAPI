---
title: "Specify Order of Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Specify_Order_of_Configurations_Example_CSharp.htm"
---

# Specify Order of Configurations Example (C#)

This example shows how to specify the order in which to list configurations in the ConfigurationManager.

```
//-------------------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
// 2. Click the ConfigurationManager tab and examine the order in which the
//    configurations are listed.
//
// Preconditions:
// 1. Lists the configurations in the specified order.
// 2. Examine the ConfigurationManager tab.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//-------------------------------------------------------------------------------------
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
            ConfigurationManager swConfigMgr = default(ConfigurationManager);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfigMgr.SortConfigurationTree((int)swConfigTreeSortType_e.swSortType_Literal);
            swModel.EditRebuild3();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

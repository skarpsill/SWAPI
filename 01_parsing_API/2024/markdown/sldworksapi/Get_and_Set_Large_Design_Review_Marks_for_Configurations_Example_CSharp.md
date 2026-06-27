---
title: "Get and Set Large Design Review Marks for Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_CSharp.htm"
---

# Get and Set Large Design Review Marks for Configurations Example (C#)

This example shows how to get and set the Large Design Review marks for all of the configurations in an assembly.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the current Large Design Review marks for all configurations.
// 2. Sets the Large Design Review marks for all configurations to true.
// 3. Gets the modified Large Design Review marks for all configurations.
// 4. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
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
            Configuration swConf = default(Configuration);
            ConfigurationManager swConfMgr = default(ConfigurationManager);
            string[] configNameArr = null;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swConfMgr = (ConfigurationManager)swModel.ConfigurationManager;
            configNameArr = (string[])swModel.GetConfigurationNames();

            //Get current Large Design Review marks for all configurations
            Debug.Print("Current Large Design Review marks for configurations:");
            foreach (string configName in configNameArr)
            {
                swConf = (Configuration)swModel.GetConfigurationByName(configName);
                Debug.Print("  " + configName + ": " + swConf.LargeDesignReviewMark);
            }

            //Set Large Design Review marks for all configurations to true
            foreach (string configName in configNameArr)
            {
                swConf = (Configuration)swModel.GetConfigurationByName(configName);
                swConf.LargeDesignReviewMark = true;
            }

            //Get modified Large Design Review marks for all configurations
            Debug.Print("Modified Large Design Review marks for configurations:");
            foreach (string configName in configNameArr)
            {
                swConf = (Configuration)swModel.GetConfigurationByName(configName);
                Debug.Print("  " + configName + ": " + swConf.LargeDesignReviewMark);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

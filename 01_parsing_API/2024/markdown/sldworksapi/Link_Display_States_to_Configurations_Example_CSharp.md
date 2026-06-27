---
title: "Link Display States to Configurations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Link_Display_States_to_Configurations_Example_CSharp.htm"
---

# Link Display States to Configurations Example (C#)

This example shows how to link and unlink display states to and from configurations.

```vb
// ---------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets and sets whether display states are linked to the
 //    active configuration.
 // 2. Closes the assembly document without saving
 //    any changes.
 //-----------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace LinkDisplayStatesToConfigurationCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ConfigurationManager swConfigMgr =  default(ConfigurationManager);
             string assemblyName = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             Debug.Print("");

             swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
             swConfigMgr.LinkDisplayStatesToConfigurations =  false;
             Debug.Print("Are display states linked to configurations? " + swConfigMgr.LinkDisplayStatesToConfigurations);
             if (!swConfigMgr.LinkDisplayStatesToConfigurations)
             {
                 Debug.Print("All display states are available to the active configuration.");
             }

             swConfigMgr.LinkDisplayStatesToConfigurations = true;
             Debug.Print("Are display states linked configurations? " + swConfigMgr.LinkDisplayStatesToConfigurations);
             if (swConfigMgr.LinkDisplayStatesToConfigurations)
             {
                 Debug.Print("All display states are not available to the active configuration.");
             }

             assemblyName = swModel.GetTitle();
             swApp.QuitDoc(assemblyName);
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

---
title: "Get Explode Step Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Explode_Step_Example_CSharp.htm"
---

# Get Explode Step Example (C#)

This example shows how to get an explode step and its properties.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document with an explode view.
// 2. Open an Immediate window.
//
// Postconditions:
// 1. Gets the first explode step.
// 2. Examine the Immediate window.
//---------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace ExplodeStepCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ConfigurationManager swConfigurationMgr = default(ConfigurationManager);
            Configuration swConfiguration = default(Configuration);
            ExplodeStep swExplodeStep = default(ExplodeStep);

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get explode step
            swConfigurationMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfiguration = (Configuration)swConfigurationMgr.ActiveConfiguration;
            swExplodeStep = (ExplodeStep)swConfiguration.GetExplodeStep(0);
            Debug.Print("Name of explode step: " + swExplodeStep.Name);
            Debug.Print("Number of components that move in this explode step: " + swExplodeStep.GetNumOfComponents());
            Debug.Print("Is the sub-assembly rigid? " + swExplodeStep.IsSubAssemblyRigid());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

---
title: "Get Whether Components Are Loaded Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Components_Are_Loaded_Example_CSharp.htm"
---

# Get Whether Components Are Loaded Example (C#)

This example gets whether the components in an assembly document are
loaded.

```vb
//---------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Loads the Magnet-1 component.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this assembly document is used elsewhere,
 // kadov_tag{{<spaces>}}do not save changes.
 //---------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace IsLoadedComponent2CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DocumentSpecification swDocSpecification;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string[] sComponents = new string[1];
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] Components;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Component2 swComponent = default(Component2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string sName;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AssemblyDoc swAssembly;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int longstatus;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int longwarnings;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int i;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ConfigurationManager swConfigMgr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Configuration swConfig;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Selectively open speaker.sldasm
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Load only Magnet-1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\pdmworks\\speaker.sldasm");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sComponents[0] = "Magnet-1@speaker";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Components = (object[])sComponents;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.ComponentList = Components;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.Selective = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sName = swDocSpecification.FileName;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.DisplayState = "Default_Display State-1";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.UseLightWeightDefault = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.LightWeight = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.Silent = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDocSpecification.IgnoreHiddenComponents = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.OpenDoc7(swDocSpecification);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}longstatus = swDocSpecification.Error;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}longwarnings = swDocSpecification.Warning;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Get whether the components in the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// assembly document are loaded and suppressed; only
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Magnet-1 should be loaded and not suppressed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly = (AssemblyDoc)swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfig = (Configuration)swConfigMgr.ActiveConfiguration;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Components = (object[])swAssembly.GetComponents(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}for (i = 0; i < Components.Length; i++)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swComponent = (Component2)Components[i];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swComponent.IsLoaded()))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component: " + swComponent.Name + " is loaded.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component: " + swComponent.Name + " is not loaded.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print (" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Suppressed: " + swConfig.GetComponentSuppressionState(swComponent.Name));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print ("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

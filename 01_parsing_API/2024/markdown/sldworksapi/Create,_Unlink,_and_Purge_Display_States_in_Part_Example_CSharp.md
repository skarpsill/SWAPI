---
title: "Create, Unlink, and Purge Display States in Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm"
---

# Create, Unlink, and Purge Display States in Part Example (C#)

This example shows how to create, unlink, and purge display states in
a part document.

```
//---------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\multibody\multi-inter.sldprt,
//    whose Default configuration has two display states:
//    * PhotoWorks Display
//    * Display State 1
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates and unlinks Display State 2.
// 2. Attempts to purge any display states identical to
//    Display State 2.
// 3. Closes the part document without saving any changes.
// 4. Examine the Immediate window.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace AddAndPurgeDisplayStates_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial
 class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc swPart;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public
 void Main()
```

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Configuration swConfig = default(Configuration);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string modelName = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get Default configuration and create a display state
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swConfig = (Configuration)swModel.GetConfigurationByName("Default");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swConfig.CreateDisplayState("Display State 2");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (boolstatus) Debug.Print("Display State 2 created.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If display is linked, unlink it
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Is Display State 2 linked? " + swModelDocExt.LinkedDisplayState);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt.LinkedDisplayState = false;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Is Display State 2 still linked? " + swModelDocExt.LinkedDisplayState);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Purge any display states identical to Display State 2
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.PurgeDisplayState();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Identical display states to Display State 2 purged? " + boolstatus);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Close the part without saving changes
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelName = swModel.GetTitle();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.QuitDoc(modelName);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

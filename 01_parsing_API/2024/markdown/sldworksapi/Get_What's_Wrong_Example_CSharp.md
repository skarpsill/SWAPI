---
title: "Get What's Wrong Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_What's_Wrong_Example_CSharp.htm"
---

# Get What's Wrong Example (C#)

This example shows how to get the What's Wrong information for a document.

```vb
//-----------------------------------
//
// Preconditions: Model document is active. Examine the Immediate
// kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}window after running this macro to see the What's Wrong
// kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}items in the model document.
//
// Postconditions: None
//
//------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace GetWhatsWrongCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object oFeatures;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object oErrorCodes;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object oWarnings;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] Features = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int[] ErrorCodes = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool[] Warnings = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int nbrWhatsWrong = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrWhatsWrong = swModelDocExt.GetWhatsWrongCount();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Number of What's Wrong items: " + nbrWhatsWrong);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (nbrWhatsWrong > 0) {
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.GetWhatsWrong(out oFeatures, out oErrorCodes, out oWarnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Features = (object[])oFeatures;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ErrorCodes = (int[])oErrorCodes;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Warnings = (bool[])oWarnings;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i < Features.Length; i++) {
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFeature = (Feature)Features[i];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Name of feature: " + swFeature.GetTypeName2());
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Error: " + ErrorCodes[i]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Did SOLIDWORKS flag this item as a warning ? " + Warnings[i]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}else {
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("No What's Wrong items.");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

---
title: "Get Hidden Components Filenames Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hidden_Components_Filenames_Example_CSharp.htm"
---

# Get Hidden Components Filenames Example (C#)

This example shows how to get the filenames of the hidden components in an
assembly.

```
//-----------------------------------------------------------
// Preconditions:
// 1. In SOLIDWORKS, click File > Open, and browse to
//    public_documents\samples\tutorial\routing-pipes.
// 2. Click ball valve with flanges.sldasm > Mode >
//    Large Design Review > Open > OK.
//
//    NOTE: If the path to the Design Library does not exist,
//    then multiple dialogs informing you that SOLIDWORKS is unable
//    to locate might be displayed some components. Click No or OK
//    to close these dialogs.
//
// 3. Click ball valve-1 in the FeatureManager design tree
//    and click Selective Open > Selective Open > Selected components >
//    Open Selected > OK.
//
//    NOTE: Only the selected components are loaded. Components
//    not selected are not loaded and not visible in the
//    SOLIDWORKS graphics area.
//
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Does not load the slip on weld flange components because
//    they are hidden.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because this assembly elsewhere, do not save changes.
//-----------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
namespace Macro1.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AssemblyDoc swAssembly;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Boolean boolStatus;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssembly = (AssemblyDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolStatus = swAssembly.HasUnloadedComponents();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (boolStatus == true)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object oPaths = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object oRefdConfigs = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object oReasons = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object oDocTypes = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object oNames = null;

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}oNames = swAssembly.GetUnloadedComponentNames(out oPaths, out oRefdConfigs, out oReasons, out oDocTypes);

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}string[] Paths = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}string[] RefdConfigs = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}int[] Reasons = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}int[] DocTypes = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}string[] Names = null;

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Paths = (string[])oPaths;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}RefdConfigs = (string[]) oRefdConfigs;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Reasons = (int[]) oReasons;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}DocTypes =(int[]) oDocTypes;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Names = (string[]) oNames;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (!(Paths is System.Array) & (RefdConfigs is System.Array) & (Reasons is System.Array) & (DocTypes is System.Array) & (Names is System.Array))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}MessageBox.Show("Error: Non-array parameter!");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Assert(false);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((Paths.Length != RefdConfigs.Length) | (Paths.Length != Reasons.Length) | (Paths.Length != DocTypes.Length) | (Paths.Length != Names.Length))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}MessageBox.Show("Error: Lengths of the arrays do not match!");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Assert(false);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (int index = 0; index < Paths.Length; index++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}string debugMessage = null;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}debugMessage = index + ": ";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swDocumentTypes_e eDocType;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}eDocType = (swDocumentTypes_e)(DocTypes[index]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}switch (eDocType)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case swDocumentTypes_e.swDocNONE:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The document ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case swDocumentTypes_e.swDocPART:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The part ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case swDocumentTypes_e.swDocASSEMBLY:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The assembly ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case swDocumentTypes_e.swDocDRAWING:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The drawing ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}case swDocumentTypes_e.swDocSDM:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The SDM ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}default:
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}debugMessage = debugMessage + "The document is an unknown type ";
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}debugMessage = debugMessage + Paths[index] + " was not loaded because it is ";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bool bUnloadedBecauseHidden = false;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (Reasons[index] == 1)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}bUnloadedBecauseHidden = true;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}bUnloadedBecauseHidden = false;

kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (bUnloadedBecauseHidden)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage + "hidden.";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}debugMessage = debugMessage + "suppressed.";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(debugMessage);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

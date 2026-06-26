---
title: "Get Whether Component Is Envelope And Excluded From BOM (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm"
---

# Get Whether Component Is Envelope And Excluded From BOM (C#)

This example shows how to find out if a component is an envelope and
whether the component is included in the bill of materials (BOM).

```vb
 //---------------------------------------------------------------------------
// Preconditions: kadov_tag{{<spaces>}}
// 1. Open SOLIDWORKS and copy the code below to a C# macro.
// 2. Ensure that the kadov_tag{{</spaces>}} specified file exists.
// 3. Specify your_license_key.
// 4. Open an Immediate window.
//
// Postconditions: Inspect the Immediate window.
//
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTE: ISwDMComponent5::ExcludeFromBom and ISwDMComponent5::IsEnvelope print
// kadov_tag{{</spaces>}}to the Immediate Window for each component.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using SwDocumentMgr;
using System.Diagnostics;
namespace ExampleCS.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDMClassFactory swClassFact;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDMApplication swDocMgr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDMDocument7 swDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDMConfigurationMgr swCfgMgr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMConfiguration7 swConfiguration7;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sDocFileName;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDmDocumentType nDocType;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDocumentMgr.SwDmDocumentOpenError nRetVal;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sLicenseKey;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sLicenseKey = "your_license_key";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\98food processor.sldasm";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nDocType = SwDocumentMgr.SwDmDocumentType.swDmDocumentAssembly;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swClassFact = new SwDMClassFactory();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocMgr = swClassFact.GetApplication(sLicenseKey);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal) as SwDMDocument7;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCfgMgr = swDoc.ConfigurationManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string[] SWConfigNames;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SWConfigNames = (string[])swCfgMgr.GetConfigurationNames();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (int j = 0; j < SWConfigNames.Length; j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swConfiguration7 = swCfgMgr.GetConfigurationByName(SWConfigNames[j]) as SwDMConfiguration7;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object[] swComponents;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swComponents = (object[])swConfiguration7.GetComponents();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Configuration Name = " + SWConfigNames[j]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (int I = 0; I < swComponents.Length; I++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SwDMComponent5 comp;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}comp = swComponents[I] as SwDMComponent5;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Component Name = " + comp.Name);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}IsEnvelope = " + comp.IsEnvelope().ToString());
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}ExcludeFromBOM = " + comp.ExcludeFromBOM.ToString());
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("_______________________________________________________");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc.CloseDoc();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

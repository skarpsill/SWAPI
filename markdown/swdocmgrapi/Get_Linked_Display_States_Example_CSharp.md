---
title: "Get Linked Display States Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Linked_Display_States_Example_CSharp.htm"
---

# Get Linked Display States Example (C#)

This example gets an assembly and reports on its active
configuration and display states.

```vb
// -------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API
 //    Getting Started topic in the API help
 //    and ensure that the required DLLs have been registered.
 // 2. Open SOLIDWORKS and copy the code below to a C# macro.
 // 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 //    interop assembly is loaded in your project. (Right-click your
 //    project in Project Explorer, click Add Reference,
 //    kadov_tag{{</spaces>}}click the interop assembly in the .NET tab, or browse
 //    for the DLL in install_dir\api\redist).
 // 4. Substitute your license key for your_license_key in the code.
 // 5. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate Window for output.
 //--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMClassFactory swCf = default(SwDMClassFactory);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCf = new SwDMClassFactory();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMApplication swDocMgr = default(SwDMApplication);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocMgr = swCf.GetApplication("your_license_key");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMDocument14 swDoc12 = default(SwDMDocument14);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDmDocumentOpenError res = default(SwDmDocumentOpenError);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDmDocumentType dt = default(SwDmDocumentType);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dt = SwDmDocumentType.swDmDocumentAssembly;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string filename;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Opening an assembly...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\motor casing.sldasm";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc12 = (SwDMDocument14)swDocMgr.GetDocument(filename, dt, false, out res);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swDoc12 == null | (res != SwDmDocumentOpenError.swDmDocumentOpenErrorNone))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Error opening file....");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMConfiguration12 activeConfig = default(SwDMConfiguration12);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string activeConfigName = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMConfigurationMgr configMgr = default(SwDMConfigurationMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}configMgr = swDoc12.ConfigurationManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}activeConfigName = configMgr.GetActiveConfigurationName();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Getting the active configuration: " + activeConfigName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}activeConfig = (SwDMConfiguration12)configMgr.GetConfigurationByName(activeConfigName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (activeConfig == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Error getting the active configuration...");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("ID of " + activeConfig.Name2 + ": " + activeConfig.GetID());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int numLinkedDisplayStates = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}String[] ldsVariant = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string lds = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Boolean[] compVisibleList = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string[] compFileDirectory = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object ldsObject = null;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}numLinkedDisplayStates = activeConfig.GetLinkedDisplayStates(out ldsObject);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Number of linked display states of " + activeConfigName + ": " + numLinkedDisplayStates);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Getting all the components for one linked display state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ldsVariant = (String[])ldsObject;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object vis = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object fd = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}lds = ldsVariant[0];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}activeConfig.GetComponentVisibleByDisplayStateName(lds, out vis, out fd);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Getting the paths and file names of all of the components in the linked display state, " + lds + ": ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}compVisibleList = (Boolean[])vis;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}compFileDirectory = (String[])fd;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j <= compFileDirectory.GetUpperBound(0); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Component: " + compFileDirectory[j]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Is visible? " + compVisibleList[j]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Getting all the components in the configuration
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Getting the names of all of the components in the FeatureManager design tree in C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\api\\redist\ " + activeConfig.Name2 + ": ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object[] vComponents = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vComponents = (Object[])activeConfig.GetComponents();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (!((vComponents == null)))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SwDMComponent11 swDmComponent = default(SwDMComponent11);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (i = 0; i <= vComponents.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swDmComponent = (SwDMComponent11)vComponents[i];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Component name: " + swDmComponent.Name3);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" For a selective open with OpenDoc7, use: " + swDmComponent.SelectName2);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc12.CloseDoc();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
```

---
title: "Get Persistent IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Persistent_IDs_Example_CSharp.htm"
---

# Get Persistent IDs Example (C#)

## Get Sheet IDs Example (C#)

This example shows how to get the IDs of
drawing sheets.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Help
 //    Getting Started topic and ensure that the required DLLs
 //    have been registered.
 // 2. Open SOLIDWORKS and copy the code below to a C# macro.
 // 3. Convert the drawing document specified in sDocFileName
 //    to the latest supported version by opening and saving it
 //    to another name in SOLIDWORKS.
 //
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Because this document is used elsewhere, do not
 //    save any changes when closing it.
 //
 // 4. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 //    interop assembly is loaded in the project.
 // kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}} (Right-click the project in Project Explorer,
 //    click Add Reference, kadov_tag{{</spaces>}} click the interop assembly in
 //    the .NET tab, or browse for the DLL in
 //    install_dir\api\redist directory).
 // 5. Substitute your license key for your_license_key
 //    in the code.
 //
 // Postconditions: Inspect the Immediate Window for the sheet IDs.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMClassFactory swClassFact = default(SwDMClassFactory);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMApplication swDocMgr = default(SwDMApplication);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMDocument14 swDoc = default(SwDMDocument14);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sDocFileName = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDmDocumentType nDocType = default(SwDmDocumentType);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDmDocumentOpenError nRetVal = default(SwDmDocumentOpenError);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string sLicenseKey = null;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Specify your license key
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sLicenseKey = "your_license_key";

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If this drawing document doesn't exist on your system,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// then substitute the name of drawing document that does
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nDocType = SwDmDocumentType.swDmDocumentDrawing;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swClassFact = new SwDMClassFactory();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocMgr = swClassFact.GetApplication(sLicenseKey);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc = (SwDMDocument14)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swDoc == null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Unable to open document. Correct path to file or register Document Manager DLL.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwDMSheet3 Sheet = default(SwDMSheet3);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] Sheets = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sheets = (Object[])swDoc.GetSheets();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i <= Sheets.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Sheet = (SwDMSheet3)Sheets[i];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(Sheet.Name + " ID: " + Sheet.GetID());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc.CloseDoc();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
```

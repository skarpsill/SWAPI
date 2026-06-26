---
title: "Keep SOLIDWORKS Invisible While Activating Documents Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm"
---

# Keep SOLIDWORKS Invisible While Activating Documents Example (C#)

This example shows how to keep SOLIDWORKS invisible while activating SOLIDWORKS
documents, including assembly component files, and saving those documents
as PDF files.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly file exists.
// 2. Verify that c:\temp exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Saves the specified assembly file and its
//    component files as PDF files to the c:\temp.
// 2. Examine the Immediate window and c:\temp.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.IO;

namespace Macro1CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public
 partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public
 ModelDoc2 swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public ModelDocExtension swExtension;
```

```vb
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Frame pFrame;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string Document = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string Output = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}try
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Allow SOLIDWORKS to run in the background
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// and be invisible
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swApp.UserControl = false;

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// If the following property is true, then the
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// SOLIDWORKS frame will be visible on a call to
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// ISldWorks::ActivateDoc2; so, set it to false
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swApp.Visible = false;

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Keep SOLIDWORKS frame invisible when
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// ISldWorks::ActivateDoc2 is called
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pFrame = (Frame)swApp.Frame();
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pFrame.KeepInvisible = true;

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Document = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\blade shaft.sldasm";
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Output = "c:\\temp\\";
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("--- Save files as PDF ---");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SaveToPDF(Document, Output);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swApp.CloseAllDocuments(true);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("--- Done ---");

 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Show SOLIDWORKS frame and SOLIDWORKS
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pFrame.KeepInvisible = false;
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swApp.Visible = true;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}catch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Execution failed.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void SaveToPDF(string docFileName, string outputpath)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AssemblyDoc swAssembly = default(AssemblyDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int doctype = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string modelpath = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string modelFileName = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string convFileName = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool Success = false;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vComponents = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long i = 0;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Determine the type of SOLIDWORKS file based on
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// its filename extension
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string extension = "";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}extension = Path.GetExtension(docFileName);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (extension == ".sldprt")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocPART;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (extension == ".SLDPRT")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocPART;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (extension == ".sldasm")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocASSEMBLY;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (extension == ".SLDASM")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocASSEMBLY;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (extension == ".slddrw")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocDRAWING;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (extension == ".SLDDRW")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocDRAWING;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}doctype = (int)swDocumentTypes_e.swDocNONE;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Open document
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.OpenDoc6(docFileName, doctype, (int)swOpenDocOptions_e.swOpenDocOptions_Silent | (int)swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", ref errors, ref warnings);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swModel == null)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Failed to open document " + modelpath + ". Errors: " + errors);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Activate the document, which should remain invisible
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// due to earlier call to IFrame::KeepInvisible
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActivateDoc2(docFileName, true, ref errors);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Build destination filename
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelpath = swModel.GetPathName();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelFileName = Path.GetFileNameWithoutExtension(modelpath);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}convFileName = outputpath + modelFileName + ".pdf";
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swExtension = (ModelDocExtension)swModel.Extension;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Save document as PDF
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Success = swExtension.SaveAs(convFileName, (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors,
 ref warnings);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Success)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Document, " + modelpath + ", saved as " + convFileName + ". ");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Document not saved: ");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Errors: " + errors + modelpath + " as " + convFileName + ". ");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Process all components
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (doctype == (int)swDocumentTypes_e.swDocASSEMBLY)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAssembly = (AssemblyDoc)swModel;
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}vComponents = (object[])swAssembly.GetComponents(true);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (i = 0; i < vComponents.Length; i++)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Component2 swComponent = default(Component2);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swComponent = (Component2)vComponents[i];
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SaveToPDF(swComponent.GetPathName(), outputpath);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```

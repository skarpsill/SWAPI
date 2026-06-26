---
title: "Get All External References for Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_All_External_References_for_Drawing_Example_CSharp.htm"
---

# Get All External References for Drawing Example (C#)

This example shows how to get the external references for a drawing document.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API
 //    Getting Started topic and ensure that
 //    the required DLLs have been registered.
 // 2. Copy and paste this module into a C#
 //    console application in Microsoft Visual Studio.
 // 3. Substitute the name of a drawing that has at least one custom property
 //    for drawing_document_with_external_references.
 // 4. Add the SolidWorks.Interop.swdocumentmgr.dll
 //    reference to the project.
 // 5. Substitute your_license_code with your SOLIDWORKS
 //    Document Manager license key.
 // 6. Compile and run this program in Debug mode.
 //
 // Postconditions: Inspect the Immediate Window.
 //--------------------------------------------------------------------------

 using SolidWorks.Interop.swdocumentmgr;
 using System;
 using System.Diagnostics;
 using System.Collections.Generic;
 using System.Text;

 class Program
 {
     static void Main(string[] args)
     {
         const string sLicenseKey = "your_license_code";
         //Specify your license key
         const string sDocFileName = "drawing_document_with_external_references";

         SwDMClassFactory swClassFact = default(SwDMClassFactory);
         SwDMApplication swDocMgr = default(SwDMApplication);
         SwDMDocument23 swDoc = default(SwDMDocument23);
         SwDMSearchOption swSearchOpt = default(SwDMSearchOption);
         SwDmDocumentType nDocType = 0;
         SwDmDocumentOpenError nRetVal = 0;
         string[] vDependArr = null;

         SwDMDocumentLicenseType_e licenseType = 0;

         // Determine type of SOLIDWORKS file based on file extension

         if (sDocFileName.EndsWith("slddrw"))
         {
             nDocType = SwDmDocumentType.swDmDocumentDrawing;
         }
         else
         {
             // Not a drawing,
             nDocType =  SwDmDocumentType.swDmDocumentUnknown;

             // So do not open
             return;
         }

         swClassFact = new SwDMClassFactory();
         swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
         swSearchOpt = swDocMgr.GetSearchOptionObject();
         swDoc = (SwDMDocument23)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);
         Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone == nRetVal);

         Debug.Print("File = " + swDoc.FullName);

        licenseType = (SwDMDocumentLicenseType_e)swDoc.GetLicenseType();

         Debug.Print("License type as defined in SwDMDocumentLicenseType_e: " + licenseType);

         string bsFileTime = "";
         string bsLWFileTime = "";
         swDoc.GetFileAvgTime(out bsFileTime, out bsLWFileTime);
         Debug.Print("File open time: " + bsFileTime);
         Debug.Print("Lightweight open time: " + bsLWFileTime);

         string[] custprops = null;
         custprops = swDoc.GetCustomPropertyNames();

         bool isEditable = false;
         swDoc.IsCustomPropertyEditable(custprops[0], out isEditable);
         Debug.Print("Custom property " + custprops[0] + " is editable: " + isEditable);

         object vBrokenRefs = null;
         object vIsVirtuals = null;
         object vTimeStamps = null;
         object vIsImported = null;

         vDependArr = (string[])swDoc.GetAllExternalReferences5(swSearchOpt, out vBrokenRefs, out vIsVirtuals, out vTimeStamps, out vIsImported);

         if ((vDependArr == null)) return;

         Debug.Print("External references");
         foreach (string vDepend in vDependArr)
         {
             Debug.Print(" " + vDepend);
         }
         Debug.Print("Reference statuses as defined in swDmReferenceStatus");
         foreach (SwDmReferenceStatus brokenRef in (SwDmReferenceStatus[])vBrokenRefs)
         {
             Debug.Print(" " + brokenRef);
         }
         Debug.Print("Virtual components?");
         foreach (Boolean isVirtual in (Boolean[])vIsVirtuals)
         {
             Debug.Print(" " + isVirtual);
         }
         Debug.Print("Timestamps");
         foreach (Double timeStamp in (Int32[])vTimeStamps)
         {
             Debug.Print(" " + timeStamp);
         }
         Debug.Print("Imported components (empty if component is not imported)");
         foreach (string isImported_loopVariable in (string[])vIsImported)
         {
             Debug.Print("  Imported component:  " + isImported_loopVariable);
         }
     }
 }
```

---
title: "Replace Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Replace_Component_Example_CSharp.htm"
---

# Replace Component Example (C#)

This example shows how to replace a component with a different component.

```vb
 '---------------------------------------------------------------------------
  // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started
 //    topic and ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a VB.NET console application
 //    in Microsoft Visual Studio.
 // 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click:
 //       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 //    e. Click Add.
 //    f. Click Close.
 // 4. Ensure that the model to open exists.
 // 5. Substitute your_license_key with your SOLIDWORKS Document
 //    Manager license key.
 // 6. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. The first instance of the shaft washer component is
 '    replaced with a lock washer in the document.
 '
 ' NOTE: The specified file should be backed up before running this macro,
 ' as it is used elsewhere. The macro uses a replacement that does not
 ' properly fit in the model.
 '-------------------------------------------------------------------------
```

```vb
 using System;
 using System.Diagnostics;
 using SolidWorks.Interop.swdocumentmgr;
 namespace ConsoleApplication2
 {
     class Program
     {
         static void Main(string[] args)
         {

             SwDMClassFactory swCf;
             swCf = new SwDMClassFactory();
             SwDMApplication swDocMgr;
             swDocMgr = (SwDMApplication)swCf.GetApplication("your_license_key");
             SwDMDocument12 swDoc12;
             SwDmDocumentOpenError res;
             SwDmDocumentType dt;
             dt = SwDmDocumentType.swDmDocumentAssembly;
             string filename;
             Debug.Print("Opening an assembly...");

             filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\98food processor.sldasm";
             swDoc12 = swDocMgr.GetDocument(filename, dt,  false,  out res)  as  SwDMDocument12;

             if (swDoc12 == null | (res != SwDmDocumentOpenError.swDmDocumentOpenErrorNone))
             {
                 Debug.Print("Error opening file...");
                 return;
             }

             Debug.Print("Getting the active configuration...");
             SwDMConfiguration8 activeConfig;
             SwDMConfigurationMgr configMgr;
             configMgr = swDoc12.ConfigurationManager;
             configMgr.GetConfigurationNames();
             activeConfig = configMgr.GetConfigurationByName(configMgr.GetActiveConfigurationName()) as  SwDMConfiguration8;
             if (activeConfig == null)
             {
                 Debug.Print("Error getting the active configuration...");
                 return;
             }

             Debug.Print("Getting the components of the active configuration...");
             object[] vComponents;
             vComponents = (object[])activeConfig.GetComponents();
             SwDMComponent6 swDmComponent;

             int i;
             for (i = 0; i < vComponents.Length; i++)
             {
                 swDmComponent = (SwDMComponent6)vComponents[i];
                 if (swDmComponent.Name == "shaft washer")
                 {
                     bool bResult = swDmComponent.Replace("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\samples\\tutorial\\smartcomponents\\lockwasher.sldprt", "Default", false);
                     Debug.Print("Replacing shaft washer with lock washer...");
                     Debug.Print(bResult.ToString());
                     break;
                 }
             }

             swDoc12.Save();
             swDoc12.CloseDoc();

         }
     }
 }
```

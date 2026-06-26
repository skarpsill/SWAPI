---
title: "Get License Type of SOLIDWORKS Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_License_Types_of_SOLIDWORKS_Example_CSharp.htm"
---

# Get License Type of SOLIDWORKS Example (C#)

This example shows how to get the type of SOLIDWORKS license used when the
model was created.

```
//----------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part document.
// 2. Gets the type of SOLIDWORKS license used when
//    the model was created.
// 3. Examine the Immediate window.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            int licenseType = 0;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            licenseType = swModelDocExt.GetLicenseType();
            Debug.Print("Type of SOLIDWORKS license used when the model was created:");
            GetLicense(swApp, licenseType);

        }
        public void GetLicense(SldWorks swApp, int ltype)
        {
            switch (ltype)
            {
                case (int)swLicenseType_e.swLicenseType_Educational:
                    Debug.Print("  Educational");
                    break;
                case (int)swLicenseType_e.swLicenseType_Student:
                    Debug.Print("  Student");
                    break;
                case (int)swLicenseType_e.swLicenseType_StudentDesignKit:
                    Debug.Print("  Student Design Kit");
                    break;
                case (int)swLicenseType_e.swLicenseType_PersonalEdition:
                    Debug.Print("  Personal Edition");
                    break;
                case (int)swLicenseType_e.swLicenseType_Full_Office:
                    Debug.Print("  Office");
                    break;
                case (int)swLicenseType_e.swLicenseType_Full_Professional:
                    Debug.Print("  Professional");
                    break;
                case (int)swLicenseType_e.swLicenseType_Full_Premium:
                    Debug.Print("  Premium");
                    break;
                case (int)swLicenseType_e.swLicenseType_Full:
                    Debug.Print("  Standard");
                    break;
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

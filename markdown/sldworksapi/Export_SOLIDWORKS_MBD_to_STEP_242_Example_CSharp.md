---
title: "Export SOLIDWORKS MBD to STEP 242 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_SOLIDWORKS_MBD_to_STEP_242_Example_CSharp.htm"
---

# Export SOLIDWORKS MBD to STEP 242 Example (C#)

This example shows how to export a SOLIDWORKS MBD part to a STEP 242 file.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified part,
//    * SOLIDWORKS MBD 3D PDF theme, and
//    * c:\temp exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Gets the MBD3DPdfData object.
// 3. Sets the path and file name for the SOLIDWORKS MBD PDF.
// 4. Sets the theme for the SOLIDWORKS MBD 3D PDF.
// 5. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
// 6. Publishes the part to SOLIDWORKS MBD PDF.
// 7. Exports the SOLIDWORKS MBD part document to STEP 242.
// 8. Examine the Immediate window and c:\temp.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------
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
            MBD3DPdfData swMBDPdfData = default(MBD3DPdfData);
            string fileName = null;
            object standardViews = null;
            int[] viewIDs = new int[3];
            int status = 0;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get MBD3DPdfData object
            swMBDPdfData = (MBD3DPdfData)swModelDocExt.GetMBD3DPdfData();

            //Set path and file name for SOLIDWORKS MBD 3D PDF
            swMBDPdfData.FilePath = "c:\\temp\\MyBlockMBD.PDF";

            //Set SOLIDWORKS MBD 3D PDF theme
            swMBDPdfData.ThemeName = "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\data\\themes\\simple part (a4, portrait)\\theme.xml";

            //Set standard views for SOLIDWORKS MBD 3D PDF
            viewIDs[0] = (int)swStandardViews_e.swFrontView;
            viewIDs[1] = (int)swStandardViews_e.swTopView;
            viewIDs[2] = (int)swStandardViews_e.swDimetricView;
            standardViews = (object)viewIDs;
            swMBDPdfData.SetStandardViews(standardViews);

            //Publish part document to SOLIDWORKS MBD 3D PDF
            status = swModelDocExt.PublishTo3DPDF(swMBDPdfData);
            Debug.Print("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " + status);

            //Export SOLIDWORKS MBD part to STEP 242
            status = swModelDocExt.PublishSTEP242File("c:\\temp\\MyStepBlock.STP");
            Debug.Print("Status of exporting SOLIDWORKS MBD part to STEP 242 (0 = success): " + status);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

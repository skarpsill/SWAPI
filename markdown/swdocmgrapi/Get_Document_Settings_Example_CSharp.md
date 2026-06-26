---
title: "Get Document Settings Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Document_Settings_Example_CSharp.htm"
---

# Get Document Settings Example (C#)

This example shows how to get various settings for a document.

```vb
 //---------------------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started
 //    topic and ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a C# console application
 //    in Microsoft Visual Studio.
 // 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Select Add Reference.
 //    c. Click Browse.
 //    d. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
 //    e. Click Add.
 //    f. Click Close.
 // 4. Substitute path_to_SOLIDWORKS_2015_model with the path to a model that has been
 //    saved in SOLIDWORKS 2015 or later.
 // 5. Substitute your_license_key with your SOLIDWORKS Document Manager
 //    license key.
 // 6. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save any changes.
 //---------------------------------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Diagnostics;
 using SolidWorks.Interop.swdocumentmgr;

 namespace GetExtRefs2_CSharp
 {
     class Program
     {

         static SwDMClassFactory dmClassFact;
         static SwDMApplication4 dmDocMgr;
         static SwDMDocument19 dmDoc;
         static SwDmDocumentType dmDocType;
         static SwDmDocumentOpenError status;

         const string docPath = "path_to_SOLIDWORKS_2015_model";
         const string licenseKey = "your_license_key";

         static void Main()
         {

             dmClassFact = new SwDMClassFactory();
             dmDocMgr = (SwDMApplication4)dmClassFact.GetApplication(licenseKey);
             dmDoc = (SwDMDocument19)dmDocMgr.GetDocument(docPath, dmDocType, true, out status);

             if ((dmDoc != null))
             {
                 Debug.Print("Angular units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsAngular));
                 Debug.Print("Angular decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsAngularDecimalPlaces));
                 Debug.Print("Decimal rounding: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsDecimalRounding));
                 Debug.Print("Dual linear units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsDualLinear));
                 Debug.Print("Dual linear decimal display: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalDisplay));
                 Debug.Print("Dual linear decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalPlaces));
                 Debug.Print("Dual linear fraction denominator: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsDualLinearFractionDenominator));
                 Debug.Print("Energy decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsEnergyDecimalPlaces));
                 Debug.Print("Energy units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsEnergyUnits));
                 Debug.Print("Force units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsForce));
                 Debug.Print("Force decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsForceDecimalPlaces));
                 Debug.Print("Linear units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinear));
                 Debug.Print("Linear decimal display: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalDisplay));
                 Debug.Print("Linear decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalPlaces);
                 Debug.Print("Linear fraction denominator: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearFractionDenominator));
                 Debug.Print("Mass prop decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropDecimalPlaces));
                 Debug.Print("Mass prop length: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropLength));
                 Debug.Print("Mass prop mass: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropMass));
                 Debug.Print("Mass prop volume: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropVolume));
                 Debug.Print("Power decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsPowerDecimalPlaces));
                 Debug.Print("Power units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsPowerUnits));
                 Debug.Print("Time decimal places: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsTimeDecimalPlaces));
                 Debug.Print("Time units: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsTimeUnits));
                 Debug.Print("Unit system: " + dmDoc.GetSwDmSettingInteger((int)swDmDocumentUnitsIntegerValue_e.swDmUnitsUnitSystem));

                 Debug.Print("Dual linear feet and inches format? " + dmDoc.GetSwDmSettingToggle((int)swDmDocumentUnitsToggle_e.swDmUnitsDualLinearFeetAndInchesFormat));
                 Debug.Print("Dual linear round to nearest fraction? " + dmDoc.GetSwDmSettingToggle((int)swDmDocumentUnitsToggle_e.swDmUnitsDualLinearRoundToNearestFraction));
                 Debug.Print("Linear feet and inches format? " + dmDoc.GetSwDmSettingToggle((int)swDmDocumentUnitsToggle_e.swDmUnitsLinearFeetAndInchesFormat));
                 Debug.Print("Linear round to nearest fraction? " + dmDoc.GetSwDmSettingToggle((int)swDmDocumentUnitsToggle_e.swDmUnitsLinearRoundToNearestFraction));

             }
             else
             {
                 Debug.Print("Unable to open document. Check docPath variable.");
             }

         }

     }
 }
```

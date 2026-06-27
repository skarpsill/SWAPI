---
title: "Get Document Settings Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Document_Settings_Example_VBNET.htm"
---

# Get Document Settings Example (VB.NET)

This example shows how to get various settings for a document.

```vb
  '---------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started
  '    topic and ensure that the required DLLs are registered.
 ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference to the project:
  '    a. Right-click the solution in Solution Explorer.
 '    b. Select Add Reference.
 '    c. Click Browse.
 '    d. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
 '    e. Click Add.
 '    f. Click Close.
 ' 4. Substitute path_to_SOLIDWORKS_2015_model with the path to a model that has been
 '    saved in SOLIDWORKS 2015 or later.
 ' 5. Substitute your_license_key with your SOLIDWORKS Document Manager
 '    license key.
 ' 6. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save any changes.
  '---------------------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Imports System
 Imports System.Diagnostics

 Module Module1

     Dim dmClassFact As SwDMClassFactory
     Dim dmDocMgr As SwDMApplication4
     Dim dmDoc As SwDMDocument19
     Dim dmDocType As SwDmDocumentType
     Dim status As SwDmDocumentOpenError

     Const docPath As String = "path_to_SOLIDWORKS_2015_model"
     Const licenseKey As String = "your_license_key"

     Sub main()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         dmDocMgr = dmClassFact.GetApplication(licenseKey)
         dmDoc = dmDocMgr.GetDocument(docPath, dmDocType, True, status)

         If Not (dmDoc Is Nothing) Then
             Debug.Print("Angular units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsAngular))
             Debug.Print("Angular decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsAngularDecimalPlaces))
             Debug.Print("Decimal rounding: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsDecimalRounding))
             Debug.Print("Dual linear units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsDualLinear))
             Debug.Print("Dual linear decimal display: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalDisplay))
             Debug.Print("Dual linear decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalPlaces))
             Debug.Print("Dual linear fraction denominator: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsDualLinearFractionDenominator))
             Debug.Print("Energy decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsEnergyDecimalPlaces))
             Debug.Print("Energy units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsEnergyUnits))
             Debug.Print("Force units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsForce))
             Debug.Print("Force decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsForceDecimalPlaces))
             Debug.Print("Linear units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinear))
             Debug.Print("Linear decimal display: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalDisplay))
             Debug.Print("Linear decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearDecimalPlaces))
             Debug.Print("Linear fraction denominator: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsLinearFractionDenominator))
             Debug.Print("Mass prop decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropDecimalPlaces))
             Debug.Print("Mass prop length: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropLength))
             Debug.Print("Mass prop mass: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropMass))
             Debug.Print("Mass prop volume: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsMassPropVolume))
             Debug.Print("Power decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsPowerDecimalPlaces))
             Debug.Print("Power units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsPowerUnits))
             Debug.Print("Time decimal places: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsTimeDecimalPlaces))
             Debug.Print("Time units: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsTimeUnits))
             Debug.Print("Unit system: " & dmDoc.GetSwDmSettingInteger(swDmDocumentUnitsIntegerValue_e.swDmUnitsUnitSystem))

             Debug.Print("Dual linear feet and inches format? " & dmDoc.GetSwDmSettingToggle(swDmDocumentUnitsToggle_e.swDmUnitsDualLinearFeetAndInchesFormat))
             Debug.Print("Dual linear round to nearest fraction? " & dmDoc.GetSwDmSettingToggle(swDmDocumentUnitsToggle_e.swDmUnitsDualLinearRoundToNearestFraction))
             Debug.Print("Linear feet and inches format? " & dmDoc.GetSwDmSettingToggle(swDmDocumentUnitsToggle_e.swDmUnitsLinearFeetAndInchesFormat))
             Debug.Print("Linear round to nearest fraction? " & dmDoc.GetSwDmSettingToggle(swDmDocumentUnitsToggle_e.swDmUnitsLinearRoundToNearestFraction))

         Else
             Debug.Print("Unable to open document. Check docPath variable.")
         End If

     End Sub

 End Module
```

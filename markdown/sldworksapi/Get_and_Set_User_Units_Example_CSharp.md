---
title: "Get and Set Document Units Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Units_Example_CSharp.htm"
---

# Get and Set Document Units Example (C#)

This example shows how to get and set document angle units.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Observe the document's angle unit properties in the Immediate window.
 // 2. Modifies the decimal places and type of the angle unit.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetSetUserUnits_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         UserUnit docUserUnit;
         bool boolstatus;
         ModelDocExtension ModelDocExtension;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             ModelDocExtension = Part.Extension;
             docUserUnit = (UserUnit)Part.GetUserUnit((int)swUserUnitsType_e.swAngleUnit);

             //Get document's current angle unit properties
             Debug.Print("Angle unit properties: ");
             Debug.Print("  Display leading zero? " + docUserUnit.DisplayLeadingZero);
             Debug.Print("  Fraction display as defined in swFractionDisplay_e: " + docUserUnit.FractionBase);
             Debug.Print("  Fraction denominator: " + docUserUnit.FractionValue);
             Debug.Print("  Pad with zeroes? " + docUserUnit.PadZero);
             Debug.Print("  Round to fraction? " + docUserUnit.RoundToFraction);
             Debug.Print("  Decimal separator character: " + docUserUnit.SeparatorCharacter);
             Debug.Print("  Decimal places: " + docUserUnit.SignificantDigits);
             Debug.Print("  Units as defined in swAngleUnit_e: " + docUserUnit.SpecificUnitType);
             Debug.Print("  Unit type as defined in swUserUnitsType_e: " + docUserUnit.UnitType);
             Debug.Print("  Units are metric? " + docUserUnit.IsMetric());
             Debug.Print("  Conversion factor: " + docUserUnit.GetConversionFactor());
             Debug.Print("  Full units name: " + docUserUnit.GetFullUnitName(true));
             Debug.Print("  Units name: " + docUserUnit.GetUnitsString(true));
             Debug.Print("  Angle tolerance: " + docUserUnit.GetUserAngleTolerance());
             Debug.Print("");

             double sysVal = 0;
             sysVal = docUserUnit.ConvertDoubleToSystemValue(2.0);
             Debug.Print("  2.0 in document angle units: " + sysVal + ".");

             double compVal = 0;
             boolstatus = docUserUnit.ConvertToSystemValue("10 / 2", ref compVal);
             Debug.Print("  10 / 2 in document angle units: " + compVal + ".");

             string stringVal = null;
             stringVal = docUserUnit.ConvertToUserUnit(2.0, true, true);
             Debug.Print("  2.0 in complete document angle units: " + stringVal + ".");

             //Modify decimal places and type of angle unit
             boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swUnitsAngular, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, (int)swAngleUnit_e.swDEG_MIN_SEC);
             boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swUnitsAngularDecimalPlaces, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, 2);

         }

         public SldWorks swApp;

     }

 }
```

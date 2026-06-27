---
title: "Get and Set Document Units Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Units_Example_VBNET.htm"
---

# Get and Set Document Units Example (VB.NET)

This example shows how to get and set document angle units.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
  ' 1. Observe the document's angle unit properties in the Immediate window.
  ' 2. Modifies the decimal places and type of the angle unit.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim docUserUnit As UserUnit
     Dim boolstatus As Boolean
     Dim ModelDocExtension As ModelDocExtension

     Sub main()

         Part = swApp.ActiveDoc
         ModelDocExtension = Part.Extension
         docUserUnit = Part.GetUserUnit(swUserUnitsType_e.swAngleUnit)

         'Get document's current angle unit properties
         Debug.Print("Angle unit properties: ")
         Debug.Print("  Display leading zero? " & docUserUnit.DisplayLeadingZero)
         Debug.Print("  Fraction display as defined in swFractionDisplay_e: " & docUserUnit.FractionBase)
         Debug.Print("  Fraction denominator: " & docUserUnit.FractionValue)
         Debug.Print("  Pad with zeroes? " & docUserUnit.PadZero)
         Debug.Print("  Round to fraction? " & docUserUnit.RoundToFraction)
         Debug.Print("  Decimal separator character: " & docUserUnit.SeparatorCharacter)
         Debug.Print("  Decimal places: " & docUserUnit.SignificantDigits)
         Debug.Print("  Units as defined in swAngleUnit_e: " & docUserUnit.SpecificUnitType)
         Debug.Print("  Unit type as defined in swUserUnitsType_e: " & docUserUnit.UnitType)
         Debug.Print("  Units are metric? " & docUserUnit.IsMetric)
         Debug.Print("  Conversion factor: " & docUserUnit.GetConversionFactor)
         Debug.Print("  Full units name: " & docUserUnit.GetFullUnitName(True))
         Debug.Print("  Units name: " & docUserUnit.GetUnitsString(True))
         Debug.Print("  Angle tolerance: " & docUserUnit.GetUserAngleTolerance)
         Debug.Print("")

         Dim sysVal As Double
         sysVal = docUserUnit.ConvertDoubleToSystemValue(2.0#)
         Debug.Print("  2.0 in document angle units: " & sysVal & ".")

         Dim compVal As Double
         boolstatus = docUserUnit.ConvertToSystemValue("10 / 2", compVal)
         Debug.Print("  10 / 2 in document angle units: " & compVal & ".")

         Dim stringVal As String
         stringVal = docUserUnit.ConvertToUserUnit(2.0#, True, True)
         Debug.Print("  2.0 in complete document angle units: " & stringVal & ".")

         'Modify decimal places and type of angle unit
         boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swUnitsAngular, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swAngleUnit_e.swDEG_MIN_SEC)
         boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swUnitsAngularDecimalPlaces, swUserPreferenceOption_e.swDetailingNoOptionSpecified, 2)

     End Sub

     Public swApp As SldWorks

 End Class
```

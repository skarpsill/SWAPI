---
title: "Get and Set Document Units Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Units_Example_VB.htm"
---

# Get and Set Document Units Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim docUserUnit As SldWorks.UserUnit
 Dim boolstatus As Boolean
 Dim ModelDocExtension As SldWorks.ModelDocExtension
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set ModelDocExtension = Part.Extension
     Set docUserUnit = Part.GetUserUnit(swAngleUnit)

    'Get document's current angle unit properties
     Debug.Print "Angle unit properties: "
     Debug.Print "  Display leading zero? " & docUserUnit.DisplayLeadingZero
     Debug.Print "  Fraction display as defined in swFractionDisplay_e: " & docUserUnit.FractionBase
     Debug.Print "  Fraction denominator: " & docUserUnit.FractionValue
     Debug.Print "  Pad with zeroes? " & docUserUnit.PadZero
     Debug.Print "  Round to fraction? " & docUserUnit.RoundToFraction
     Debug.Print "  Decimal separator character: " & docUserUnit.SeparatorCharacter
     Debug.Print "  Decimal places: " & docUserUnit.SignificantDigits
     Debug.Print "  Units as defined in swAngleUnit_e: " & docUserUnit.SpecificUnitType
     Debug.Print "  Unit type as defined in swUserUnitsType_e: " & docUserUnit.UnitType
     Debug.Print "  Units are metric? " & docUserUnit.IsMetric
     Debug.Print "  Conversion factor: " & docUserUnit.GetConversionFactor
     Debug.Print "  Full units name: " & docUserUnit.GetFullUnitName(True)
     Debug.Print "  Units name: " & docUserUnit.GetUnitsString(True)
     Debug.Print "  Angle tolerance: " & docUserUnit.GetUserAngleTolerance
     Debug.Print ""

    Dim sysVal As Double
     sysVal = docUserUnit.ConvertDoubleToSystemValue(2#)
     Debug.Print "  2.0 in document angle units: " & sysVal & "."

    Dim compVal As Double
     boolstatus = docUserUnit.ConvertToSystemValue("10 / 2", compVal)
     Debug.Print "  10 / 2 in document angle units: " & compVal & "."

    Dim stringVal As String
     stringVal = docUserUnit.ConvertToUserUnit(2#, True, True)
     Debug.Print "  2.0 in complete document angle units: " & stringVal & "."

    'Modify decimal places and type of angle unit
     boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swUnitsAngular, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swAngleUnit_e.swDEG_MIN_SEC)
     boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swUnitsAngularDecimalPlaces, swUserPreferenceOption_e.swDetailingNoOptionSpecified, 2)

End Sub
```

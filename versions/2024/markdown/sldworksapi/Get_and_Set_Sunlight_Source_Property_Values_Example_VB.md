---
title: "Get and Set Sunlight Source Property Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm"
---

# Get and Set Sunlight Source Property Values Example (VBA)

This example shows how to get and set sunlight properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part with a sunlight source.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the sunlight properties.
 ' ---------------------------------------------------------------------------
Dim swApp           As SldWorks.SldWorks
 Dim swModelDoc      As SldWorks.ModelDoc2
 Dim swModelDocExt   As SldWorks.ModelDocExtension
 Dim retval          As Boolean
 Dim NorthDirection  As SldWorks.MathVector
 Dim DateTime        As String
 Dim vVector         As Variant
 Dim nVector(2)      As Double
 Dim swMathUtil      As SldWorks.MathUtility
 Dim NorthLatitude   As Double
 Dim EastLongitude   As Double
 Dim TimeZone        As Double
 Dim Haze As Double
 Dim SunDiameter As Double
 Dim GroundAlbedo As Long
 Dim SkyGamma As Double
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swModelDoc = swApp.ActiveDoc
     Set swModelDocExt = swModelDoc.Extension

    'Get sunlight property values
     retval = swModelDocExt.GetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
     retval = swModelDocExt.GetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)

    Debug.Print "North direction: " & NorthDirection.ArrayData(0) & "," & NorthDirection.ArrayData(1) & "," & NorthDirection.ArrayData(2)
     Debug.Print "North latitude: " & NorthLatitude
     Debug.Print "East longitude: " & EastLongitude
     Debug.Print "Time Zone: " & TimeZone
     Debug.Print "Date and time: " & DateTime
     Debug.Print "Haze (0.0 - 1.0): " & Haze
     Debug.Print "Sun diameter (0.01 - 21474836.47): " & SunDiameter
     Debug.Print "RGB for ground albedo: " & GroundAlbedo
     Debug.Print "Sky Gamma (0.1 = 100.0): " & SkyGamma
     Debug.Print "Minutes of sunlight: " & swModelDocExt.SunLightInformation(swSunlight_LengthOfDay)
     Debug.Print "Sunrise (hours from midnight): " & swModelDocExt.SunLightInformation(swSunlight_Sunrise)
     Debug.Print "Sunset (hours from midnight): " & swModelDocExt.SunLightInformation(swSunlight_Sunset)

    'Set sunlight source property values
     Set swMathUtil = swApp.GetMathUtility
     nVector(0) = 1:  nVector(1) = 0:  nVector(2) = 0
     vVector = nVector
     Set NorthDirection = swMathUtil.CreateVector((vVector))

    DateTime = "11/9/2012 2:48:13 PM"
     NorthLatitude = NorthLatitude + 0.1
     EastLongitude = EastLongitude + 0.1
     TimeZone = TimeZone + 0.5
     retval = swModelDocExt.SetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)

End Sub
```

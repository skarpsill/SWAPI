---
title: "Get and Set User Preferences Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Preferences_Example_VB.htm"
---

# Get and Set User Preferences Example (VBA)

This sample code demonstrates how to get and set
various system options and document properties.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Open a drawing document.
 ' kadov_tag{{<spaces>}}2. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Create a layer named test in the document.
 ' kadov_tag{{<spaces>}}3. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Open an Immediate window.
 '
 ' kadov_tag{{<spaces>}}Postconditions:
 ' 1. Observe the new settings in the Immediate window.
 ' 2. Maps the value returned by the GetUserPreferenceInteger method
 '    to the corresponding enumerator member in the enumerator online help.
 ' kadov_tag{{<spaces>}}3. Click Tools > Options in SOLIDWORKS and verify the new settings.
 '----------------------------------------------------------------------------
Dim swApp As Object
Dim Part As Object
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Dim swTextFormat As SldWorks.TextFormat
Dim TextFormatObj As Object
Dim ModelDocExtension As ModelDocExtension

Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
Set ModelDocExtension = Part.Extension

    'The following call demonstrates how to get and set a Tools > Options > System Options > General option
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Custom property used as component description
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceStringValue(swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription, "Status")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > General > Custom property used as component description: " & swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription)

    'The following calls demonstrate how to get and set Tools > Options > System Options > View options
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Reverse mouse wheel zoom direction
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swViewReverseWheelZoomDirection, True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > Reverse mouse wheel zoom direction: " & swApp.GetUserPreferenceToggle(swUserPreferenceToggle_e.swViewReverseWheelZoomDirection)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'View rotation - Arrow keys
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewRotationArrowKeys, 0.2268928027593)
     '1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > Arrow keys: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewRotationArrowKeys) * 57.3 'Convert to degrees
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'View rotation - Mouse speed
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed, 56)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > Mouse speed: " & swApp.GetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Transitions - View transition
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewAnimationSpeed, 2.5)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > View transition: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewAnimationSpeed)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Transitions - Hide/show component
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent, 0.8000000119209)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > Hide/show component: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Transitions - Isolate
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionIsolate, 1.222222208977)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > System Options > View > Isolate: " & swApp.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swViewTransitionIsolate)

    'The following calls demonstrate how to get and set the Tools > Options > Document Properties > Drafting Standard option. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
    'Map the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Overall drafting standard
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swDetailingStandard_e.swDetailingStandardISO)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim sText As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}sText = "Tools > Options > Document Properties > Drafting Standard > Overall drafting standard is "
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Select Case ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, swUserPreferenceOption_e.swDetailingNoOptionSpecified)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "ANSI"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "ISO"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "DIN"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "JIS"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 5
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "BS"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 6
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "GOST"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 7
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "GB"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Case 8
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print sText & "User Defined"
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
     'The following API calls demonstrate how to get and set Tools > Options > Document Properties > Annotations > Balloons options
     'Map the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Leader style - Leader Thickness
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0, swLineWeights_e.swLW_NUMBER)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Leader Thickness: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Leader style - Custom leader thickness
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0, 0.00028)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Custom Leader Thickness: " & ModelDocExtension.GetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Frame style - Frame Thickness
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0, swLineWeights_e.swLW_NUMBER)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Frame Thickness: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Frame style - Custom frame thickness
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0, 0.00028)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Custom Frame Thickness: " & ModelDocExtension.GetUserPreferenceDouble(swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Text - Upper - Custom property
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0, "Source")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Text Upper Custom property: " & ModelDocExtension.GetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Single balloon - Style
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0, swBalloonStyle_e.swBS_Triangle)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Style: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Single balloon - Size
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0, swBalloonFit_e.swBF_3Chars)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Size: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Stacked balloons - Style
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0, swBalloonStyle_e.swBS_Triangle)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Style: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Stacked balloons - Size
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0, swBalloonFit_e.swBF_3Chars)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Size: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Auto balloon layout
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0, swBalloonLayoutType_e.swDetailingBalloonLayout_Right)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Auto balloon layout: " & ModelDocExtension.GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Leader display - Use document leader length
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Leader display - Use document leader length: " & ModelDocExtension.GetUserPreferenceToggle(swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Layer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingBalloon, "test")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Layer: " & ModelDocExtension.GetUserPreferenceString(swUserPreferenceStringValue_e.swDetailingLayer, swUserPreferenceOption_e.swDetailingBalloon)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Font...
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set TextFormatObj = ModelDocExtension.GetUserPreferenceTextFormat(swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swTextFormat = TextFormatObj
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTextFormat.Italic = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTextFormat.Bold = True
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceTextFormat(swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0, swTextFormat)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Tools > Options > Document Properties > Annotations > Balloons > Font is italic and bold: " & boolstatus
End Sub
```

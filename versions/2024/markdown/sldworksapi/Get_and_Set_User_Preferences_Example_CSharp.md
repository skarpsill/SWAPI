---
title: "Get and Set User Preferences Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_User_Preferences_Example_CSharp.htm"
---

# Get and Set User Preferences Example (C#)

This sample code demonstrates how to use the methods for getting and setting various system options and document properties.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}1. kadov_tag{{<spaces>}}Open a drawing document.
 // kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}2. kadov_tag{{<spaces>}}Create a layer named test in the drawing.
 // kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}3. kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Open an Immediate window.
 // kadov_tag{{<spaces>}}
 // kadov_tag{{<spaces>}}Postconditions: kadov_tag{{</spaces>}}
 // 1. kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Observe the new settings in the Immediate window.
 // kadov_tag{{<spaces>}}2. Maps the value returned by the GetUserPreferenceInteger
 //    method to the corresponding enumerator member in the enumerator
 //    online help.
 // 3. Click Tools > Options in SOLIDWORKS and verify the new settings.
 //-------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace UserPreferences_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
partial class SolidWorksMacro
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 Part = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}TextFormat swTextFormat = default(TextFormat);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object TextFormatObj = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension ModelDocExtension = default(ModelDocExtension);
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Part = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension = Part.Extension;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//The following call demonstrates how to get and set a Tools > Options > System Options > General option

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Custom property used as component description
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription, "Status");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > General > Custom property used as component description: " + swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription));

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//The following calls demonstrate how to get and set Tools > Options > System Options > View options

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Reverse mouse wheel zoom direction
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swViewReverseWheelZoomDirection, true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > Reverse mouse wheel zoom direction: " + swApp.GetUserPreferenceToggle((int)swUserPreferenceToggle_e.swViewReverseWheelZoomDirection));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//View rotation - Arrow keys
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewRotationArrowKeys, 0.2268928027593);

        //1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > Arrow keys: " + swApp.GetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewRotationArrowKeys) * 57.3);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Convert to degrees
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//View rotation - Mouse speed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceIntegerValue((int)swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed, 56);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > Mouse speed: " + swApp.GetUserPreferenceIntegerValue((int)swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Transitions - View transition
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewAnimationSpeed, 2.5);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > View transition: " + swApp.GetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewAnimationSpeed));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Transitions - Hide/show component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent, 0.8000000119209);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > Hide/show component: " + swApp.GetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Transitions - Isolate
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swApp.SetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewTransitionIsolate, 1.222222208977);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > System Options > View > Isolate: " + swApp.GetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swViewTransitionIsolate));

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//The following calls demonstrate how to get and set the Tools > Options > Document Properties > Drafting Standard option
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Maps the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Overall drafting standard
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, (int)swDetailingStandard_e.swDetailingStandardISO);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string sText = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}sText = "Tools > Options > Document Properties > Drafting Standard > Overall drafting standard is ";
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingDimensionStandard, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "ANSI");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "ISO");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "DIN");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "JIS");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 5:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "BS");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 6:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "GOST");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 7:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "GB");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 8:
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(sText + "User Defined");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//The following calls demonstrate how to get and set Tools > Options > Document Properties > Annotations > Balloons options
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Maps the value returned by the GetUserPreferenceInteger method to the corresponding enumerator member in the enumerator online help

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Leader style - Leader Thickness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0, (int)swLineWeights_e.swLW_NUMBER);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Leader Thickness: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBalloonLeaderLineThickness, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Leader style - Custom leader thickness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceDouble((int)swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0, 0.00028);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Custom Leader Thickness: " + ModelDocExtension.GetUserPreferenceDouble((int)swUserPreferenceDoubleValue_e.swDetailingBalloonLeaderLineThicknessCustom, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Frame style - Frame Thickness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0, (int)swLineWeights_e.swLW_NUMBER);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Frame Thickness: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBalloonFrameLineThickness, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Frame style - Custom frame thickness
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceDouble((int)swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0, 0.00028);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Custom Frame Thickness: " + ModelDocExtension.GetUserPreferenceDouble((int)swUserPreferenceDoubleValue_e.swDetailingBalloonFrameLineThicknessCustom, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Text - Upper - Custom property
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceString((int)swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0, "Source");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Text Upper Custom property: " + ModelDocExtension.GetUserPreferenceString((int)swUserPreferenceStringValue_e.swDetailingBOMUpperCustomProperty, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Single balloon - Style
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0, (int)swBalloonStyle_e.swBS_Triangle);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Style: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Single balloon - Size
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0, (int)swBalloonFit_e.swBF_3Chars);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Single balloon - Size: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Stacked balloons - Style
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0, (int)swBalloonStyle_e.swBS_Triangle);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Style: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonStyle, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Stacked balloons - Size
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0, (int)swBalloonFit_e.swBF_3Chars);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Stacked balloons - Size: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Auto balloon layout
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0, (int)swBalloonLayoutType_e.swDetailingBalloonLayout_Right);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Auto balloon layout: " + ModelDocExtension.GetUserPreferenceInteger((int)swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Leader display - Use document leader length
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0, true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Leader display - Use document leader length: " + ModelDocExtension.GetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDetailingBalloonUseDocBentLeaderLength, 0));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Layer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceString((int)swUserPreferenceStringValue_e.swDetailingLayer, (int)swUserPreferenceOption_e.swDetailingBalloon, "test");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Layer: " + ModelDocExtension.GetUserPreferenceString((int)swUserPreferenceStringValue_e.swDetailingLayer, (int)swUserPreferenceOption_e.swDetailingBalloon));
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Font
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}TextFormatObj = ModelDocExtension.GetUserPreferenceTextFormat((int)swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTextFormat = (TextFormat)TextFormatObj;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTextFormat.Italic = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTextFormat.Bold = true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = ModelDocExtension.SetUserPreferenceTextFormat((int)swUserPreferenceTextFormat_e.swDetailingBalloonTextFormat, 0, swTextFormat);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Tools > Options > Document Properties > Annotations > Balloons > Font is italic and bold: " + boolstatus);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
}
```

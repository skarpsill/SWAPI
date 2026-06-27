---
title: "Get and Save Routing Settings Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Save_Routing_Settings_Example_CSharp.htm"
---

# Get and Save Routing Settings Example (C#)

This example shows how to get and save routing settings.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. In SOLIDWORKS, click Tools > Add-Ins, select SOLIDWORKS Routing, and
 //    click OK.
  // 2. In the IDE, right-click the project, select Add Reference,
 //      browse  install_dir\api\redist, and click
 //    SolidWorks.Interop.SWRoutingLib.dll.
 // 3. Ensure that c:\temp exists.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 // 1. Saves routing settings to c:\temp\routingSettings.sqy.
 // 2. Inspect the Immediate window.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System.Runtime.InteropServices;
 namespace CreateRoutingSettings_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             RoutingSettings routingSettings = default(RoutingSettings);
             Boolean boolstatus = false;

             string wireNameHdr = null;
             string fromRefHdr = null;
             string fromPinHdr = null;
             string fromPartNoHdr = null;
             string toRefHdr = null;
             string toPinHdr = null;
             string toPartNoHdr = null;
             string cableNameHdr = null;
             string coreNameHdr = null;
             string colourHdr = null;
             string wireSpecHdr = null;
             string otherAttribHdr = null;
             wireNameHdr = "";
             fromRefHdr = "";
             fromPinHdr = "";
             fromPartNoHdr = "";
             toRefHdr = "";
             toPinHdr = "";
             toPartNoHdr = "";
             cableNameHdr = "";
             coreNameHdr = "";
             colourHdr = "";
             wireSpecHdr = "";
             otherAttribHdr = "";

             routingSettings = swApp.GetRoutingSettings();

             boolstatus = routingSettings.SaveRoutingSettingsToFile("c:\\temp\\routingSettings.sqy");
             boolstatus = routingSettings.GetFromToListHeaderDefinitions(out wireNameHdr, out fromRefHdr, out fromPinHdr, out fromPartNoHdr, out toRefHdr, out toPinHdr, out toPartNoHdr, out cableNameHdr, out coreNameHdr, out colourHdr,
             out wireSpecHdr, out otherAttribHdr);
             Debug.Print("From-to list column headers");
             Debug.Print("  Wire name: " + wireNameHdr);
             Debug.Print("  From reference: " + fromRefHdr);
             Debug.Print("  From pin: " + fromPinHdr);
             Debug.Print("  From part number: " + fromPartNoHdr);
             Debug.Print("  To reference: " + toRefHdr);
             Debug.Print("  To pin: " + toPinHdr);
             Debug.Print("  To part number: " + toPartNoHdr);
             Debug.Print("  Cable name: " + cableNameHdr);
             Debug.Print("  Core name: " + coreNameHdr);
             Debug.Print("  Color: " + colourHdr);
             Debug.Print("  Wire spec: " + wireSpecHdr);
             Debug.Print("  Other attribute: " + otherAttribHdr);
             Debug.Print("");
             Debug.Print("Slack %: " + routingSettings.GetRoutingUserPreferenceDoubleValue((int)swUserPreferenceRoutingDouble_e.swSlackPercentage));
             Debug.Print("Text size for connection and route points: " + routingSettings.GetRoutingUserPreferenceDoubleValue((int)swUserPreferenceRoutingDouble_e.swTextSizeForConnectionAndRoutePoints));
             Debug.Print("Rotation increment in degrees: " + routingSettings.GetRoutingUserPreferenceIntegerValue((int)swUserPreferenceRoutingInteger_e.swComponentRotationIncrementDegrees));
             Debug.Print("Enable minimum bend radius checks: " + routingSettings.GetRoutingUserPreferenceIntegerValue((int)swUserPreferenceRoutingInteger_e.swEnableMinimumBendRadiusChecks));
             Debug.Print("");
             Debug.Print("Default file locations");
             Debug.Print("  Assembly template: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingAssemblyTemplate, true));
             Debug.Print("  Cable library: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingCableLibrary, true));
             Debug.Print("  Component library: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingComponentLibrary, true));
             Debug.Print("  Covering library: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingCoveringLibrary, true));
             Debug.Print("  Interconnects library: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingInterconnectsLibrary, true));
             Debug.Print("  Pipe tube covering library: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingPipeTubeCoveringLibrary, true));
             Debug.Print("  Standard cable: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingStandardCable, true));
             Debug.Print("  Standard tubes: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingStandardTubes, true));
             Debug.Print("  Tag schemes: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swFileLocationsRoutingTagSchemes, true));
             Debug.Print("  Routing library path: " + routingSettings.GetRoutingUserPreferenceStringValue((int)swUserPreferenceRoutingFileLocations_e.swRoutingLibraryPath, true));
             Debug.Print("");
             Debug.Print("Always use default document template? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swAlwaysUseDefaultDocumentTemplate));
             Debug.Print("Automatically add dimensions to route stubs? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swAutomaticallyAddDimensionToRouteStubs));
             Debug.Print("Automatically create sketch fillets? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swAutomaticallyCreateSketchFillets));
             Debug.Print("Automatically route on drop of clips? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swAutomaticallyRouteOnDropOfClips));
             Debug.Print("Automatically route on drop of flange connectors? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swAutomaticallyRouteOnDropOfFlangeConnectors));
             Debug.Print("Create custom fittings? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swCreateCustomFittings));
             Debug.Print("Create pipes on open line segments? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swCreatePipesOnOpenLineSegments));
             Debug.Print("Display error balloons? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swDisplayErrorBalloons));
             Debug.Print("Enable route error checking? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swEnableRouteErrorChecking));
             Debug.Print("Include coverings in bills of material? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swIncludeCoveringsInBOM));
             Debug.Print("Save route assembly externally? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swSaveRouteAssemblyExternally));
             Debug.Print("Save route parts externally? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swSaveRoutePartsExternally));
             Debug.Print("Use automatic naming for route parts? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swUseAutomaticNamingForRouteParts));
             Debug.Print("User centerline dimension? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swUseCenterlineDim));
             Debug.Print("Use triad to position and orient components? " + routingSettings.GetRoutingUserPreferenceToggle((int)swUserPreferenceRoutingToggle_e.swUseTriadToPosAndOrientComp));

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

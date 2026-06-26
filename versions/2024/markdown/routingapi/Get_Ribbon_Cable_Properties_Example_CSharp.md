---
title: "Get Ribbon Cable Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Ribbon_Cable_Properties_Example_CSharp.htm"
---

# Get Ribbon Cable Properties Example (C#)

This example shows how to get ribbon cable properties.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 // 2. In Tools > Options > System Options > Routing > Routing File Locations,
 //    click Launch Routing Library Manager and set the locations of your
 //    SOLIDWORKS Routing files.
  // 3. In the IDE, right-click the project,
 //    click Add Reference, browse install_dir\api\redist, click
 //    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
  // 4. Open an electrical routing assembly that has a ribbon cable.
 // 5. In the FeatureManager design tree, select the component that contains the
 //    electrical route.
 // 6. Open an Immediate window.
 //
 // Postconditions: Prints the thickness and width of the ribbon cable to the
 // Immediate window.
  //----------------------------------------------------------------------------
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

 namespace GetRibbonCableProperties_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         AssemblyDoc swTopLevelAssembly;
         RouteManager rtRouteManager;
         RibbonCable rtRibbonCable;
         ElectricalRoute rtElectRoute;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swTopLevelAssembly = (AssemblyDoc)swModel;
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document: " + swModel.GetPathName());
                 return;
             }

             rtElectRoute = rtRouteManager.GetElectricalRoute();

             if ((rtElectRoute != null))
             {
                 rtRibbonCable = rtElectRoute.GetRibbonCableDispatch();

                 Debug.Print("Ribbon cable");
                 Debug.Print(" Thickness: " + rtRibbonCable.GetRibbonCableThickness);
                 Debug.Print(" Width: " + rtRibbonCable.GetRibbonCableWidth);

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

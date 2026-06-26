---
title: "Get Cable Cores Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Cores_Example_CSharp.htm"
---

# Get Cable Cores Example (C#)

This example shows how to get the cores of cables.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified assembly exists.
 // 2. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
  // 3. In Tools > Options > System Options > Routing > Routing File Locations,
  //    click Launch Routing Library Manager and set the locations of your
 //    SOLIDWORKS Routing files.
 // 4. In the IDE, right-click the project,
 //    click Add Reference, browse install_dir\api\redist, click
 //    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified assembly.
 // 2. Selects Harness1^RoutingAssem1-1.
 // 3. Gets the cables in the electrical route.
  // 4. Prints the number of wires and the properties of each wire in the cable.
 // 5. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
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

 namespace GetCores_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         AssemblyDoc swAssemblyDoc;
         RouteManager rtRouteManager;
         ElectricalRoute rtElectricalRoute;
         Cable rtCable;
         CableProperty rtCableProperty;
         WireProperty aWireProperty;
         Wire aWire;
         int lNumCores;
         int i;
         int j;
         int k;
         object[] vCables;
         object[] vCores;
         object[] vCoreProperties;
         bool boolstatus;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\RoutingAssem1.SLDASM", 2, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("RoutingAssem1", false, ref longstatus);
             swAssemblyDoc = (AssemblyDoc)swModel;
             rtRouteManager = (RouteManager)swAssemblyDoc.GetRouteManager();
             boolstatus = swModel.Extension.SelectByID2("Harness1^RoutingAssem1-1@RoutingAssem1", "COMPONENT", 0, 0, 0, false, 0, null, 0);

             rtRouteManager.EditRoute();
             rtElectricalRoute = rtRouteManager.GetElectricalRoute();

             vCables = (object[])rtElectricalRoute.GetCables();

             if ((vCables != null))
             {
                 for (i = 0; i <= rtElectricalRoute.GetCablesCount() - 1; i++)
                 {
                     rtCable = (Cable)vCables[i];

                     Debug.Print("Cable " + rtCable.UserName);

                     vCores = (object[])rtCable.GetCores();

                     if ((vCores != null))
                     {
                         lNumCores = rtCable.GetCoresCount();

                         Debug.Print("  Cutting length: " + rtCable.GetCuttingLength());
                         rtCableProperty = rtCable.GetCableProperty();

                         Debug.Print("  Diameter: " + rtCableProperty.Diameter);
                         Debug.Print("  Name of cable library: " + rtCableProperty.Name);
                         Debug.Print("  Number of wires: " + lNumCores);
                         for (k = 0; k <= vCores.GetUpperBound(0); k++)
                         {
                             aWire = (Wire)vCores[k];
                             Debug.Print("    " + aWire.UserName);
                             aWireProperty = aWire.GetWireProperty();
                             Debug.Print("      Library name: " + aWireProperty.Name);
                         }

                         Debug.Print("");

                         vCoreProperties = (object[])rtCableProperty.GetCoreProperties();
                         for (j = 0; j <= rtCableProperty.GetCorePropertyCount() - 1; j++)
                         {
                             aWireProperty = (WireProperty)vCoreProperties[j];
                             Debug.Print("    Wire library name: " + aWireProperty.Name);
                             Debug.Print("      Color: " + aWireProperty.Color);
                             Debug.Print("      Diameter: " + aWireProperty.Diameter);
                             Debug.Print("      Part number: " + aWireProperty.PartNumber);
                             Debug.Print("      Size: " + aWireProperty.Size);
                             Debug.Print("");
                         }

                     }

                 }

             }

             rtRouteManager.ExitRoute();
             swAssemblyDoc.EditAssembly();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

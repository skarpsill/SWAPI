---
title: "Set New Route Paths for Wires Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Set_New_Route_Paths_for_Wires_Example_CSharp.htm"
---

# Set New Route Paths for Wires Example (C#)

```
This example shows how to set new route paths for wires.
```

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Add SOLIDWORKS Routing as an add-in
//   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
// 2. Add Solidworks.interop.SwRoutingLib.dll as a reference
//   (in the IDE right-click the project,
//    select Add Reference, and browse install_dir\api\redist).
// 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
// 4. Open the Immediate window.
// 5. Run the macro.
//
// Postconditions: Examine the Immediate window.
//
// NOTE: Because the assembly document is used elsewhere,
// do not save any changes when saving it.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using SolidWorks.Interop.SWRoutingLib;
using System;
using System.Diagnostics;

namespace SetRoutePathForWireCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDoc = default(ModelDocExtension);
            AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
            RouteManager rtRouteManager = default(RouteManager);
            ElectricalRoute rtElectricalRoute = default(ElectricalRoute);
            Wire rtWire = default(Wire);
            bool status = false;
            int count = 0;
            object[] wires = null;
            string cableName = null;
            double cuttingLength = 0;
            int routePathStatus = 0;
            int[] routeSegmentIDs = null;
            int routeSegmentIDsCount = 0;
            int i = 0;
            int j = 0;
            int k = 0;

            // Get the active document
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDoc = (ModelDocExtension)swModel.Extension;

            // Downcast from model document to assembly document
            swTopLevelAssembly = (AssemblyDoc)swModel;

            // Get the RouteManager from the top-level assembly
            rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();

            if (rtRouteManager == null)
            {
                Debug.Print("No RouteManager found in top-level document");
                return;
            }

            // Select and edit a route
            status = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, false, 0, null, 0);
            swModel.EditRoute();

            // Get electrical route
            rtElectricalRoute = (ElectricalRoute)rtRouteManager.GetElectricalRoute();
            if (rtElectricalRoute == null)
            {
                Debug.Print("Electrical route not found");
                return;
            }
            Debug.Print("Electrical route found");

            // Get the number of wires and get the wires
            count = rtElectricalRoute.GetWiresCount();
            Debug.Print("Number of wires: " + count);
            wires = (object[])rtElectricalRoute.GetWires();

            // For each wire...

            for (i = 0; i <= count - 1; i++)
            {
                // Get wire
                rtWire = (Wire)wires[i];
                if (rtWire == null)
                {
                    return;
                }
                Debug.Print("");
                // Get wire's cutting length and name of the cable
                cuttingLength = rtWire.GetCuttingLength();
                Debug.Print("  Cutting length: " + cuttingLength);
                cableName = rtWire.UserName;
                Debug.Print("  Cable name: " + cableName);

                // Get and set wire's route segments and their IDs
                routeSegmentIDs = (int[])rtWire.GetRouteSegmentIDs();
                routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount();
                for (j = 0; j <= routeSegmentIDsCount - 1; j++)
                {
                    Debug.Print("    Original route segmentID: " + routeSegmentIDs[j]);
                    int ID = routeSegmentIDs[j];
                    routeSegmentIDs[j] = ID - 1;
                }

                // Set new IDs for the route segments in the wire, clear
                // the previous selected route path, and create a new
                // route path for the route segments in the wire
                routePathStatus = rtWire.SetRoutePathForWire(routeSegmentIDs);
                Debug.Print("    Status of creating new route path (0 = success): " + routePathStatus);

                // Get wire's route segments and their IDs
                routeSegmentIDs = (int[])rtWire.GetRouteSegmentIDs();
                routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount();
                for (k = 0; k <= routeSegmentIDsCount - 1; k++)
                {
                    Debug.Print("    New route segment ID: " + routeSegmentIDs[k]);
                }

            }

            // Clear selection
            swModel.ClearSelection2(true);

            // Exit edit mode
            swTopLevelAssembly.EditAssembly();

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }

}
```

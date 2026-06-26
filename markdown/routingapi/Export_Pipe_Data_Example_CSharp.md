---
title: "Export Pipe Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Pipe_Data_Example_CSharp.htm"
---

# Export Pipe Data Example (C#)

This example shows how to export routing pipe data.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add SOLIDWORKS Routing as an add-in
 //     (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 // 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
 //     (in the IDE right-click the project, select Add Reference,
 //    and browse  install_dir\api\redist).
 // 3. In Tools > Options > System Options > Routing > Routing File Locations,
  //     add locations of your SOLIDWORKS Routing files.
 // 4. Open:
 //      public_documents\samples\tutorial\routing-pipes\fittings\reducerroute.sldasm.
 // 5. Select ReducerRoute, the assembly containing the route,
  //     in the FeatureManager design tree.
 // 6. Open an Immediate Window.
 // 7. Ensure that c:\temp exists.
 //
 // Postconditions: Piping data in millimeters is exported to
 //    c:\temp\reducerroute.pcf.
 //
 // NOTE: Because this assembly is used elsewhere,
 //   do not save any changes to it.
 //--------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace ExportPipeData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
             RouteManager rtRouteManager = default(RouteManager);
             int resultCode = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swTopLevelAssembly = (AssemblyDoc)swModel;

             // Get the RouteManager from the top-level assembly
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document.");
                 return;
             }

             resultCode = rtRouteManager.ExportPipeData("c:\\temp\\", 0, 0);
         }

         public SldWorks swApp;

     }
 }
```

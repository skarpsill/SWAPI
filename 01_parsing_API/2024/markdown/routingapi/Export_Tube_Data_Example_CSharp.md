---
title: "Export Tube Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Tube_Data_Example_CSharp.htm"
---

# Export Tube Data Example (C#)

This example shows how to export routing tube data.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add SOLIDWORKS Routing as an add-in
 //     (in SOLIDWORKS select  Tools > Add-Ins > SOLIDWORKS Routing).
 // 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
 //     (in the IDE right-click the project,
 //     select Add Reference, and browse install_dir\api\redist).
 // 3. In Tools > Options > System Options > Routing > Routing File Locations,
 //     add locations of your SOLIDWORKS Routing files.
 // 4. Open public_documents\samples\tutorial\api\tubing.sldasm.
 // 5. In the FeatureManager design tree select Tube1^Tubing assembly.
 // 6. Rename the namspace to match the name of your C# project.
 // 7. Open an Immediate Window.
 // 8. Ensure that c:\temp exists.
 //
 // Postconditions: Tangent bend data is exported to c:\temp\default.html.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace ExportTubeData_CSharp.csproj
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

             resultCode = rtRouteManager.ExportTubeData("c:\\temp.html", 1, 0);
         }

         public SldWorks swApp;

     }
 }
```

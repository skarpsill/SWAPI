---
title: "Merge Guidelines into a Route Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Merge_Guidelines_into_a_Route_Example_CSharp.htm"
---

# Merge Guidelines into a Route Example (C#)

This example shows how to merge guidelines into a single route.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add SOLIDWORKS Routing as an add-in
  //     (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 // 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
  //     (in the IDE right-click the project,
  //     select Add Reference, and browse  install_dir\api\redist).
 // 3. In Tools > Options > System Options > Routing > Routing File Locations,
  //     add locations of your SOLIDWORKS Routing files.
 // 4. Open an assembly that contains a route.
 // 5. Rename the namespace to match the name of your C# project.
 // 6. In the FeatureManager design tree, select the sub-assembly that
 //    contains the route.
 // 7. Open an Immediate Window.
 //
 // Postconditions: All of the guidelines are merged into a single route.
 //
 // NOTE: Because the assembly is used elsewhere,
 //   do not save any changes when you close it.
 //---------------------------------------------------------------------------

  using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace MergeGuidelines_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
             RouteManager rtRouteManager = default(RouteManager);
             AutoRoute autoRoute = default(AutoRoute);
             int resultCode = 0;
             bool boolstatus = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swTopLevelAssembly = (AssemblyDoc)swModel;

             // Get the RouteManager from the top-level assembly
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document. ");
                 return;
             }

             rtRouteManager.EditRoute();
             autoRoute = rtRouteManager.GetAutoRoute();
             resultCode = autoRoute.ShowGuidelines();

             // Select all guidelines
             resultCode = autoRoute.SelectGuidelines();
             // Merge guidelines
             boolstatus = autoRoute.MergeGuidelines();

             rtRouteManager.ExitRoute();

             swTopLevelAssembly.EditAssembly();
         }

         public SldWorks swApp;

     }
 }
```

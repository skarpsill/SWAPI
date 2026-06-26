---
title: "Create a Drawing for a Pipe Route Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_a_Drawing_for_a_Pipe_Route_Example_CSharp.htm"
---

# Create a Drawing for a Pipe Route Example (C#)

This example shows how to create a drawing of a pipe assembly.

```vb
 // --------------------------------------------------------------------------
 // Preconditions:
 // 1. Add SOLIDWORKS Routing as an add-in
 //     (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS routing).
 // 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
 //    (in the IDE right-click the project,  select Add Reference,
 //    and browse install_dir\api\redist).
 // 3. Create a piping BOM template named piping_template.sldbomtbt.
 // 4. Add a column with header "Length" to the piping BOM template.
 // 5. Ensure that the specified piping BOM and sheet format
 //    template paths exist.
 // 6. In Tools > Options > Routing > Routing File Locations,
  //    add the locations of your SOLIDWORKS Routing files.
 // 7. In Tools > Options > File Locations, add the location of
 //     your sheet  format templates.
 // 8. Open:
 //    public_documents\samples\tutorial\routing-pipes\fittings\reducerroute.sldasm
 // 9. Rename the namespace to match the name of your C# project.
 //
 // Postconditions: A drawing of the pipe assembly is created
 //  in a standard  format and includes auto balloons, a bill of
 // materials, and a route sketch.
 //
 // NOTE: Because this assembly is used elsewhere,
 //  do not save any changes to it.
 //---------------------------------------------------------------------------
  using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace CreatePipeDrawing_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         AssemblyDoc Part;

         public void Main()
         {

             Part = (AssemblyDoc)swApp.ActiveDoc;
             RouteManager RouteMgr = default(RouteManager);
             RouteMgr = (RouteManager)Part.GetRouteManager();
             string bomtemplatepath = null;
             bomtemplatepath = "Piping_BOM_template_path";
             string bomtemplatename = null;
             bomtemplatename = "piping_template.sldbomtbt";
             string sheettemplatepath = null;
             sheettemplatepath = "install_dir\\lang\\english\\sheetformat";
             string sheettemplatename = null;
             sheettemplatename = "a - landscape.slddrt";
             bool insertballoons = false;
             insertballoons = true;
             bool insertBOM = false;
             insertBOM = true;
             bool showRouteSketch = false;
             showRouteSketch = true;
             bool subAssembly = false;
             subAssembly = true;
             double userSheetWidth = 0;
             userSheetWidth = 500.0;
             double userSheetHeight = 0;
             userSheetHeight = 500.0;
             bool displayFormat = false;
             displayFormat = true;
             int dwgTemplates = 0;
             dwgTemplates = 0;

             RouteMgr.CreatePipeDrawingforPipeRoute(bomtemplatepath, bomtemplatename, insertballoons, insertBOM, showRouteSketch, subAssembly, userSheetWidth, userSheetHeight, sheettemplatepath, sheettemplatename,
             displayFormat, dwgTemplates);

         }

         public SldWorks swApp;

     }
 }
```

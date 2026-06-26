---
title: "Import a From-to List Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Import_a_From-To_List_Example_CSharp.htm"
---

# Import a From-to List Example (C#)

This example shows how to import a from-to connection list.

```vb
  //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Add SOLIDWORKS Routing as an add-in
 //    (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 // 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
  //     (in the IDE right-click the project,
  //     select Add Reference, and browse install_dir\api\redist).
 // 3. In Tools > Options > System Options > Routing > Routing File Locations,
  //     add locations of your SOLIDWORKS Routing files.
 // 4. Open:
 //    public_documents\samples\tutorial\routing\electrical\top_assy.sldasm.
 // 5. Rename the namespace to match the name of your C# project.
 // 6. Ensure that the specified files exist.
 // 7. Open an Immediate Window.
 //
 // Postconditions:
 // 1. Position the components in the harness by clicking the housing wall
  //     five (5) times.
 // 2. Click Yes in the message box.
 // 3. Click the green checkmark in Route Properties to accept the defaults.
 //    Guidelines display in the electronic housing.
 //    The Auto Route PropertyManager page displays.
 // 4. Click the green checkmark to accept the defaults.
 // 5. Stop editing the route.
 // 6. Stop editing the assembly.
 // 7. Harness_1-top_assy, containing the imported route,
  //     appears in the FeatureManager design tree.
 //
 // NOTE: Because the assembly is used elsewhere,
  //   do not save any changes when you close it.
 //--------------------------------------------------------------------------

  using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace ImportFromToList_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             AssemblyDoc swTopLevelAssembly = default(AssemblyDoc);
             RouteManager rtRouteManager = default(RouteManager);
             string fromtoListFileName = null;
             fromtoListFileName = "public_documents\\tutorial\\routing\\electrical\\from-to list.xlsx";
             string compoLibFilename = null;
             compoLibFilename = "install_dir\\data\\design library\\routing\\electrical\\components.xml";
             string cableWireLibFilename = null;
             cableWireLibFilename = "c:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 20nn\\design library\\routing\\electrical\\cable.xml";
             bool useExistingAssembly = false;
             useExistingAssembly = false;
             bool overwriteData = false;
             overwriteData = true;
             bool searchAllSubAssemblies = false;
             searchAllSubAssemblies = true;
             bool boolstatus = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swTopLevelAssembly = (AssemblyDoc)swModel;

             // Get the RouteManager from the top-level assembly
             rtRouteManager = (RouteManager)swTopLevelAssembly.GetRouteManager();
             if (rtRouteManager == null)
             {
                 Debug.Print("No RouteManager found in top-level document.");
                 return;
             }

             boolstatus = rtRouteManager.ImportFromToList(fromtoListFileName, compoLibFilename, cableWireLibFilename, useExistingAssembly, overwriteData, searchAllSubAssemblies);
         }

         public SldWorks swApp;

     }
 }
```

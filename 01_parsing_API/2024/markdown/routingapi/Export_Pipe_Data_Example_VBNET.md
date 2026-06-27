---
title: "Export Pipe Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Pipe_Data_Example_VBNET.htm"
---

# Export Pipe Data Example (VB.NET)

This example shows how to export routing pipe data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '     (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
 '     (in the IDE right-click the project,
 '      select Add Reference, and browse  install_dir\api\redist).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '      add locations of your SOLIDWORKS Routing files.
 ' 4. Open:
 '    public_documents\samples\tutorial\routing-pipes\fittings\reducerroute.sldasm
 ' 5. Select ReducerRoute, the assembly containing the route,
 '     in the FeatureManager design tree.
 ' 6. Open an Immediate Window.
 ' 7. Ensure that c:\temp exists.
 '
 ' Postconditions: Piping data in millimeters is exported to
 ' c:\temp\reducerroute.pcf.
 '
 ' NOTE: Because this assembly is used elsewhere,
 '  do not save any changes to it.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()
         Dim swModel As ModelDoc2
         Dim swTopLevelAssembly As AssemblyDoc
         Dim rtRouteManager As RouteManager
         Dim resultCode As Long

         swModel = swApp.ActiveDoc
         swTopLevelAssembly = swModel

         ' Get the RouteManager from the top-level assembly
         rtRouteManager = swTopLevelAssembly.GetRouteManager
         If rtRouteManager Is Nothing Then
             Debug.Print("No RouteManager found in top-level document.")
             Exit Sub
         End If

         resultCode = rtRouteManager.ExportPipeData("c:\temp\", 0, 0)

     End Sub

     Public swApp As SldWorks

 End  Class
```

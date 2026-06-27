---
title: "Export Tube Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Tube_Data_Example_VBNET.htm"
---

# Export Tube Data Example (VB.NET)

This example shows how to export routing tube data.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '     (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add SOLIDWORKS.interop.SwRoutingLib.dll as a reference
 '     (in the IDE right-click the project,
 '      select Add Reference, and browse  install_dir\api\redist).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '      add locations of your SOLIDWORKS Routing files.
 ' 4. Open public_documents\samples\tutorial\api\tubing.sldasm.
 ' 5. In the FeatureManager design tree select Tube1^Tubing assembly.
 ' 6. Open an Immediate Window.
 ' 7. Ensure that c:\temp exists.
 '
 ' Postconditions: Tangent bend data is exported to c:\temp\default.html.
 '--------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SwRoutingLib
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

         resultCode = rtRouteManager.ExportTubeData("c:\temp.html", 1, 0)
     End Sub

     Public swApp As SldWorks

 End   Class
```

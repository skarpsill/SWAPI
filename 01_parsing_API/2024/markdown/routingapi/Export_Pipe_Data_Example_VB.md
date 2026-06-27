---
title: "Export Pipe Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Pipe_Data_Example_VB.htm"
---

# Export Pipe Data Example (VBA)

This example shows how to export routing pipe data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
 '   (in the IDE select Tools > References).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add locations of your SOLIDWORKS Routing files.
 ' 4. Open:
 '    public_documents\samples\tutorial\routing-pipes\fittings\reducerroute.sldasm.
 ' 5. Select ReducerRoute, the assembly containing the route,
 '    in the FeatureManager design tree.
 ' 6. Open an Immediate Window.
 ' 7. Ensure that c:\temp exists.
 '
 ' Postconditions: Piping data in millimeters is exported to
 ' c:\temp\reducerroute.pcf.
 '
 ' NOTE: Because this assembly is used elsewhere,
 ' do not save any changes to it.
 '---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Option Explicit
 Sub main()
```

```vb
Dim swModel As SldWorks.ModelDoc2
Dim swTopLevelAssembly As SldWorks.AssemblyDoc
Dim swRoutingAssembly As SldWorks.AssemblyDoc
Dim rtRouteManager As SWRoutingLib.RouteManager
Dim resultCode As Long
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swTopLevelAssembly = swModel
' Get the RouteManager from the top-level assembly
Set rtRouteManager = swTopLevelAssembly.GetRouteManager
If rtRouteManager Is Nothing Then
     Debug.Print "No RouteManager found in top-level document."
     Exit Sub
End If
resultCode = rtRouteManager.ExportPipeData("c:\temp\", 0, 0)
```

```vb
End Sub
```

---
title: "Convert Guidelines into a Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Convert_Guidelines_into_a_Route_Example_VB.htm"
---

# Convert Guidelines into a Route Example (VBA)

This example shows how to convert selected guidelines into a route.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '    (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add the SOLIDWORKS  <version> Routing Type Library as a reference
 '    (in the IDE select Tools > References).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add locations of your SOLIDWORKS Routing files.
 ' 4. Open a routing assembly.
 ' 5. Select routing guidelines in the graphics area.
 ' 6. Open an Immediate Window.
 '
 ' Postconditions: The selected guidelines are converted into a route.
 '
 ' NOTE: Because the assembly is used elsewhere,
 ' do not save any changes when you close it.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks

 Sub main()
```

```vb
Dim swModel As SldWorks.ModelDoc2
Dim swTopLevelAssembly As SldWorks.AssemblyDoc
Dim rtRouteManager As SWRoutingLib.RouteManager
Dim autoRoute As SWRoutingLib.autoRoute
Dim resultCode As Long
Dim boolstatus As Boolean
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swTopLevelAssembly = swModel
' Get the RouteManager from the top-level assembly
Set rtRouteManager = swTopLevelAssembly.GetRouteManager
If rtRouteManager Is Nothing Then
     Debug.Print "No RouteManager found in top-level document."
     Exit Sub
End If
rtRouteManager.EditRoute
Set autoRoute = rtRouteManager.GetAutoRoute
resultCode = autoRoute.ShowGuidelines
' Convert guidelines to route
boolstatus = autoRoute.ConvertGuidelinesToRoute
rtRouteManager.ExitRoute
swTopLevelAssembly.EditAssembly
```

```vb
End Sub
```

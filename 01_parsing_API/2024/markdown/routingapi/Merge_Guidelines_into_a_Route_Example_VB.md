---
title: "Merge Guidelines into a Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Merge_Guidelines_into_a_Route_Example_VB.htm"
---

# Merge Guidelines into a Route Example (VBA)

This example shows how to merge guidelines into a single route.

```vb
  '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '   (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
 '   (in the IDE select Tools > References).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add locations of your SOLIDWORKS Routing files.
 ' 4. Open an assembly that contains a route.
 ' 5. In the FeatureManager design tree, select the sub-assembly that
 '    contains the route.
 '
 ' Postconditions: All of the guidelines are merged into a single route.
 '
 ' NOTE: Because the assembly is used elsewhere,
 ' do not save any changes when you close it.
 '---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Option Explicit
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
' Select all guidelines
resultCode = autoRoute.SelectGuidelines
' Merge guidelines
boolstatus = autoRoute.MergeGuidelines
rtRouteManager.ExitRoute
swTopLevelAssembly.EditAssembly
```

```vb
End Sub
```

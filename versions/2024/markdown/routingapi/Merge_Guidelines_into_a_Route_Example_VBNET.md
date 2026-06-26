---
title: "Merge Guidelines into a Route Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Merge_Guidelines_into_a_Route_Example_VBNET.htm"
---

# Merge Guidelines into a Route Example (VB.NET)

This example shows how to merge guidelines into a single route.

```vb
  '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
  '     (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add SolidWorks.Interop.SwRoutingLib.dll as a reference
  '     (in the IDE right-click the project,
  '      select Add Reference, and browse  install_dir\api\redist).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
  '      add locations of your SOLIDWORKS Routing files.
 ' 4. Open an assembly with a route.
 ' 5. In the FeatureManager design tree, select the sub-assembly that
 '    contains the route.
 ' 6. Open an Immediate Window.
 '
 ' Postconditions: All of the guidelines are merged into a single route.
 '
 ' NOTE: Because the assembly is used elsewhere,
 '   do not save any changes when you close it.
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
         Dim autoRoute As AutoRoute
         Dim resultCode As Long
         Dim boolstatus As Boolean

         swModel = swApp.ActiveDoc
         swTopLevelAssembly = swModel

         ' Get the RouteManager from the top-level assembly
         rtRouteManager = swTopLevelAssembly.GetRouteManager
         If rtRouteManager Is Nothing Then
             Debug.Print("No RouteManager found in top-level document. ")
             Exit Sub
         End If

         rtRouteManager.EditRoute()
         autoRoute = rtRouteManager.GetAutoRoute
         resultCode = autoRoute.ShowGuidelines

         ' Select all guidelines
         resultCode = autoRoute.SelectGuidelines
         ' Merge guidelines
         boolstatus = autoRoute.MergeGuidelines

         rtRouteManager.ExitRoute()
         swTopLevelAssembly.EditAssembly()

     End Sub

     Public swApp As SldWorks

 End  Class
```

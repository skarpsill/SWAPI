---
title: "Start Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Start_Route_Example_VB.htm"
---

# Start Route Example (VBA)

This example shows how to start a route using a selected routing component.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in (select Tools > Add-Ins > SOLIDWORKS
'    Routing in SOLIDWORKS).
' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
'    (select Tools > References in the IDE).
' 3. In Tools > Options > System Options > Routing > Routing File Locations,
'    add the locations of your SOLIDWORKS Routing files.
' 4. Press F5 to run the macro.
'
' Postconditions:
' 1. When the macro stops, click the green checkmark in the Route
'    Properties PropertyManager page to create the route.
' 2. A route is added to the assembly. To verify, expand
'    Pipe_1StartRoute and locate the Route1 feature in the
'    FeatureManager design tree.
'
' NOTE: Because the models are used elsewhere,
' do not save changes when closing the models.
' ---------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim SwApp               As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel         As SldWorks.ModelDoc2
    Dim swAssembly      As SldWorks.AssemblyDoc
    Dim swModelDocExt   As SldWorks.ModelDocExtension
    Dim swRouteMgr      As SWRoutingLib.RouteManager
    Dim status          As Boolean
    Dim warnings        As Long
    Dim errors          As Long
    Dim fileName        As String
```

```
    ' Connect to SOLIDWORKS
    Set SwApp = Application.SldWorks
    If SwApp Is Nothing Then Exit Sub
```

```
    ' Open the assembly and make it the active document
    fileName = "public_documents\tutorial\api\StartRoute.sldasm"
    SwApp.OpenDoc6 fileName, swDocASSEMBLY, swOpenDocOptions_Silent, "Default", errors, warnings
    Set swModel = SwApp.ActiveDoc
    Set swAssembly = swModel
    Set swModelDocExt = swModel.Extension
```

```
    ' Get the RouteManager
    Set swRouteMgr = swAssembly.GetRouteManager
```

```
    ' Select slip on weld flange component
    status = swModelDocExt.SelectByID2("slip on weld flange-1@MyStartRoute", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Start the route
    status = swRouteMgr.StartRoute("", "")
```

```
    ' In SOLIDWORKS, click the green check mark in the Route
    ' Properties PropertyManager page to create the route
```

```
    ' Exit the route from edit mode
    swRouteMgr.ExitRoute
```

```
    ' Exit editing the assembly
    swModel.EditAssembly
```

```
    swModel.ViewZoomtofit
```

```
End Sub
```

---
title: "Add to Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Add_to_Route_Example_VB.htm"
---

# Add to Route Example (VBA)

This example shows how to add to a route.

```vb
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
 ' 1. The routing assembly component is added to the route at
 '    CPoint1 and CPoint3 on the straight cross inch pipe component.
 ' 2. The routing assembly component is added to the reducing outlet cross inch
 '    component.
 '
 ' NOTE: Because the models are used elsewhere,
 ' do not save changes when closing the models.
 ' ---------------------------------------------------------------------------
 Option Explicit

 Dim swApp               As SldWorks.SldWorks
```

```
Sub main()

    Dim swModel         As SldWorks.ModelDoc2
    Dim swAssembly      As SldWorks.AssemblyDoc
    Dim swRouteMgr      As SWRoutingLib.RouteManager
    Dim swModelDocExt   As SldWorks.ModelDocExtension
    Dim boolstatus      As Boolean
    Dim errors          As Long
    Dim warnings        As Long
    Dim fileName        As String
```

```
    Set swApp = Application.SldWorks
    If swApp Is Nothing Then Exit Sub
```

```
    ' Open assembly document and make it the active document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\AddtoRoute.sldasm"
    swApp.OpenDoc6 fileName, swDocASSEMBLY, swOpenDocOptions_Silent, "Default", errors, warnings
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
```

```
    ' Get the RouteManager
    Set swRouteMgr = swAssembly.GetRouteManager
```

```
    swModel.ClearSelection2 True
```

```
   ' Select the routing assembly component to add to the route
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Route1@Pipe_2^AddToRoute-1@AddToRoute", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Put the route in edit mode
    swRouteMgr.EditRoute
```

```
    swModel.ClearSelection2 True
```

```
   ' Select the connection points where to add the routing assembly component
    boolstatus = swModelDocExt.SelectByID2("CPoint3@Pipe_2^AddToRoute-1@AddToRoute/straight cross inch-1@Pipe_2^AddToRoute", "CONNECTIONPOINT", 0#, 0#, 0#, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("CPoint1@Pipe_2^AddToRoute-1@AddToRoute/straight cross inch-1@Pipe_2^AddToRoute", "CONNECTIONPOINT", 0#, 0#, 0#, True, 0, Nothing, 0)
```

```
    ' Add to the route
    boolstatus = swRouteMgr.AddToRoute()
```

```
    swModel.ClearSelection2 True
```

```
    ' Select the assembly component where to add the routing assembly component
    boolstatus = swModelDocExt.SelectByID2("reducing outlet cross inch-1@AddToRoute", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Add to the route
    boolstatus = swRouteMgr.AddToRoute()
```

```
    ' Exit the route from edit mode
    swRouteMgr.ExitRoute
```

```
    ' Exit editing the assembly
    swAssembly.EditAssembly
```

```
    swModel.ViewZoomtofit
```

```
End Sub
```

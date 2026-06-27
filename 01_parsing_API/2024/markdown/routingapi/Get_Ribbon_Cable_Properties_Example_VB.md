---
title: "Get Ribbon Cable Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Ribbon_Cable_Properties_Example_VB.htm"
---

# Get Ribbon Cable Properties Example (VBA)

This example shows how to get ribbon cable properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 2. In Tools > Options > System Options > Routing > Routing File Locations,
 '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 3. In the IDE, click Tools > References, select
 '    SOLIDWORKS version Routing Type Library, and click OK.
 ' 4. Open an electrical routing assembly that has a ribbon cable.
 ' 5. In the FeatureManager design tree, select the component that contains the
 '    electrical route.
 ' 6. Open an Immediate window.
 '
 ' Postconditions: Prints the thickness and width of the ribbon cable to the
 ' Immediate window.
 '----------------------------------------------------------------------------
 Option Explicit
     Dim swApp                As SldWorks.SldWorks
     Dim swModel              As SldWorks.ModelDoc2
     Dim swTopLevelAssembly   As SldWorks.AssemblyDoc
     Dim rtRouteManager       As SWRoutingLib.RouteManager
     Dim rtRibbonCable        As SWRoutingLib.RibbonCable
     Dim rtElectRoute         As SWRoutingLib.ElectricalRoute

Sub Main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swTopLevelAssembly = swModel
     Set rtRouteManager = swTopLevelAssembly.GetRouteManager
     If rtRouteManager Is Nothing Then
         Debug.Print "No RouteManager found in top-level document: " & swModel.GetPathName
         Exit Sub
     End If
    Set rtElectRoute = rtRouteManager.GetElectricalRoute
        If Not rtElectRoute Is Nothing Then
            Set rtRibbonCable = rtElectRoute.GetRibbonCableDispatch

            Debug.Print "Ribbon cable"
             Debug.Print " Thickness: " & rtRibbonCable.GetRibbonCableThickness
             Debug.Print " Width: " & rtRibbonCable.GetRibbonCableWidth

        End If
End Sub
```

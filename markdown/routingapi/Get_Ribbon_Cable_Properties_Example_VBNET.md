---
title: "Get Ribbon Cable Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Ribbon_Cable_Properties_Example_VBNET.htm"
---

# Get Ribbon Cable Properties Example (VB.NET)

This example shows how to get ribbon cable properties.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 2. In Tools > Options > System Options > Routing > Routing File Locations,
 '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 3. In the IDE, right-click the project,
 '    click Add Reference, browse install_dir\api\redist, click
 '    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
  ' 4. Open an electrical routing assembly that has a ribbon cable.
 ' 5. In the FeatureManager design tree, select the component that contains the
 '    electrical route.
 ' 6. Open an Immediate window.
 '
 ' Postconditions: Prints the thickness and width of the ribbon cable to the
 ' Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swTopLevelAssembly As AssemblyDoc
     Dim rtRouteManager As RouteManager
     Dim rtRibbonCable As RibbonCable
     Dim rtElectRoute As ElectricalRoute

     Sub Main()

         swModel = swApp.ActiveDoc
         swTopLevelAssembly = swModel
         rtRouteManager = swTopLevelAssembly.GetRouteManager
         If rtRouteManager Is Nothing Then
             Debug.Print("No RouteManager found in top-level document: " & swModel.GetPathName)
             Exit Sub
         End If

         rtElectRoute = rtRouteManager.GetElectricalRoute

         If Not rtElectRoute Is Nothing Then

             rtRibbonCable = rtElectRoute.GetRibbonCableDispatch

             Debug.Print("Ribbon cable")
             Debug.Print(" Thickness: " & rtRibbonCable.GetRibbonCableThickness)
             Debug.Print(" Width: " & rtRibbonCable.GetRibbonCableWidth)

         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

---
title: "Get Cable Cores Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_Cores_Example_VBNET.htm"
---

# Get Cable Cores Example (VB.NET)

This example shows how to get the cores of cables.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly exists.
 ' 2. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
  ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
  '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 4. In the IDE, right-click the project,
 '    click Add Reference, browse install_dir\api\redist, click
 '    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified assembly.
 ' 2. Selects Harness1^RoutingAssem1-1.
 ' 3. Gets the cables in the electrical route.
  ' 4. Prints the number of wires and the properties of each wire in the cable.
 ' 5. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swAssemblyDoc As AssemblyDoc
     Dim rtRouteManager As RouteManager
     Dim rtElectricalRoute As ElectricalRoute
     Dim rtCable As Cable
     Dim rtCableProperty As CableProperty
     Dim aWireProperty As WireProperty
     Dim aWire As Wire
     Dim lNumCores As Integer
     Dim i As Integer
     Dim j As Integer
     Dim k As Integer
     Dim vCables As Object
     Dim vCores As Object
     Dim vCoreProperties As Object
     Dim boolstatus As Boolean
     Dim longstatus As Integer
     Dim longwarnings As Integer

     Sub main()

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\RoutingAssem1.SLDASM", 2, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("RoutingAssem1", False, longstatus)
         swAssemblyDoc = swModel
         rtRouteManager = swAssemblyDoc.GetRouteManager()
         boolstatus = swModel.Extension.SelectByID2("Harness1^RoutingAssem1-1@RoutingAssem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

         rtRouteManager.EditRoute()
         rtElectricalRoute = rtRouteManager.GetElectricalRoute

         vCables = rtElectricalRoute.GetCables

         If Not IsNothing(vCables) Then

             For i = 0 To rtElectricalRoute.GetCablesCount - 1
                 rtCable = vCables(i)

                 Debug.Print("Cable " & rtCable.UserName)

                 vCores = rtCable.GetCores

                 If Not IsNothing(vCores) Then

                     lNumCores = rtCable.GetCoresCount

                     Debug.Print("  Cutting length: " & rtCable.GetCuttingLength)
                     rtCableProperty = rtCable.GetCableProperty

                     Debug.Print("  Diameter: " & rtCableProperty.Diameter)
                     Debug.Print("  Name of cable library: " & rtCableProperty.Name)
                     Debug.Print("  Number of wires: " & lNumCores)
                     For k = 0 To UBound(vCores)
                         aWire = vCores(k)
                         Debug.Print("    " & aWire.UserName)
                         aWireProperty = aWire.GetWireProperty
                         Debug.Print("      Library name: " & aWireProperty.Name)
                     Next k

                     Debug.Print("")

                     vCoreProperties = rtCableProperty.GetCoreProperties
                     For j = 0 To rtCableProperty.GetCorePropertyCount - 1
                         aWireProperty = vCoreProperties(j)
                         Debug.Print("    Wire library name: " & aWireProperty.Name)
                         Debug.Print("      Color: " & aWireProperty.Color)
                         Debug.Print("      Diameter: " & aWireProperty.Diameter)
                         Debug.Print("      Part number: " & aWireProperty.PartNumber)
                         Debug.Print("      Size: " & aWireProperty.Size)
                         Debug.Print("")
                     Next j

                 End If

             Next i

         End If

         rtRouteManager.ExitRoute()
         swAssemblyDoc.EditAssembly()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

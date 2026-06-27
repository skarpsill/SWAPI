---
title: "Set New Route Paths for Wires Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Set_New_Route_Paths_for_Wires_Example_VBNET.htm"
---

# Set New Route Paths for Wires Example (VB.NET)

```
This example shows how to set new route paths for wires.
```

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add Solidworks.interop.SwRoutingLib.dll as a reference
'   (in the IDE right-click the project,
'    select Add Reference, and browse install_dir\api\redist).
' 3. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do
' not save any changes when saving it.
'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports SolidWorks.Interop.SWRoutingLib
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDoc As ModelDocExtension
        Dim swTopLevelAssembly As AssemblyDoc
        Dim rtRouteManager As RouteManager
        Dim rtElectricalRoute As ElectricalRoute
        Dim rtWire As Wire
        Dim status As Boolean
        Dim count As Integer
        Dim wires As Object
        Dim cableName As String
        Dim cuttingLength As Double
        Dim routePathStatus As Integer
        Dim routeSegmentIDs As Object
        Dim routeSegmentIDsCount As Long
        Dim i As Integer
        Dim j As Integer
        Dim k As Integer

        ' Get the active document
        swModel = swApp.ActiveDoc
        swModelDoc = swModel.Extension

        ' Downcast from model document to assembly document
        swTopLevelAssembly = swModel

        ' Get the RouteManager from the top-level assembly
        rtRouteManager = swTopLevelAssembly.GetRouteManager

        If rtRouteManager Is Nothing Then
            Debug.Print("No RouteManager found in top-level document")
            Exit Sub
        End If

        ' Select and edit a route
        status = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditRoute()

        ' Get electrical route
        rtElectricalRoute = rtRouteManager.GetElectricalRoute
        If rtElectricalRoute Is Nothing Then
            Debug.Print("Electrical route not found")
            Exit Sub
        End If
        Debug.Print("Electrical route found")

        ' Get the number of wires and get the wires
        count = rtElectricalRoute.GetWiresCount
        Debug.Print("Number of wires: " & count)
        wires = rtElectricalRoute.GetWires

        ' For each wire...
        For i = 0 To count - 1

            ' Get wire
            rtWire = wires(i)
            If rtWire Is Nothing Then
                Exit Sub
            End If
            Debug.Print("")
            ' Get wire's cutting length and name of the cable
            cuttingLength = rtWire.GetCuttingLength
            Debug.Print("  Cutting length: " & cuttingLength)
            cableName = rtWire.UserName
            Debug.Print("  Cable name: " & cableName)

            ' Get and set wire's route segments and their IDs
            routeSegmentIDs = rtWire.GetRouteSegmentIDs
            routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount
            For j = 0 To routeSegmentIDsCount - 1
                Debug.Print("    Original route segment ID: " & routeSegmentIDs(j))
                routeSegmentIDs(j) = routeSegmentIDs(j) - 1
            Next j

            ' Set new IDs for the route segments in the wire, clear
            ' the previous selected route path, and create a new
            ' route path for the route segments in the wire
            routePathStatus = rtWire.SetRoutePathForWire(routeSegmentIDs)
            Debug.Print("  Status of creating new route path (0 = success): " & routePathStatus)

            ' Get the wire's route segments and their IDs
            routeSegmentIDs = rtWire.GetRouteSegmentIDs
            routeSegmentIDsCount = rtWire.GetRouteSegmentIDsCount
            For k = 0 To routeSegmentIDsCount - 1
                Debug.Print("    New route segment ID: " & routeSegmentIDs(k))
            Next k

        Next i

        ' Clear selection
        swModel.ClearSelection2(True)

        ' Exit edit mode
        swTopLevelAssembly.EditAssembly()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```

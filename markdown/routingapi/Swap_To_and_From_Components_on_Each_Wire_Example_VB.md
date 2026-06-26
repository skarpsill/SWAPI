---
title: "Swap To and From Components on Each Wire Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm"
---

# Swap To and From Components on Each Wire Example (VBA)

This example shows how to swap the "to" and "from"
components on each wire.

'--------------------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. Open an assembly document that contains a routing assembly.
'kadov_tag{{<spaces>}}2. Select a component
representing a routing assembly.
'
' Postconditions: "To" and "from"
components are swapped.
'--------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swTopLevelAssemblykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swRoutingAssemblykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtRouteManagerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.RouteManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swComponentkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtElectricalRoutekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.ElectricalRoute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetValkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vWireskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vWirekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
rtWirekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWRoutingLib.Wire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strNewWireNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strNewToComponentkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strNewFromComponentkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strNewToPinkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
strNewFromPinkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Downcast from model document to assembly document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTopLevelAssembly = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the component that represents a routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swComponent = swModel.SelectionManager.GetSelectedObject6(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
swComponent Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No component selected."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the assembly document for this component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swRoutingAssembly = swComponent.GetModelDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the RouteManager from the routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtRouteManager = swRoutingAssembly.GetRouteManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtRouteManager Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No route manager found in sub-assembly document: " & swRoutingAssembly.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Subkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Must be editing component for route properties to be available

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear selection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make sure that the component representing the routing assembly is selected

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRetVal
= swComponent.Select3(True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Start editing the routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTopLevelAssembly.EditAssembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the electrical route

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtElectricalRoute = rtRouteManager.GetElectricalRoute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Check for an electrical route

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtElectricalRoute Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No electrical route found."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Electrical route found."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Swap "to" and "from" component on each wire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the wires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vWires
= rtElectricalRoute.GetWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Loop over the wires.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vWires) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vWire In vWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtWire = vWire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
(Not rtWire Is Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Give the wire a new name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strNewWireName
= rtWire.UserName& "-swapped"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtWire.UserName= strNewWireName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Swap references

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strNewToComponent
= rtWire.FromComponentReference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strNewToPin
= rtWire.FromPinReference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strNewFromComponent
= rtWire.ToComponentReference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strNewFromPin
= rtWire.ToPinReference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtWire.FromComponentReference= strNewFromComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtWire.FromPinReference= strNewFromPin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtWire.ToComponentReference= strNewToComponent

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rtWire.ToPinReference= strNewToPin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
vWire

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Commit the changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRetVal
= rtElectricalRoute.RouteWires

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
bRetVal = False Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Routing of wires failed."kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Elsekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Routing of wires successful."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Return to editing the top-level assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTopLevelAssembly.EditAssembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

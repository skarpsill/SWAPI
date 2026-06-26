---
title: "Get RouteManager and Electrical Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_RouteManager_and_Electrical_Route_Example_VB.htm"
---

# Get RouteManager and Electrical Route Example (VBA)

This example shows how to get the RouteManager from an assembly and then how to get the electrical route.

'----------------------------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. Open an assembly document that contains a routing assembly.
'kadov_tag{{<spaces>}}2. Select a component
representing a routing assembly.
'
' Postconditions: None
'---------------------------------------------------------------------------

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
Booleankadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Downcast from model document to assembly document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTopLevelAssembly = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the component that represents a routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swComponent = swModel.SelectionManager.**GetSelectedObject6**(1, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
swComponent Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No component selected"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the assembly document for this component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swRoutingAssembly = swComponent.**GetModelDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the RouteManager from the routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtRouteManager = swRoutingAssembly.**GetRouteManager**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtRouteManager Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No RouteManager found in sub-assembly document: " & swRoutingAssembly.**GetPathName**

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.**ClearSelection2**True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make sure the component representing the routing assembly is selected

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRetVal
= swComponent.**Select3**(True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Start editing the routing assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTopLevelAssembly.**EditAssembly**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the electrical route

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
rtElectricalRoute = rtRouteManager.GetElectricalRoute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Check for an electrical route

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
rtElectricalRoute Is Nothing Thenkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No electrical route found."kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Elsekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Electrical route found."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Number of cables = " & rtElectricalRoute.GetCablesCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Number of wireskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & rtElectricalRoute.GetWiresCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Make edits ...

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Return to editing the top-level assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTopLevelAssembly.**EditAssembly**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub

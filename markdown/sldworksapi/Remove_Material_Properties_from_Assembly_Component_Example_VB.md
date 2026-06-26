---
title: "Remove Material Properties from Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Material_Properties_from_Assembly_Component_Example_VB.htm"
---

# Remove Material Properties from Assembly Component Example (VBA)

This example shows how to remove the material properties from the selected
assembly component.

'--------------------------------------------

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Assembly
is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Component
with changed material properties (for example, color)

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}is
selected.

'

' Postconditions:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Material
properties from selected component are removed.

'

'--------------------------------------------

Option Explicit

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCompkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Component2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfigkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Configuration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vConfigNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swComp = swSelMgr.GetSelectedObjectsComponent2(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the names of the configurations in the assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vConfigName
= swModel.GetConfigurationNames

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Remove the material properties from the selected

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
component in this configuration in this assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swComp.RemoveMaterialProperty2(swThisConfiguration,
(vConfigName))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
(" Material removed: "); bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2

End Sub

'-----------------------------------------

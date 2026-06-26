---
title: "Get Dimension Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_Example_VB.htm"
---

# Get Dimension Values Example (VBA)

This example shows how to get the dimension values in all configurations
of a model.

'----------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Model document with dimensions is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Dimension is selected.

'

' Postconditions: None

'

'-----------------------------------------

Option Explicit

Public Enum swDimensionDrivenState_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDimensionDrivenUnknown
= 0kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the driven/driving
state is unknown

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDimensionDriven
= 1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the dimension
is a driven dimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDimensionDriving
= 2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the dimension
is a driving dimension

End Enum

Public Enum swInConfigurationOpts_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swConfigPropertySuppressFeatures
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swThisConfiguration
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAllConfiguration
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSpecifyConfiguration
= 3

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfigMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ConfigurationManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfigkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Configuration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDispDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DisplayDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Dimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vConfigNameArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vConfigNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDimValArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDimValkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sSpecConfigNameArr(0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSpecConfigNameArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dimValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swConfigMgr = swModel.ConfigurationManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swConfig = swConfigMgr.ActiveConfiguration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDispDim = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDim = swDispDim.GetDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vConfigNameArr
= swModel.GetConfigurationNames

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName& "<" & swConfig.Name& ">"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swDim.FullName& "
[" & swDim.Name&
"]"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dimValue
= swDim.GetSystemValue3(swThisConfiguration,
vConfigNameArr(0))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SystemValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & dimValue(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IsAppliedToAllConfigurationskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.IsAppliedToAllConfigurations

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DrivenStatekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.DrivenState

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IsReferencekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.IsReference

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReadOnlykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.ReadOnly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vConfigName In vConfigNameArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sSpecConfigNameArr(0)
= vConfigName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSpecConfigNameArr
= sSpecConfigNameArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vDimValArr
= swDim.GetValue3(swSpecifyConfiguration,
vSpecConfigNameArr): Debug.Assert 0 = UBound(vDimValArr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vDimVal In vDimValArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& vConfigName & " --> " & vDimVal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
vDimVal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
vConfigName

End Sub

'----------------------------------------

---
title: "Get Custom Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_Example_VB.htm"
---

# Get Custom Properties Example (VBA)

This example shows how to get the custom properties for the configurations
in a document.

'---------------------------------------------

Option Explicit

Public Enum swCustomInfoType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustomInfoUnknown
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustomInfoText
= 30kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VT_LPSTR

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustomInfoDate
= 64kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VT_FILETIME

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustomInfoNumber
= 3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VT_I4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCustomInfoYesOrNo
= 11kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VT_BOOL

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swConfigkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Configuration

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vConfNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPropNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPropValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPropTypekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nNumPropkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
jkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " + swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vConfName
= swModel.GetConfigurationNames

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vConfName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swConfig = swModel.GetConfigurationByName(vConfName(i))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumProp
= swConfig.GetCustomProperties(vPropName,
vPropValue, vPropType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Configkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vConfName(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = 0 To nNumProp - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& vPropName(j) & " <" & vPropType(j) & ">
= " & vPropValue(j)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}---------------------------"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

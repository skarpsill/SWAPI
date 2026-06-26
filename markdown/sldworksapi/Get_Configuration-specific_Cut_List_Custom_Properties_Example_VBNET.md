---
title: "Get Configuration-specific Cut List Custom Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration-specific_Cut_List_Custom_Properties_Example_VBNET.htm"
---

# Get Configuration-specific Cut List Custom Properties Example (VB.NET)

This example shows how to get configuration-specific cut list custom
properties.

'================================================================

'Preconditions:

' 1. Open a part that
has one or more configuration-specific cut lists with custom properties.

' (Or ask SOLIDWORKS API Support to send you the models that work
with this ICutListItem sample code.)

' 2. Open an
Immediate/Output window.

'Postconditions: Inspect
all the configurations' cut lists' custom properties in the
Immediate/Output window.

'=============================================================

ImportsSolidWorks.Interop.sldworks

ImportsSolidWorks.Interop.swconst

ImportsSystem.Runtime.InteropServices

ImportsSystem

PartialClassSolidWorksMacro

DimswModelAsModelDoc2

DimvConfigNameArr()AsObject

DimvConfigNameAsString

DimvcutlistItems()AsObject

DimvcutlistItemAsCutListItem

DimcutlistItemAsCutListItem

DimcusPropMgrAsCustomPropertyManager

DimconfigAsConfiguration

DimlRetValAsInteger

DimvPropNames()AsString

DimvPropTypes()AsInteger

DimvPropValues()AsString

Dimresolved()AsInteger

DimlinkProp()AsInteger

DimiAsInteger

DimjAsInteger

DimpropNameAsString

PublicSubmain()

swModel = swApp. ActiveDoc

vConfigNameArr = swModel. GetConfigurationNames ()

ForEachvConfigNameInvConfigNameArr

Debug.Print("Configuration:
"& vConfigName)

config = swModel. GetConfigurationByName (vConfigName)

vcutlistItems = config. GetCutListItems ()

i = 1

ForEachvcutlistItemInvcutlistItems

Debug.Print("Cut
list item #"& i &" custom properties:")

cutlistItem = vcutlistItem

cusPropMgr = cutlistItem. CustomPropertyManager ()

lRetVal = cusPropMgr. GetAll3 (vPropNames,
vPropTypes, vPropValues, resolved, linkProp)

j = 0

ForEachpropNameInvPropNames

Debug.Print("
"& propName &" "& vPropValues(j))

j = j + 1

Next

i = i + 1

Next

Next

EndSub

'''<summary>

'''The SldWorks swApp variable is
pre-assigned for you.

'''</summary>

PublicswAppAsSldWorks

EndClass

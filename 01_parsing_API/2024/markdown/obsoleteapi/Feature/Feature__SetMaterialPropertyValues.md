---
title: "Feature::SetMaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__SetMaterialPropertyValues.htm"
---

# Feature::SetMaterialPropertyValues

This method is obsolete and has been superseded
by[Feature::SetMaterialPropertyValues2](sldworksAPI.chm::/Feature/Feature__SetMaterialPropertyValues2.htm).

Description

This
method sets the material properties for this feature. The material values
include the face color (R,G,B values), reflectivity (ambient, diffuse,
specular, shininess), transparency and emission. Valid values are from
0 to 1 for all variables.

Syntax (OLE Automation)

retval
= Feature.SetMaterialPropertyValues ( MaterialPropertyValues)

(Table)=========================================================

| Input: | (VARIANT)
MaterialPropertyValues | Property
values of the material for this feature |
| --- | --- | --- |
| Return: | (VARIANT_BOOL)
retval | TRUE
if the material property values were set successfully, FALSE if not |

Syntax (COM)

status
= Feature->ISetMaterialPropertyValues ( MaterialPropertyValues, &retval
)

(Table)=========================================================

| Input: | (double*)
MaterialPropertyValues | Property
values of the material for this feature |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the material property values were set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The format of the variant is an array of doubles as follows:

[ R, G, B,Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

To reset the feature to use the default part material properties, refer
to ModelDoc2::SelectedFeatureProperties

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Feature_Object$$**$$MaterialPropertyValues$$**$$ZModifyFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__SetMaterialPropertyValues.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

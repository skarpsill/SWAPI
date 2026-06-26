---
title: "Feature::GetMaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetMaterialPropertyValues.htm"
---

# Feature::GetMaterialPropertyValues

This method is obsolete and has been superseded
by[Feature::GetMaterialPropertyValues2](sldworksAPI.chm::/Feature/Feature__GetMaterialPropertyValues2.htm).

Description

This
method gets the material properties for this feature. The material values
returned include the face color (R,G,B values), reflectivity (ambient,
diffuse, specular, shininess), transparency and emission. Valid values
are from 0 to 1 for all variables.

Syntax (OLE Automation)

retval
= Feature.GetMaterialPropertyValues ()

(Table)=========================================================

| Return: | (VARIANT)
retval | Property
values of the material for this feature (see below) |
| --- | --- | --- |

Syntax (COM)

status
= Feature->IGetMaterialPropertyValues ( retval )

(Table)=========================================================

| Output: | (double*)
retval | Array
of doubles describing the material values (see below) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method returns NULL if this feature was not explicitly modified
from the material property values of the body. If you create a body and
change the body color to red, then Feature::GetMaterialPropertyValues
returns a NULL array because you did not specifically change the values
of the feature.

The format of the return value is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular,
Shininess, Transparency, Emission ]

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
<param name="Items" value="Feature_Object$$**$$MaterialPropertyValues$$**$$ZGetInfoFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Feature\Feature__GetMaterialPropertyValues.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "Body::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__MaterialPropertyValues.htm"
---

# Body::MaterialPropertyValues

This property is obsolete and has been superseded
by[Body2::MaterialPropertyValues](../Body2/Body2__MaterialPropertyValues.htm).

Description

This property gets or sets the material properties for a body other
than the base body.

Syntax (OLE Automation)

MaterialPropertyValues = Body.MaterialPropertyValues (VB
Get property)

Body.MaterialPropertyValues = MaterialPropertyValues (VB
Set property)

MaterialPropertyValues = Body.GetMaterialPropertyValues
( ) (C++ Get property)

Body.SetMaterialPropertyValues ( MaterialPropertyValues
) (C++ Set property)

(Table)=========================================================

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Body->get_IMaterialPropertyValues(MaterialPropertyValues)

status = Body->put_IMaterialPropertyValues
(MaterialPropertyValues)

(Table)=========================================================

| Property: | (double*) values | Array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This property is intended to be used on bodies
other than the base body and should follow a call to PartDoc::EnumRelatedBodies.

The material values include the face color (R,G,B
values), reflectivity (ambient, diffuse, specular, shininess), transparency,
and emission. Valid settings are from 0 to 1 for all values. The format
of the parameters or return values is an array of 9 doublesas follows:

[R, G, B, Ambient, Diffuse, Specular,
Shininess, Transparency, Emission]

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$MaterialPropertyValues$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Body\Body__MaterialPropertyValues.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

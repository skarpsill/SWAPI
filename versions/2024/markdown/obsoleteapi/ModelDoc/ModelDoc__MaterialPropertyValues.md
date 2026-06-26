---
title: "ModelDoc::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__MaterialPropertyValues.htm"
---

# ModelDoc::MaterialPropertyValues

This
property is obsolete and has been superseded by[ModelDoc2::MaterialPropertyValues](sldworksAPI.chm::/ModelDoc2/ModelDoc2__MaterialPropertyValues.htm).

Description

This method gets or sets a material's properties.

Syntax (OLE Automation)

MaterialPropertyValues = ModelDoc.MaterialPropertyValues (VB
Get property)

ModelDoc.MaterialPropertyValues = MaterialPropertyValues (VB
Set property)

MaterialPropertyValues = ModelDoc.GetMaterialPropertyValues
( ) (C++ Get property)

ModelDoc.SetMaterialPropertyValues
( MaterialPropertyValues ) (C++ Set property)

(Table)=========================================================

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles, describing the material's values |
| --- | --- | --- |

Syntax (Com)

status = ModelDoc->get_IMaterialPropertyValues(
MaterialPropertyValues )

status = ModelDoc.put_IMaterialPropertyValues
( MaterialPropertyValues )

(Table)=========================================================

| Property: | (double*) MaterialPropertyValues | Array of doubles describing the material's values |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the parameters or return values is an array of doublesas follows:

[R, G, B, Ambient, Diffuse, Specular,
Shininess, Transparency, Emission]

All elements must be in the range 0 to 1.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__MaterialPropertyValues.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

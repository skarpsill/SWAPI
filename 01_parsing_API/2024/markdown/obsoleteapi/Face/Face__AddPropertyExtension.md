---
title: "Face::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__AddPropertyExtension.htm"
---

# Face::AddPropertyExtension

This
method is obsolete and has been superseded by[Face2::AddPropertyExtension](sldworksAPI.chm::/Face2/Face2__AddPropertyExtension.htm).

Description

This method allows you to store a float, string, or integer value on
a face. To do this, you must first define the VARIANT type (float, string,
or integer), give your variable a value, and then call this method to
place the value on the face for future reference.

Syntax (OLE Automation)

retval = Face.AddPropertyExtension
( PropertyExtension)

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you want to store on the face |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the property extension |

Syntax
(COM)

status
= Face->AddPropertyExtension ( PropertyExtension, &retval )

(Table)=========================================================

| Input: | (VARIANT)
PropertyExtension | Value you want to store on the face |
| --- | --- | --- |
| Output: | (long*)
retval | Unique
identifier returned to allow you to access the property extension |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter classes instead of this
method. These classes are newer and provide more flexibility.

Please note that this method is currently unsupported for faces obtained
from reference surface bodies.

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
<param name="Items" value="Face_Object$$**$$Face::GetPropertyExtension$$**$$Attribute_Object$$**$$AttributeDef_Object$$**$$Parameter_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__AddPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

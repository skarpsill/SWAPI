---
title: "Face::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetPropertyExtension.htm"
---

# Face::GetPropertyExtension

This
method is obsolete and has been superseded by[Face2::GetPropertyExtension](sldworksAPI.chm::/Face2/Face2__GetPropertyExtension.htm).

Description

This method gets a float, string, or integer value from a face.

Syntax (OLE Automation)

retval
= Face.GetPropertyExtension ( Id )

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT)
retval | Value
stored using Face::AddPropertyExtension |

Syntax (COM)

status
= Face->GetPropertyExtension ( Id, &retval )

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT)
retval | Value
stored using Face::AddPropertyExtension |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter classes instead of this
method. These classes are newer and provide more flexibility.

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
<param name="Items" value="Face_Object$$**$$Face::AddPropertyExtension$$**$$Attribute_Object$$**$$AttributeDef_Object$$**$$Parameter_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__GetPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

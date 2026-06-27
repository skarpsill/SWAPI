---
title: "Body::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetPropertyExtension.htm"
---

# Body::GetPropertyExtension

This property is obsolete and has been superseded
by[Body2::GetPropertyExtension](../Body2/Body2__GetPropertyExtension.htm).

Description

This method gets a float, string, or integer value from a body. The
VARIANT type returned is based on the how the data was placed on the body.
See Body::AddPropertyExtension for details.

Syntax (OLE Automation)

retval
= Body.GetPropertyExtension ( Id)

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT)
retval | Value
which was stored using Body::AddPropertyExtension |

Syntax (COM)

status
= Body->GetPropertyExtension ( Id, retval )

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT)
retval | Value
which was stored using Body::AddPropertyExtension |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter objects instead of this
method. They provide more flexibility.

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__GetPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

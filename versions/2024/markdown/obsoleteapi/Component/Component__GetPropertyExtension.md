---
title: "Component::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetPropertyExtension.htm"
---

# Component::GetPropertyExtension

This property is obsolete and has been superseded
by[Component2::GetPropertyExtension](sldworksAPI.chm::/Component2/Component2__GetPropertyExtension.htm).

Description

This method retrieves a float, string, or integer value from a component.

Syntax (OLE Automation)

retval
= Component.GetPropertyExtension ( Id)

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier of the property extension |
| --- | --- | --- |
| Return: | (VARIANT)
retval | Value
that was stored using Component::AddPropertyExtension |

Syntax (COM)

status
= Component->GetPropertyExtension ( Id, &retval )

(Table)=========================================================

| Input: | (long)
Id | Unique
identifier of the property extension |
| --- | --- | --- |
| Output: | (VARIANT)
retval | Value that was stored using Component::AddPropertyExtension |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The VARIANT type returned by this method is based on the how the data
was placed on the component. See Component::AddPropertyExtension.

Use Attribute, AttributeDef, and Parameter instead of this method. These
classes are newer and provide more flexibility.

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
<param name="Items" value="Component_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

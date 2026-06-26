---
title: "ModelDoc::AddLightSourceExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddLightSourceExtProperty.htm"
---

# ModelDoc::AddLightSourceExtProperty

This
method is obsolete and has been superseded by[ModelDoc2::AddLightSourceExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddLightSourceExtProperty.htm).

Description

This method stores a float, string, or integer value for light source.
This light source extension property is stored on the model document,
but is unique to the specified light source. To add the extension property,
you must first define the VARIANT type (float, string, or integer), give
your variable a value, and then call this method to place the value on
the light source for future reference.

Syntax (OLE Automation)

retval = ModelDoc.AddLightSourceExtProperty
( Id, PropertyExtension)

(Table)=========================================================

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (VARIANT) PropertyExtension | Value you wish to store for the light source |
| Return: | (long) retval | ID of the extension property |

Syntax (COM)

status = ModelDoc->AddLightSourceExtProperty
( Id, PropertyExtension, &retval )

(Table)=========================================================

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (VARIANT) PropertyExtension | Value you wish to store for the light source |
| Output: | (long) retval | ID of the extension property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ModelDoc_Object$$**$$ZLighting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__AddLightSourceExtProperty.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

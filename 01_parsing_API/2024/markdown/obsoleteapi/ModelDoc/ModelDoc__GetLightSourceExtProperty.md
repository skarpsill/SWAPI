---
title: "ModelDoc::GetLightSourceExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLightSourceExtProperty.htm"
---

# ModelDoc::GetLightSourceExtProperty

This
method is obsolete and has been superseded by[ModelDoc2::GetLightSourceExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLightSourceExtProperty.htm).

Description

This method retrieves a float, string, or integer value stored for the
light source. The VARIANT type returned is based on the how the data was
placed. See ModelDoc::AddLightSourceExtProperty for reference.

Syntax (OLE Automation)

retval = ModelDoc.GetLightSourceExtProperty
( Id, PropertyId)

(Table)=========================================================

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (long) PropertyId | ID of the property extension |
| Return: | (VARIANT) retval | Value stored for the light source |

Syntax (COM)

status = ModelDoc->GetLightSourceExtProperty
( Id, PropertyId, &retval )

(Table)=========================================================

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (long) PropertyId | ID of the property extension |
| Output: | (VARIANT) retval | Value stored for the light source |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID ranges from 0 ton,
wheren= (the total number of
light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZLighting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetLightSourceExtProperty.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

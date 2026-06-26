---
title: "ModelDoc::GetLightSourceIdFromName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLightSourceIdFromName.htm"
---

# ModelDoc::GetLightSourceIdFromName

This
method is obsolete and has been superseded by[ModelDoc2::GetLightSourceIdFromName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLightSourceIdFromName.htm).

Description

This method gets the ID of the name of the specified light source. The
name specified should be the internal light source name. This is the name
that is not visible to the user.

Syntax (OLE Automation)

retval = ModelDoc.GetLightSourceIdFromName
( lightName)

(Table)=========================================================

| Input: | (BSTR) lightName | Internal name of the desired light source |
| --- | --- | --- |
| Return: | (long) retval | Light source ID for the specified light source |

Syntax (COM)

status = ModelDoc->GetLightSourceIdFromName
( lightName, &retval )

(Table)=========================================================

| Input: | (BSTR) lightName | Internal name of the desired light source |
| --- | --- | --- |
| Output: | (long) retval | Light source ID for the specified light source |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetLightSourceIdFromName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

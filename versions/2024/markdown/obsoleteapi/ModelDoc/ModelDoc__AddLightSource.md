---
title: "ModelDoc::AddLightSource"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddLightSource.htm"
---

# ModelDoc::AddLightSource

This
method is obsolete and has been superseded by[ModelDoc2::AddLightSource](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddLightSource.htm).

Description

This method adds a specific light source type to a scene with the specified
names.

Syntax (OLE Automation)

retval = ModelDoc.AddLightSource (
idName, lTyp, userName)

(Table)=========================================================

| Input: | (BSTR) idName | New light source Id name |
| --- | --- | --- |
| Input: | (int) Type | New light source type |
| Input: | (BSTR) userName | New light source user name |
| Return: | (BOOL) retval | TRUE if the light source creation was successful, FALSE otherwise; creation
will fail, for example, if the light source idName is not unique within
this model |

Syntax (COM)

status = ModelDoc->AddLightSource
( idName, lTyp, userName, &retval )

(Table)=========================================================

| Input: | (BSTR) idName | New light source Id name |
| --- | --- | --- |
| Input: | (int) Type | New light source type |
| Input: | (BSTR) userName | New light source user name |
| Output: | (VARIANT_BOOL) retval | TRUE if the light source creation was successful, FALSE otherwise; creation
will fail, for example, if the light source idName is not unique within
this model |
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__AddLightSource.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

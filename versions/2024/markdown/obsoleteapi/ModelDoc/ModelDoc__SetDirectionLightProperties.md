---
title: "ModelDoc::SetDirectionLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetDirectionLightProperties.htm"
---

# ModelDoc::SetDirectionLightProperties

This
method is obsolete and has been superseded by[ModelDoc2::SetDirectionLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetDirectionLightProperties.htm).

Description

This method sets direction light properties.

Syntax (OLE Automation)

retval = ModelDoc.SetDirectionLightProperties ( name,
ambient, diffuse, specular, color, enabled, fixed, xDir, yDir, zDir )

(Table)=========================================================

| Input: | (BSTR)name | Light name to modify |
| --- | --- | --- |
| Input: | (double)ambient | Light source ambient value |
| Input: | (double)diffuse | Light source diffuse value |
| Input: | (double)specular | Light source specular value |
| Input: | (long)color | COLORREF color value |
| Input: | (BOOL)enabled | TRUE if the light should be enabled |
| Input: | (BOOL)fixed | TRUE if the light should be fixed |
| Input: | (double)xDir | x component of the light direction vector |
| Input: | (double)yDir | y component of the light direction vector |
| Input: | (double)zDir | z component of the light direction vector |
| Return: | (BOOL) retval | TRUE if light properties were changed successfully |

Syntax (COM)

status = ModelDoc->SetDirectionLightProperties
(name, ambient, diffuse, specular, color, enabled, fixed, xDir, yDir,
zDir, &retval )

(Table)=========================================================

| Input: | (BSTR)name | Light name to be modified |
| --- | --- | --- |
| Input: | (double)ambient | Light source ambient value |
| Input: | (double)diffuse | Light source diffuse value |
| Input: | (double)specular | Light source specular value |
| Input: | (long)color | COLORREF color value |
| Input: | (VARIANT_BOOL)enabled | TRUE if the light should be enabled |
| Input: | (VARIANT_BOOL)fixed | TRUE if the light should be fixed |
| Input: | (double)xDir | x component of the light direction vector |
| Input: | (double)yDir | y component of the light direction vector |
| Input: | (double)zDir | z component of the light direction vector |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties were changed successfully |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetDirectionLightProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

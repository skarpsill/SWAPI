---
title: "ModelDoc::SetSpotlightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSpotlightProperties.htm"
---

# ModelDoc::SetSpotlightProperties

This method is obsolete
and has been superseded by[ModelDoc2::SetSpotlightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSpotlightProperties.htm).

Description

This method sets the spotlight properties.

Syntax (OLE Automation)

retval = ModelDoc.SetSpotlightProperties ( name,
ambient, diffuse, specular, color, enabled, fixed, x, y, z, xTarget, yTarget,
zTarget )

(Table)=========================================================

| Input: | (BSTR) name | Light name to be modified |
| --- | --- | --- |
| Input: | (double) ambient | Light source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long) color | COLORREF color value |
| Input: | (BOOL) enabled | TRUE if a light is enabled |
| Input: | (BOOL) fixed | TRUE if a light is fixed |
| Input: | (double) x | x location of the spotlight |
| Input: | (double) y | y location of the spotlight |
| Input: | (double) z | z location of the spotlight |
| Input: | (double) xTarget | x location of the spotlight target |
| Input: | (double) yTarget | y location of the spotlight target |
| Input: | (double) zTarget | z location of the spotlight target |
| Input: | (double) coneAngle | Cone angle through which the beam spreads in
degrees |
| Return: | (BOOL) retval | TRUE if light properties were modified successfully |

Syntax (COM)

status = ModelDoc->SetSpotlightProperties ( name,
ambient, diffuse, specular, color, enabled, fixed, x, y, z, xTarget, yTarget,
zTarget, &retval )

(Table)=========================================================

| Input: | (BSTR) name | Light name to be modified |
| --- | --- | --- |
| Input: | (double) ambient | Light source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long) color | COLORREF color value |
| Input: | (VARIANT_BOOL) enabled | TRUE if the light should be enabled |
| Input: | (VARIANT_BOOL) fixed | TRUE if the light should be fixed |
| Input: | (double) x | x location of the spotlight |
| Input: | (double) y | y location of the spotlight |
| Input: | (double) z | z location of the spotlight |
| Input: | (double) xTarget | x location of the spotlight target |
| Input: | (double) yTarget | y location of the spotlight target |
| Input: | (double) zTarget | z location of the spotlight target |
| Input: | (double) coneAngle | Cone angle through which the beam spreads in
degrees |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties were modified successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZLighting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetSpotlightProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

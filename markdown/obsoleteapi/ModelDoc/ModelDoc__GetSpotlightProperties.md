---
title: "ModelDoc::GetSpotlightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSpotlightProperties.htm"
---

# ModelDoc::GetSpotlightProperties

This
method is obsolete and has been superseded by[ModelDoc2::GetSpotlightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSpotlightProperties.htm).

Description

This method gets the spotlight properties.

Syntax (OLE Automation)

retval = ModelDoc.GetSpotlightProperties ( name,
&ambient, &diffuse, &specular, &color, &enabled, &fixed,
&x, &y, &z, &xTarget, &yTarget, &zTarget, &coneAngle
)

(Table)=========================================================

| Input: | (BSTR) name | Light name used internally by SolidWorks (returned
by ModelDoc::GetLightSourceName) |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long) color | COLORREF color value |
| Output: | (BOOL) enabled | TRUE if a light is enabled, FALSE if not |
| Output: | (BOOL) fixed | TRUE if a light is fixed, FALSE if not |
| Output: | (double) x | x location of the spot light |
| Output: | (double) y | y location of the spot light |
| Output: | (double) z | z location of the spot light |
| Output: | (double) xTarget | x location of the spot light target |
| Output: | (double) yTarget | y location of the spot light target |
| Output: | (double) zTarget | z location of the spot light target |
| Output: | (double) coneAngle | Cone angle through which the beam spreads in
degrees |
| Return: | (BOOL) retval | TRUE if light properties determined without a
problem, FALSE if not |

Syntax (COM)

status = ModelDoc->GetSpotlightProperties ( name,
&ambient, &diffuse, &specular, &color, &enabled, &fixed,
&x, &y, &z, &xTarget, &yTarget, &zTarget, &coneAngle,
&retval )

(Table)=========================================================

| Input: | (BSTR) name | Light name used internally by SolidWorks (returned
by ModelDoc::GetLightSourceName) |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long) color | COLORREF color value |
| Output: | (VARIANT_BOOL) enabled | TRUE if a light is enabled, FALSE if not |
| Output: | (VARIANT_BOOL) fixed | TRUE if a light is fixed, FALSE if not |
| Output: | (double) x | x location of the spot light |
| Output: | (double) y | y location of the spot light |
| Output: | (double) z | z location of the spot light |
| Output: | (double) xTarget | x location of the spot light target |
| Output: | (double) yTarget | y location of the spot light target |
| Output: | (double) zTarget | z location of the spot light target |
| Output: | (double) coneAngle | Cone angle through which the beam spreads in
degrees |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties determined without a
problem, FALSE if not |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetSpotlightProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

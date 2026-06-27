---
title: "ModelDoc::SetLightSourcePropertyValuesVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetLightSourcePropertyValuesVB.htm"
---

# ModelDoc::SetLightSourcePropertyValuesVB

This
property is obsolete and has been superseded by[ModelDoc2::SetLightSourcePropertyValuesVB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetLightSourcePropertyValuesVB.htm).

Description

This method sets the light source property values. This method is similar
to the ModelDoc::LightSourcePropertyValues property, but this method allows
you to pass each argument individually.

Syntax (OLE Automation)

retval = ModelDoc.SetLightSourcePropertyValuesVB
( IdName, lType, diff, rgbColor, dist, dirX, dirY, dirZ, spotDirX, spotDirY,
spotDirZ, spotAngle, fallOff0, fallOff1, fallOff2, ambient, specular,
spotExponent, disable)

(Table)=========================================================

| Input: | (BSTR) IdName | Light source ID name |
| --- | --- | --- |
| Input: | (int) lType | Light source type where valid types are taken from openGL definitions
(LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT) |
| Input: | (double) diff | Light source diffuseness where values range from 0 to 1 |
| Input: | (long) rgbColor | Color value |
| Input: | (double) dist | Distance between the light source position and the vertex |
| Input: | (double) dirX | X unit vector value describing the lights position |
| Input: | (double) dirY | Y unit vector value describing the lights position |
| Input: | (double) dirZ | Z unit vector value describing the lights position |
| Input: | (double) spotDirX | Spot X direction |
| Input: | (double) spotDirY | Spot Y direction |
| Input: | (double) spotDirZ | Spot Z direction |
| Input: | (double) spotAngle | Spot angle |
| Input: | (double) fallOff0 | Light source falloff - constant attenuation |
| Input: | (double) fallOff1 | Light source falloff - linear attenuation |
| Input: | (double) fallOff2 | Light source falloff - quadratic attenuation |
| Input: | (double) ambient | Llight source ambient intensity |
| Input: | (double) specular | Light source specular intensity |
| Input: | (double) spotExponent | Spot exponent |
| Input: | (BOOL) disable | Light source disabled |
| Return: | (BOOL) retval | Return value is for the SetLightSourcePropertyValuesVB implementation
and will return TRUE if setting the light source properties was successful
and FALSE otherwise |

Syntax
(COM)

status = ModelDoc->SetLightSourcePropertyValuesVB
( IdName, lType, diff, rgbColor, dist, dirX, dirY, dirZ, spotDirX, spotDirY,
spotDirZ, spotAngle, fallOff0, fallOff1, fallOff2, ambient, specular,
spotExponent, disable, &retval )

(Table)=========================================================

| Input: | (BSTR) IdName | Lght source id name |
| --- | --- | --- |
| Input: | (int) lType | Light source type where valid types are taken from openGL definitions
(LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT) |
| Input: | (double) diff | Light Source diffuseness where values range from 0 to 1 |
| Input: | (long) rgbColor | Color value |
| Input: | (double) dist | Distance between the light source position and the vertex |
| Input: | (double) dirX | X unit vector value describing the lights position |
| Input: | (double) dirY | Y unit vector value describing the lights position |
| Input: | (double) dirZ | Z unit vector value describing the lights position |
| Input: | (double) spotDirX | Spot X direction |
| Input: | (double) spotDirY | Spot Y direction |
| Input: | (double) spotDirZ | Spot Z direction |
| Input: | (double) spotAngle | Spot angle |
| Input: | (double) fallOff0 | Light source falloff - constant attenuation |
| Input: | (double) fallOff1 | Light source falloff - linear attenuation |
| Input: | (double) fallOff2 | Light source falloff - quadratic attenuation |
| Input: | (double) ambient | Light source ambient intensity |
| Input: | (double) specular | Light source specular intensity |
| Input: | (double) spotExponent | Spot exponent |
| Input: | (VARIANT_BOOL) disable | Light source disabled |
| Output: | (VARIANT_BOOL) retval | Return value is for the SetLightSourcePropertyValuesVB implementation
and will return TRUE if setting the light source properties was successful
and FALSE otherwise |
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZLighting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetLightSourcePropertyValuesVB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

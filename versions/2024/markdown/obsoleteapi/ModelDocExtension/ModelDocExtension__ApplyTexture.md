---
title: "ModelDocExtension::ApplyTexture"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__ApplyTexture.htm"
---

# ModelDocExtension::ApplyTexture

This method is obsolete and has been superseded
by[ModelDocExtension::SetTexture](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__SetTexture.htm).

Description

This method applies texture
to all of the selected objects.

NOTE:You cannot apply textures to drawing components.

Syntax (OLE Automation)

status = ModelDocExtension.ApplyTexture (Scale, angle,
textureFilename, blendColor)

(Table)=========================================================

| Input: | (long) Scale | Scale factor (must be between
2 and 198) for texture |
| --- | --- | --- |
| Input: | (double) angle | Angle in degrees (must be between
0 ° and 360 ° ) at which to apply
the texture |
| Input: | (BSTR) textureFilename | Path and filename of the texture
to apply |
| Input: | (VARIANT_BOOL) blendColor | TRUE to blend the current face
color with the texture, FALSE to display the texture as is |
| Output: | (VARIANT_BOOL) status | TRUE if texture applied, FALSE
if not |

Syntax (COM)

status = ModelDocExtension->ApplyTexture ( Scale,
angle, textureFilename, blendColor, &status)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Scale | Scale factor for texture; 1.0
fits the texture to the model |
| --- | --- | --- |
| Input: | (double) angle | Angle in degrees
at which to apply the texture |
| Input: | (BSTR) textureFilename | Path and filename of the texture to apply |
| Input: | (VARIANT_BOOL) blendColor | TRUE to blend the current face
color with the texture, FALSE to display the texture as is |
| Output: | (VARIANT_BOOL) status | TRUE if texture applied, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDocExtension\ModelDocExtension__ApplyTexture.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="ModelDocExtension_Object$$**$$ModelDocExtensionTextures$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDocExtension\ModelDocExtension__ApplyTexture.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

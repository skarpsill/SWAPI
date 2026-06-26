---
title: "ModelDoc::FeatureCutThicken2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureCutThicken2.htm"
---

# ModelDoc::FeatureCutThicken2

This
method is obsolete and has been superseded by[ModelDoc2::FeatureCutThicken2](../ModelDoc2/ModelDoc2__FeatureCutThicken2.htm).

Description

This method thickens the selected
reference surface feature and then generates a cut.

Syntax (OLE Automation)

void ModelDoc.FeatureCutThicken2 (thickness, direction, faceIndex, fillVolume)

(Table)=========================================================

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0
Thicken side 1 1
Thicken side2 2
Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (BOOL) fillVolume | TRUE if you wish to make a solid from knitted
surface, FALSE if not |

Syntax (COM)

status = ModelDoc->FeatureCutThicken2 ( thickness,
direction, faceIndex, fillVolume )

(Table)=========================================================

| Input: | (double )thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0
Thicken side 1 1
Thicken side2 2
Thicken both sides |
| Input: | (long) faceIndex | Not used |
| Input: | (VARIANT_BOOL) fillVolume | TRUE if you wish to make a solid from knitted
surface, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If fillVolume is TRUE, the other arguments are
ignored. A closed surface is required when fillVolumeis TRUE.

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
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__FeatureCutThicken2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

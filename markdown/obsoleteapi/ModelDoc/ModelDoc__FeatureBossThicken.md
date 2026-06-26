---
title: "ModelDoc::FeatureBossThicken"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureBossThicken.htm"
---

# ModelDoc::FeatureBossThicken

This
method is obsolete and has been superseded by[ModelDoc::FeatureBossThicken2](ModelDoc__FeatureBossThicken2.htm).

Description

This method creates a thicken
feature and then a boss .

Syntax (OLE Automation)

void ModelDoc.FeatureBossThicken (
thickness, direction, faceIndex )

(Table)=========================================================

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0
– Thicken side 1 1
– Thicken side2 2
– Thicken both sides |
| Input: | (long) NotUsed | Not used |

Syntax (COM)

status = ModelDoc->FeatureBossThicken
( thickness, direction, faceIndex )

(Table)=========================================================

| Input: | (double) thickness | Wall thickness |
| --- | --- | --- |
| Input: | (long) direction | 0
– Thicken side 1 1
– Thicken side2 2
– Thicken both sides |
| Input: | (long) NotUsed | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a boss feature by thickening the selected reference
surface.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__FeatureBossThicken.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

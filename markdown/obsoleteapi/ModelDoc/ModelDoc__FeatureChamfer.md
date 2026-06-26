---
title: "ModelDoc::FeatureChamfer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureChamfer.htm"
---

# ModelDoc::FeatureChamfer

This
method is obsolete and has been superseded by[ModelDoc2::FeatureChamfer](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureChamfer.htm).

Description

This method creates a chamfer feature.

Syntax (OLE Automation)

void ModelDoc.FeatureChamfer ( width,
angle, flip)

(Table)=========================================================

| Input: | (double) width | Width of the chamfer in meters |
| --- | --- | --- |
| Input: | (double) angle | Angle of the chamfer |
| Input: | (BOOL) flip | 0
if angle is to be measured from the right face 1
if angle is to be measured from the left face |

Syntax (COM)

status = ModelDoc->FeatureChamfer
( width, angle, flip )

(Table)=========================================================

| Input: | (double) width | Width of the chamfer in meters |
| --- | --- | --- |
| Input: | (double) angle | Angle of the chamfer |
| Input: | (VARIANT_BOOL) flip | 0
if angle is to be measured from the right face 1
if angle is to be measured from the left face |
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FeatureChamfer.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

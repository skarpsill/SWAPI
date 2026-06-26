---
title: "ModelDoc::SketchPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchPoint.htm"
---

# ModelDoc::SketchPoint

This
method is obsolete and has been superseded by[ModelDoc::CreatePoint2](ModelDoc__CreatePoint2.htm).

Description

This method creates a point entity at point (x, y, z).

Syntax (OLE Automation)

void ModelDoc.SketchPoint ( x, y, z)

(Table)=========================================================

| Input: | (double) x | x value of point in meters |
| --- | --- | --- |
| Input: | (double) y | y value of point in meters |
| Input: | (double) z | Not used |

Syntax (COM)

status = ModelDoc->SketchPoint (
x, y, z )

(Table)=========================================================

| Input: | (double) x | x value of point in meters |
| --- | --- | --- |
| Input: | (double) y | y value of point in meters |
| Input: | (double) z | Not used |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The z value should be set to 0.0 as points created in a sketch must
be in the particular sketch plane.

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchPoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

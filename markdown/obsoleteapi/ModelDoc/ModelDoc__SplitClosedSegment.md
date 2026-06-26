---
title: "ModelDoc::SplitClosedSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SplitClosedSegment.htm"
---

# ModelDoc::SplitClosedSegment

This method is obsolete
and has been superseded by[ModelDoc2::SplitClosedSegment](../ModelDoc2/ModelDoc2__SplitClosedSegment.htm).

Description

This method splits the selected sketch segment
into two sketch segments.

Syntax (OLE Automation)

void ModelDoc.SplitClosedSegment ( x1, y1, z1, x2,
y2, z2 )

(Table)=========================================================

| Input: | (double) x1 | X value of first point |
| --- | --- | --- |
| Input: | (double) y1 | Y value of first point |
| Input: | (double) z1 | Z value of first point |
| Input: | (double) x2 | X value of second point |
| Input: | (double) y2 | Y value of second point |
| Input: | (double) z2 | Z value of second point |

Syntax (COM)

status = ModelDoc->SplitClosedSegment ( x1, y1,
z1, x2, y2, z2 )

(Table)=========================================================

| Input: | (double) x1 | X value of first point |
| --- | --- | --- |
| Input: | (double) y1 | Y value of first point |
| Input: | (double) z1 | Z value of first point |
| Input: | (double) x2 | X value of second point |
| Input: | (double) y2 | Y value of second point |
| Input: | (double) z2 | Z value of second point |
| Return: | (HRESULT )status | S_OK if successful |

Remarks

The selected sketch segment must be a closed entity;
for example, the start point and end point must be the same. To split
a closed sketch segment, for example a complete circle, into two pieces,
you must specify two points (x1, y1, z1) and (x2, y2, z2).

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifySketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SplitClosedSegment.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

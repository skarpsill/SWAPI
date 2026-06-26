---
title: "ModelDoc::SplitOpenSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SplitOpenSegment.htm"
---

# ModelDoc::SplitOpenSegment

This method is obsolete
and has been superseded by[ModelDoc2::SplitOpenSegment](../ModelDoc2/ModelDoc2__SplitOpenSegment.htm).

Description

This method splits the selected sketch segment
into two sketch segments.

Syntax (OLE Automation)

retval = ModelDoc.SplitOpenSegment ( x1, y1, z1 )

(Table)=========================================================

| Input: | (double) x | X value of the point, which splits the sketch
segment in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point, which splits the sketch
segment in two |
| Input: | (double) z | Y value of the point, which splits the sketch
segment in two |

Syntax (COM)

status = ModelDoc->SplitOpenSegment ( x1, y1,
z1 )

(Table)=========================================================

| Input: | (double) x | X value of the point, which will split the sketch
segment in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point, which will split the sketch
segment in two |
| Input: | (double) z | Y value of the point, which will split the sketch
segment in two |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected sketch segment must be an open
entity; for example, the start point and end point cannot be the same.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SplitOpenSegment.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

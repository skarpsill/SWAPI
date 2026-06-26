---
title: "ModelDoc::CreateArcVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateArcVB.htm"
---

# ModelDoc::CreateArcVB

This
method is obsolete and has been superseded by[ModelDoc::CreateArc2](ModelDoc__CreateArc2.htm).

Description

This method creates an arc from P1 as center, from P2 to P3, and may
be used in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc.CreateArcVB ( p1x, p1y,
p1z, p2x, p2y, p2z, p3x, p3y, p3z, dir)

(Table)=========================================================

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Start point x value in meters |
| Input: | (double) p2y | Start point y value in meters |
| Input: | (double) p2z | Start point z value in meters |
| Input: | (double) p3x | End point x value in meters |
| Input: | (double) p3y | End point y value in meters |
| Input: | (double) p3z | End point z value in meters |
| Input: | (short) dir | Direction of arc ( +1 or -1) |

Syntax (COM)

status = ModelDoc->CreateArcVB (
p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z, dir )

(Table)=========================================================

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) p2x | Start point x value in meters |
| Input: | (double) p2y | Start point y value in meters |
| Input: | (double) p2z | Start point z value in meters |
| Input: | (double) p3x | End point x value in meters |
| Input: | (double) p3y | End point y value in meters |
| Input: | (double) p3z | Eend point z value in meters |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The ModelDoc::SetAddToDB method increases performance during entity
creation by adding entities directly to the SolidWorks database, and it
also avoids inferencing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__CreateArcVB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

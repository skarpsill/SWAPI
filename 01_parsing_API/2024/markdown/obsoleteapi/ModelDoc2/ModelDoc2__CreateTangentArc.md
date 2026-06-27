---
title: "ModelDoc2::CreateTangentArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateTangentArc.htm"
---

# ModelDoc2::CreateTangentArc

This method is obsolete and has been superseded
by[ModelDoc2::CreateTangentArc2](ModelDoc2__CreateTangentArc2.htm).

Description

This method creates an arc that is tangent to the entity which shares
its start point. The input start point must be an existing point in the
sketch and an endpoint of some other sketch entity.

Syntax (OLE Automation)

retval = ModelDoc2.CreateTangentArc
( p1x, p1y, p1z, p2x, p2y, p2z)

(Table)=========================================================

| Input: | (double) p1x | Start point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Start point y value in meters |
| Input: | (double) p1z | Start point z value in meters |
| Input: | (double) p2x | End point x value in meters |
| Input: | (double) p2y | End point y value in meters |
| Input: | (double) p2z | End point z value in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreateTangentArc
( p1x, p1y, p1z, p2x, p2y, p2z, &retval )

(Table)=========================================================

| Input: | (double) p1x | Start point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Start point y value in meters |
| Input: | (double) p1z | Start point z value in meters |
| Input: | (double) p2x | End point x value in meters |
| Input: | (double) p2y | End point y value in meters |
| Input: | (double) p2z | End point z value in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateTangentArc.htm" >
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
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateTangentArc.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

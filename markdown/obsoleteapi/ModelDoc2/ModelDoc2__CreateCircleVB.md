---
title: "ModelDoc2::CreateCircleVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCircleVB.htm"
---

# ModelDoc2::CreateCircleVB

This
method is obsolete and has been superseded by[ModelDoc2::CreateCircle2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCircle2.htm).

Description

This method creates a circle using a center point and another point
on the circle that helps determine the radius. This point also enables
any automatic relations, snapping to grid, and so on., which may be applicable
depending on its location. This method is for use in Visual Basic and
other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc2.CreateCircleVB ( p1x,
p1y, p1z, radius)

(Table)=========================================================

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |

Syntax (COM)

status = ModelDoc2->CreateCircleVB
( p1x, p1y, p1z, radius )

(Table)=========================================================

| Input: | (double) p1x | Center point x value in meters |
| --- | --- | --- |
| Input: | (double) p1y | Center point y value in meters |
| Input: | (double) p1z | Center point z value in meters |
| Input: | (double) radius | Radius of circle in meters |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__CreateCircleVB.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__CreateCircleVB.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

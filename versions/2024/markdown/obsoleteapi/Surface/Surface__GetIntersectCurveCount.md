---
title: "Surface::GetIntersectCurveCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__GetIntersectCurveCount.htm"
---

# Surface::GetIntersectCurveCount

This method is obsolete and has been superseded
by[Surface::GetIntersectCurveCount2](sldworksAPI.chm::/Surface/Surface__GetIntersectCurveCount2.htm).

Description

This method gets a point count for a surface-curve
intersection.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Surface->GetIntersectCurveCount ( otherCurve,
curveBound, &count )

Parameters Table Start

(Table)=========================================================

| Input: | (LPCURVE) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (double*) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Output: | (long) count | Number of points |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Visual Basic and C++ Dispatch applications should
use Surface::IntersectCurve instead of this method.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Surface\Surface__GetIntersectCurveCount.htm" >
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
<param name="Items" value="Surface_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Surface\Surface__GetIntersectCurveCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

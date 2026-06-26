---
title: "Surface::IntersectCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__IntersectCurve.htm"
---

# Surface::IntersectCurve

This method is obsolete and has been superseded
by[Surface::IntersectCurve2](sldworksAPI.chm::/Surface/Surface__IntersectCurve2.htm).

Description

This method gets a surface-curve intersection.
The curves must be bounded.

Syntax (OLE Automation)

retval = Surface.IntersectCurve ( otherCurve, curveBound,
pointArray, tArray, uvArray, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (LPDISPATCH) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (VARIANT) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Output: | (VARIANT*) pointArray | Array of points |
| Output: | (VARIANT*) tArray | VARIANT of type SafeArray of parameters on
curve |
| Output: | (VARIANT*) uvArray | VARIANT of type SafeArray of parameters on
surface |
| Output: | (VARIANT_BOOL) retval | TRUE if intersection succeeded, FALSE if not |

Syntax (COM)

status = Surface->IIntersectCurve ( otherCurve,
curveBound, pointArray, tArray, uvArray, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (LPCURVE) otherCurve | Pointer to curve |
| --- | --- | --- |
| Input: | (double*) curveBound | Array of 6 doubles representing the start and end points of the curve |
| Input: | (long) pointCount | Number of points |
| Output: | (VARIANT*) pointArray | Array of points of size pointCount*3 |
| Output: | (VARIANT*) tArray | Array of parameters on curve of size pointCount |
| Output: | (VARIANT*) uvArray | Array of size pointCount*2 |
| Output: | (VARIANT_BOOL) retval | TRUE if intersection succeeded, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Visual Basic applications should use this method
instead of using Surface::GetIntersectCurveCount.

Users of the COM version of this method should
first call Surface::GetIntersectCurveCount to get the number of points
for this surface-curve intersection.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Surface\Surface__IntersectCurve.htm" >
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
<param name="Items" value="Surface_Object$$**$$Curve_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Surface\Surface__IntersectCurve.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXIntersectFaces$$**$$EXIntersectFaceEdge$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Surface\Surface__IntersectCurve.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

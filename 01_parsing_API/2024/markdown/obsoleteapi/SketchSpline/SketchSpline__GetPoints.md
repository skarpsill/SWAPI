---
title: "SketchSpline::GetPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchSpline/SketchSpline__GetPoints.htm"
---

# SketchSpline::GetPoints

T his
method is obsolete and has been superseded by[SketchSpline::GetPoints2](sldworksAPI.chm::/SketchSpline/SketchSpline__GetPoints2.htm).

Description

This method gets the points used when creating
this sketch spline. The points returned are by interpolation instead of
by tessellation as is done by Sketch::GetSplines.

Syntax (OLE Automation)

retval = SketchSpline.GetPoints ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of doubles; these are
the x,y,z points used to create the spline |
| --- | --- | --- |

Syntax (COM)

status = SketchSpline->IGetPoints ( retval )

(Table)=========================================================

| Output: | (double*) retval | Array of doubles of size (SketchSpline::GetPointCount
* 3); these are the x,y,z points used to create the spline |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The[x,y,z]points returned for this
spline are the same points used to generate the spline. If you want a
tessellated representation of the spline, see Sketch::GetSplines.

For COM implementations, you can determine the
size of the array by multiplying the SketchSpline::GetPointCount return
value by 3.

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
<param name="Items" value="SketchSpline_Object$$**$$ZGetInfoSketchSpline$$**$$ZGetSketchSpline$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SketchSpline\SketchSpline__GetPoints.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

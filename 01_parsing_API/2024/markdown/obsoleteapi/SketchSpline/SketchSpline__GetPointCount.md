---
title: "SketchSpline::GetPointCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchSpline/SketchSpline__GetPointCount.htm"
---

# SketchSpline::GetPointCount

T his
method is obsolete and superseded by[SketchSpline::IEnumPoints](sldworksAPI.chm::/SketchSpline/SketchSpline__IEnumPoints.htm).

Description

This method determines the number of points
used when creating this sketch spline.

Syntax (OLE Automation)

retval = SketchSpline.GetPointCount ( )

(Table)=========================================================

| Return: | (long) retval | Nnumber of points used in creating this spline |
| --- | --- | --- |

Syntax (COM)

status = SketchSpline->GetPointCount ( &retval
)

(Table)=========================================================

| Output: | (long) retval | Number of points used in creating this spline |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this value to allocate your memory for a call
to the COM version ofkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSpline::GetPoints.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SketchSpline\SketchSpline__GetPointCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

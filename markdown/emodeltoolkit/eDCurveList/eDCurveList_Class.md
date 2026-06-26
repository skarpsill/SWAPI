---
title: "eDCurveList Class"
project: ""
interface: "eDCurveList"
member: ""
kind: "class"
source: "emodeltoolkit/eDCurveList/eDCurveList_Class.htm"
---

# eDCurveList Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more circles, arcs, ellipses, elliptical arcs, lines,
polylines, individual polygons, and splines.

#### Header file code

class eDCurveList : public[eDObject](../eDObject/eDObject_Class.htm)

{

public:

eDOutcomebegin!kadov{{}}end!kadovInsertLine( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&from,
const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&to, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts a line

eDOutcomebegin!kadov{{}}end!kadovInsertPolyline( int npoints,[eDPt3d](../eDPt3d/eDPt3d_Class.htm)*pointdata, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style
=[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts a polyline

eDOutcomebegin!kadov{{}}end!kadovInsertPolygon( int npoints,[eDPt3d](../eDPt3d/eDPt3d_Class.htm)*pointdata, bool fill, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts
a polygon

eDOutcomebegin!kadov{{}}end!kadovInsertCircle( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&start,
const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&mid, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&end, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts a circle

eDOutcomebegin!kadov{{}}end!kadovInsertCircularArc( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&start,
const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&mid, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&end, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts a circular
arc

eDOutcomebegin!kadov{{}}end!kadovInsertEllipse( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)¢er,
const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&major, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&minor, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts an ellipse

eDOutcomebegin!kadov{{}}end!kadovInsertEllipticalArc( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)¢er, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&major,
const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&minor, double
start, double end,const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts
an elliptical arc

eDOutcomebegin!kadov{{}}end!kadovInsertSpline( int degree, int npoints,[eDPt3d](../eDPt3d/eDPt3d_Class.htm)*pointdata, float *weights, float *knots, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts
a spline

eDOutcomebegin!kadov{{}}end!kadovInsertText( constECHARbegin!kadov{{}}end!kadov*text, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&insertpt,
const[eDFont](../eDFont/eDFont_Class.htm)&font, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)*endpt = NULL, const[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)&style =[eDLineStyle](../eDLineStyle/eDLineStyle_Structure.htm)() ); //Inserts text

};

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
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
<param name="Items" value="DocumentGeometryClasses$$**$$eDCurveList$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDCurveList\eDCurveList_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

begin!kadov{{

}}end!kadov

kadov_tag{{<implicit_p>}}

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
<param name="Items" value="ZGeteDCurveList$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDCurveList\eDCurveList_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

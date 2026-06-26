---
title: "Sketch::GetSplineParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetSplineParams.htm"
---

# Sketch::GetSplineParams

This method is obsolete
and is superseded by[Sketch::GetSplineParams2](sldworksAPI.chm::/Sketch/Sketch__GetSplineParams2.htm).

Description

This method returns the parameters of the spline.

Syntax (OLE Automation)

params = Sketch.GetSplineParams
( )

(Table)=========================================================

| Return: | (VARIANT) params | VARIANT of type SafeArray containing an array of doubles |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetSplineParams
( params )

(Table)=========================================================

| Output: | (double*) params | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments
for access to individual SketchSegment and SketchSpline objects.

For COM implementations, call Sketch::GetSplineParamsCount
to determine the size of the array required to hold the data.

The return value is an array of doubles containing
data for all the splines in the sketch.

The first two array elements for each spline contain
4 integer values holding information that describes the rest of the data
in that splines parameters:

(Table)=========================================================

| Spline
Element | Packed Data |  |
| --- | --- | --- |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dimis the number of dimensions the spline is defined in
- Order is the order
  of the spline
- nCtrlPointsis the number of control points
- Periodicis 1 for a closed spline or 0 for an open spline

The number of knots depends on whether the spline
is periodic or not:

(Table)=========================================================

| Periodic: | numKnots = nCtrlPoints + 1 |
| --- | --- |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

Therefore, the size of the data for each spline is
given by:

2 + numKnots + numControlPointDoubles
* Dim

The ControlPoint data (in the sketch coordinate system)
follows the 2 packed data elements, and then the Knot points. Subsequent
Splines follow one another in the array.

[packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension
elements],... knot1, knot2,...,]

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
<param name="Items" value="Sketch_Object$$**$$ZGetInfoSketch$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Sketch\Sketch__GetSplineParams.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Sketch_GetSplineParameters_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Sketch\Sketch__GetSplineParams.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZPacked_Integers$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Sketch\Sketch__GetSplineParams.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

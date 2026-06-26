---
title: "Body::AddProfileBspline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddProfileBspline.htm"
---

# Body::AddProfileBspline

This method is obsolete and has been superseded by[Body2::AddProfileBspline](sldworksAPI.chm::/Body2/Body2__AddProfileBspline.htm).

Description

This method creates an B-spline profile curve and returns a pointer
to that curve.

Syntax (OLE Automation)

retval = Body.AddProfileBspline ( props,
knots, ctrlPtCoords )

(Table)=========================================================

| Input: | (VARIANT) props | Contains 4 integers
packed into 2 double elements (see below) |
| --- | --- | --- |
| Input: | (VARIANT) knots | VARIANT of type SafeArray
of numKnots doubles (see below) |
| Input: | (VARIANT) ctrlPtCoords | VARIANT of type SafeArray
of numCtrlPtCoord doubles (see below) |
| Return: | (LPDISPATCH) retval | Pointer to dispatch
object, the B-spline profile curve |

Syntax (COM)

status = Body->IAddProfileBsplineDLL
( props, knots, ctrlPtCoords, &retval )

(Table)=========================================================

| Input: | (long*) props | Contains 4 longs (see
below) |
| --- | --- | --- |
| Input: | (double*) knots | Pointer to an array
of numKnots doubles (see below) |
| Input: | (double*) ctrlPtCoords | Pointer to an array
of numCtrlPtCoord doubles (see below) |
| Output: | (LPCURVE) retval | Pointer to the B-spline
profile curve |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method in conjunction with Body::CreateRevolutionSurface
to generate any surface of revolution, or with Body::CreateExtrusionSurface
to generate a tabulated cylinder.

The props argument contains the following values:

- DimensionControlPoints
- Order
- NumCtrlPoints
- Periodicity

The length of the knots array is given by:

numKnots = NumCtrlPoints + Order

The length of the CtrlPtCoords is given by:

numCtrlPtCoord = NumCtrlPoints * DimensionControlPoints

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__AddProfileBspline.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

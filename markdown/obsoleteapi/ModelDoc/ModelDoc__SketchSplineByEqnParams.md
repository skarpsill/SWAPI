---
title: "ModelDoc::SketchSplineByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchSplineByEqnParams.htm"
---

# ModelDoc::SketchSplineByEqnParams

This method is obsolete
and has been superseded by[ModelDoc2::SketchSplineByEqnParams](../ModelDoc2/ModelDoc2__SketchSplineByEqnParams.htm).

Description

This method creates a spline on the active 2D sketch using the Bcurve
parameters provided. For use with Visual Basic, see ModelDoc::SketchSplineByEqnParams2.

Syntax (OLE Automation)

retval = ModelDoc.SketchSplineByEqnParams
( paramsIn )

(Table)=========================================================

| Input: | (VARIANT) paramsIn | VARIANT of type SafeArray containing an array of doubles |
| --- | --- | --- |
| Return: | (BOOLEAN) retval | TRUE if created successfully |

Syntax (COM)

status = ModelDoc->ISketchSplineByEqnParams
( propArray, knotsArray, cntrlPntCoordArray, &retval )

(Table)=========================================================

| Input: | (int*) propArray | Includes dimension, order, number of control points, periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (VARIANT_BOOL) retval | TRUE if created successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray argument contains 4 integers (packed into the first two
doubles in the SafeArray):

- Dimension
- Order
- Number of control points
- Periodicity ( TRUE or FALSE )

The knotsArray argument is an array of doubles with (Number of Control
Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension.

- Dimension
  = 2 then each control point is an array of 2 doubles ( x, y )
- Dimension
  = 3 then each control point is an array of 3 doubles ( x, y, z)
- Dimension
  = 4 then each control point is an array of 4 doubles ( x, y, z, w ) where
  w = weight

The parameters are provided as 3 arrays, which for COM applications
are passed separately and for OLE automation are packed into a single
SafeArray, which is packed as follows:

[packedDouble1,
packedDouble2, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],...]

Control point coordinates should be passed to this routine in sketch
space. The Z value is interpreted as 0. In certain situations, you must
transform your Bcurve parameters to sketch space with the help of Sketch::ModelToSketchXform.

Note:If the spline being generated
is a closed spline, then it must be flagged as periodic. In addition,
splines generated in sketches must be G1 continuous. If the data passed
to this method does not generate a G1 continuous spline, then it is rejected
and no spline is created.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreate3DCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SketchSplineByEqnParams.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

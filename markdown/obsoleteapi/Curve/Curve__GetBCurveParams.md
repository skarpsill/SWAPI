---
title: "Curve::GetBCurveParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__GetBCurveParams.htm"
---

# Curve::GetBCurveParams

This method is obsolete and has been superseded
by[Curve::GetBCurveParams3](sldworksAPI.chm::/Curve/Curve__GetBCurveParams3.htm).

Description

This
method gets the parameters of the curve.

Syntax (OLE Automation)

retval
= Curve.GetBCurveParams ( wantCubicIn)

(Table)=========================================================

| Input: | (BOOL)
wantCubicIn | TRUE
returns cubic rational parameters, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray describing the parameters of the curve |

Syntax (COM)

status
= Curve->IGetBCurveParams ( retval )

(Table)=========================================================

| Output: | (double*)
retval | Pointer
to an array of doubles describing the parameters of the curve |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

For COM implementations, see Curve::IGetBCurveParamsSize2 to determine
the size of the array returned and whether the curve data returned by
Cure::IGetBCurveParams is cubic rational or not.

To control the accuracy of the curve data, see Modeler::SetToleranceValue.

The return value retval is an array of doubles. The array size is (
2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints
+ order). The array is as follows:

[packedDouble1,packedDouble2,knot1,knot2,...,ControlPoint1[Dimension],ControlPoint2[Dimension],...]

where:

- packedDouble1isan integer pair containing theDimensionandOrder
- packedDouble2isan integer pair containing theNumControlPointsandPeriodicity
- knot1
- knot2

...

- ControlPoint1[dimension]
- ControlPoint2[dimension]

...

The size of the control
point array is based on the curve dimension:

- IfDimension= 3, thenControlPointis an
  array of 3 doubles ( x, y, z )
- IfDimension= 4, thenControlPointis an
  array of 4 doubles ( x, y, z, w ) where w = weight

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Curve_Object$$**$$ZGetInfoCurve$$**$$ZCurveMakeBsplineCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Curve\Curve__GetBCurveParams.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZExample_Get__Curve_Spline_Points_Example_VB$$**$$ZExample_Get_Curve_Spline_Points$$**$$EXSelectEdgeHoleFace$$**$$EXGetSplineEllipticalEdge$**$$EXGetParamsSplinePtsCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Curve\Curve__GetBCurveParams.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

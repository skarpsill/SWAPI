---
title: "Curve::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__Evaluate.htm"
---

# Curve::Evaluate

This method is obsolete and has been superseded
by[Curve::Evaluate2](sldworksAPI.chm::/Curve/Curve__Evaluate2.htm).

Description

This method evaluates the curve at the specified
parameter of the curve.

Syntax (OLE Automation)

retval = Curve.Evaluate ( Parameter )

(Table)=========================================================

| Input: | (double) Parameter | Curve parameter |
| --- | --- | --- |
| Return: | (VARIANT) retval | SafeArray containing an array of doubles |

Syntax (COM)

status = Curve->IEvaluate ( Parameter, &retval
)

(Table)=========================================================

| Input: | (double) Parameter | Curve parameter |
| --- | --- | --- |
| Output: | (double) retval | Pointer to an array of doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To determine a valid parameter range, use Curve::GetEndParams
or Edge::GetCurveParams2.

The OLE Automation retval is an array of doubles
with the following format:

[PointX, PointY, PointZ, TangentX, TangentY,
TangentZ, Success]

where:

- PointX,PointY,andPointZrepresent the 3D point in space for the given parameter
- TangentX,TangentY,andTangentZrepresent the tangent vector at the point
- TRUE if the
  operation is successful

The COM return value is an array of 6 doubles representing
the point and tangent. The success value is determined from the HRESULT
return.

This method returns values in meters.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__Evaluate.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Curve_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__Evaluate.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXIntersectFaces$$**$$EXOutsideEdgesFace$$**$$EXReturnUntrimmedCurve$$**$$EXCreatePCurve$$**$$EXSketchSegmentCurve$$**$$EXEvaluateCurvesDefinedSketchSpace$$**$$EXGetStartEndPointsSpline$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__Evaluate.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

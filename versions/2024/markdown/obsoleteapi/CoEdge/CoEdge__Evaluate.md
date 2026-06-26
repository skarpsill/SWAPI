---
title: "CoEdge::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CoEdge/CoEdge__Evaluate.htm"
---

# CoEdge::Evaluate

This method is obsolete and has been superseded
by[CoEdge::Evaluate2](sldworksAPI.chm::/CoEdge/CoEdge__Evaluate2.htm).

Description

This method gets the (X,Y,Z) location and the tangency vector on the
coedge at the specified position.

Syntax (OLE Automation)

retval = CoEdge.Evaluate ( param)

(Table)=========================================================

| Input: | (double) param | Curve parameter desired (U value desired for evaluation) |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = CoEdge.IEvaluate ( param,
retval )

(Table)=========================================================

| Input: | (double) param | Curve parameter desired (U value desired for evaluation) |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| Return: | ( HRESULT ) status | S_OK if successful |

Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of 6 doubles:

- retval[0] x location
  on the curve
- retval[1] y location
  on the curve
- retval[2] z location
  on the curve
- retval[3] x vector
  describing the tangency at the parameter location on the coedge
- retval[4] y vector
  describing the tangency at the parameter location on the coedge
- retval[5] z vector
  describing the tangency at the parameter location on the coedge
- retval[6] TRUE for
  successful completion, otherwise FALSE

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
<param name="Items" value="CoEdge_Object$$**$$Coedge::GetCurveParams$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\CoEdge\CoEdge__Evaluate.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXSelectTangentFaces$$**$$EXSelectEdgeHoleFace$$**$$EXFaceType$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\CoEdge\CoEdge__Evaluate.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "Edge::Evaluate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__Evaluate.htm"
---

# Edge::Evaluate

This method is obsolete and has been superseded
by[Edge::Evaluate2](sldworksAPI.chm::/Edge/Edge__Evaluate2.htm).

Description

This method evaluates the edge at the specified parameter.

Syntax (OLE Automation)

retval
= Edge.Evaluate ( Parameter)

(Table)=========================================================

| Input: | (double)
Parameter | Value
of the edge parameter |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray values containing the x,y,z value and derivative of
the edge (see Remarks ) |

Syntax (COM)

status
= Edge->IEvaluate ( Parameter, retval )

(Table)=========================================================

| Input: | (double)
Parameter | Value
of the edge parameter |
| --- | --- | --- |
| Output: | (double*)
retval | Pointer
to an array of doubles (see Remarks ) |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Use Edge::GetCurveParams2 to determine the valid
parameter range for this method.

This OLE implementation of this method returns
an array of doubles as follows:

[PointX, PointY, PointZ, TangentX, TangentY,
TangentZ, Success]

where the point values are in meters andSuccessis TRUE if successful and FALSE
if not.

The return value for the COM implementation is
different. To determine success, check the HRESULT return value. The array
is as follows:

[PointX, PointY, PointZ, TangentX, TangentY,
TangentZ]

where the point values are specified in meters.

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
<param name="Items" value="Edge_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Edge\Edge__Evaluate.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="Items" value="EXSelectTangentItem$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Edge\Edge__Evaluate.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

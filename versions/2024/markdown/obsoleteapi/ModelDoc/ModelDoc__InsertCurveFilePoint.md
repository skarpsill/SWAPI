---
title: "ModelDoc::InsertCurveFilePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFilePoint.htm"
---

# ModelDoc::InsertCurveFilePoint

This
method is obsolete and has been superseded by[ModelDoc2::InsertCurveFilePoint](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFilePoint.htm).

Description

This method is one of the methods called in a set of methods that can
create a 3D-reference curve. This method can set the curve points for
the 3D-reference curve.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFilePoint
( x, y, z)

(Table)=========================================================

| Input: | (double) x | X value for the point |
| --- | --- | --- |
| Input: | (double) y | Y value for the point |
| Input: | (double) z | Z value for the point |
| Return: | (BOOL) retval | TRUE if this call is successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertCurveFilePoint
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | X value for the point |
| --- | --- | --- |
| Input: | (double) y | Y value for the point |
| Input: | (double) z | Z value for the point |
| Output: | (VARIANT_BOOL) retval | TRUE if this call is successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ModelDoc::InsertCurveFileBegin and ModelDoc::InsertCurveFileEnd
should enclose all of your calls to this method. For example:

Part.InsertCurveFileBegin

Part.InsertCurveFilePoint 0.3048, 0.6096,
0.9144

Part.InsertCurveFilePoint 0.6096, 0.9144,
1.2192

Part.InsertCurveFilePoint 0.9144, 1.2192,
1.524

Part.InsertCurveFilePoint 1.2192, 1.524,
1.8288

Part.InsertCurveFileEnd

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateCurve$$**$$ZCreate3DCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertCurveFilePoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

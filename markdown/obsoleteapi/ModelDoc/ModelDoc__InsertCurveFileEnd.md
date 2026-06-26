---
title: "ModelDoc::InsertCurveFileEnd"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFileEnd.htm"
---

# ModelDoc::InsertCurveFileEnd

This
method is obsolete and has been superseded by[ModelDoc2::InsertCurveFileEnd](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFileEnd.htm).

Description

This method is the last method called in a set of related methods that
can create a 3D-reference curve. This method also ends the 3D-curve creation.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFileEnd
()

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if curve is created successfully, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertCurveFileEnd
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if curve is created successfully, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ModelDoc::InsertCurveFileBegin and this
method should enclose all of your calls to ModelDoc::InsertCurveFilePoint.
For example:

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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateCurve$$**$$ZCreate3DCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCurveFileEnd.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "ModelDoc::Sketch3DIntersections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Sketch3DIntersections.htm"
---

# ModelDoc::Sketch3DIntersections

This method is obsolete
and has been superseded by[ModelDoc2::Sketch3DIntersections](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Sketch3DIntersections.htm).

Description

This methods creates new sketch segments based
on the selected surfaces. The new sketch segments arekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}added
either to the active sketch or to an appropriate new sketch.

Syntax (OLE Automation)

void ModelDoc.Sketch3DIntersections ( )

Syntax (COM)

status = ModelDoc->Sketch3DIntersections ( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successfu |
| --- | --- | --- |

Remarks

If the active sketch is a 2D sketch and the intersection
curves are not in that plane, then the resulting sketch segments is projected
onto the plane of the sketch.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__Sketch3DIntersections.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "ModelDoc::Insert3DSplineCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Insert3DSplineCurve.htm"
---

# ModelDoc::Insert3DSplineCurve

This
method is obsolete and has been superseded by[ModelDoc2::Insert3DSplineCurve](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Insert3DSplineCurve.htm).

Description

This method inserts a 3D-spline curve through the selected reference
points.

Syntax (OLE Automation)

void ModelDoc.Insert3DSplineCurve (
curveClosed)

(Table)=========================================================

| Input: | (BOOL) curveClosed | TRUE if you want the curve to be closed, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->Insert3DSplineCurve
( curveClosed )

(Table)=========================================================

| Input: | (VARIANT_BOOL) curveClosed | TRUE if you want the curve to be closed, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To create 2D splines on a sketch, use ModelDoc::SketchSpline or ModelDoc::CreateSpline.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__Insert3DSplineCurve.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

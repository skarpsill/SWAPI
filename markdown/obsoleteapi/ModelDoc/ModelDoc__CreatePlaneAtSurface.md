---
title: "ModelDoc::CreatePlaneAtSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtSurface.htm"
---

# ModelDoc::CreatePlaneAtSurface

This method is obsolete
and has been superseded by[ModelDoc::CreatePlaneAtSurface2](ModelDoc__CreatePlaneAtSurface2.htm).

Description

This method creates a reference plane tangent
(or normal) to a surface.

Syntax (OLE Automation)

void ModelDoc.CreatePlaneAtSurface ( interIndex,
projOpt, reverseDir, normalPlane, angle )

(Table)=========================================================

| Input: | (int) interIndex | When there are multiple intersections, other
solutions may exist; for a surface, plane, and edge, the intersection
index is the intersection point to use when there are multiple intersections;
when the intersection index input is more than the number of intersection
points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (BOOL) projOpt | For a sketch point and a surface, TRUE to project
the sketch plane point along the sketch plane normal, FALSE to project
the sketch plane point normal to the surface |
| Input: | (BOOL) normalPlane | For a conical surface, TRUE to find the plane
normal to the surface, FALSE to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane,
relative to a chosen reference plane |

Syntax (COM)

status = ModelDoc->CreatePlaneAtSurface ( interIndex,
projOpt, reverseDir, normalPlane, angle )

(Table)=========================================================

| Input: | (int) interIndex | When there are multiple intersections, other
solutions may exist; for a surface, plane, and edge, the intersection
index is the intersection point to use when there are multiple intersections;
when the intersection index input is more than the number of intersection
points, the index of the last intersection point found will be used |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) projOpt | For a sketch point and a surface, TRUE to project
the sketch plane point along the sketch plane normal, FALSE to project
the sketch plane point normal to the surface |
| Input: | (VARIANT_BOOL)
normalPlane | For a conical surface, TRUE to find the plane
normal to the surface, FALSE
to find the plane tangent to the surface |
| Input: | (double) angle | Value of the angular offset of the normal plane,
relative to a chosen reference plane |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefPlane$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePlaneAtSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

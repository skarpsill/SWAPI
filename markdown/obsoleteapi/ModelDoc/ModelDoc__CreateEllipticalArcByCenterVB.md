---
title: "ModelDoc::CreateEllipticalArcByCenterVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipticalArcByCenterVB.htm"
---

# ModelDoc::CreateEllipticalArcByCenterVB

This
method is obsolete and has been superseded by[ModelDoc::CreateEllipticalArc2](ModelDoc__CreateEllipticalArc2.htm).

Description

This methodcreates
an elliptical arc trimmed between two points.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipticalArcByCenterVB
( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ,
startX, startY, startZ, endX, endY, endZ)

(Table)=========================================================

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center point |
| Input: | (double) centerZ | Z value for the ellipse center point |
| Input: | (double) majorX | X value for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y value for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y value for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the ellipse and on the minor axis |
| Input: | (double) startX | X value for CCW elliptical arc start point |
| Input: | (double) startY | Y value for CCW elliptical arc start point |
| Input: | (double) startZ | Z value for CCW elliptical arc start point |
| Input: | (double) endX | X value for CCW elliptical arc end point |
| Input: | (double) endY | Y value for CCW elliptical arc end point |
| Input: | (double) endZ | Z value for CCW elliptical arc end point |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->CreateEllipticalArcByCenterVB
( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ,
startX, startY, startZ, endX, endY, endZ, &retval )

(Table)=========================================================

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center
point |
| Input: | (double) centerZ | Z value for the ellipse center
point |
| Input: | (double) majorX | X value for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y value for a point on the
ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the
ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y value for a point on the
ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the
ellipse and on the minor axis |
| Input: | (double) startX | X value for CCW elliptical arc start point |
| Input: | (double) startY | Y value for CCW elliptical
arc start point |
| Input: | (double) startZ | Z value for CCW elliptical
arc start point |
| Input: | (double) endX | X value for CCW elliptical arc end point |
| Input: | (double) endY | Y value for CCW elliptical
arc end point |
| Input: | (double) endZ | Z value for CCW elliptical
arc end point |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specify the start* and end*arguments
in a counter-clockwise manner.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateEllipticalArcByCenterVB.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan

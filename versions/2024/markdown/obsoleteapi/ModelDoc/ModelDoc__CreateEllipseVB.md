---
title: "ModelDoc::CreateEllipseVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipseVB.htm"
---

# ModelDoc::CreateEllipseVB

This
method is obsolete and has been superseded by[ModelDoc::CreateEllipse2](../ModelDoc2/ModelDoc2__CreateEllipse2.htm).

Description

This methodcreates
an ellipse.

Syntax
(OLE Automation)

retval = ModelDoc.CreateEllipseVB (
centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ)

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
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise. |

Syntax (COM)

status = ModelDoc->CreateEllipseVB
( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ,
&retval )

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
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateEllipseVB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

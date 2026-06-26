---
title: "ModelDoc::CreateTangentArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateTangentArc2.htm"
---

# ModelDoc::CreateTangentArc2

This
method is obsolete and has been superseded by[ModelDoc2::CreateTangentArc2](../ModelDoc2/ModelDoc2__CreateTangentArc2.htm).

Description

This method creates an arc that is tangent
to the entity that shares it start point. The input start point must be
an existing point in the sketch and be the endpoint of another sketch
entity.

Syntax (OLE Automation)

retval = ModelDoc.CreateTangentArc2 ( p1x, p1y, p1z,
p2x, p2y, p2z, arcType )

(Table)=========================================================

| Input: | (double) p1x | Start point x |
| --- | --- | --- |
| Input: | (double) p1y | Start point y |
| Input: | (double) p1z | Start point z |
| Input: | (double) p2x | End point x |
| Input: | (double) p2y | End point y |
| Input: | (double) p2z | End point z |
| Input: | (long) arcType | Type of tangent arc as defined in swTangentArcTypes_e |
| Return: | (BOOL) retval | True for success |

Syntax (COM)

status = ModelDoc->CreateTangentArc2 ( p1x, p1y,
p1z, p2x, p2y, p2z, arcType, &retval )

(Table)=========================================================

| Input: | (double) p1x | Start point x |
| --- | --- | --- |
| Input: | (double) p1y | Start point y |
| Input: | (double) p1z | Start point z |
| Input: | (double) p2x | End point x |
| Input: | (double) p2y | End point y |
| Input: | (double) p2z | End point z |
| Input: | (long) arcType | Type of tangent arc as defined in swTangentArcTypes_e |
| Output: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The arcType argument refers to the direction that
the tangent takes off from the other sketch entity.

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateTangentArc2.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateTangentArc2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

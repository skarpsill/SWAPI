---
title: "ModelDoc::CreatePlaneAtAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtAngle.htm"
---

# ModelDoc::CreatePlaneAtAngle

This method is obsolete
and has been superseded by[ModelDoc::CreatePlaneAtAngle2](ModelDoc__CreatePlaneAtAngle2.htm).

Description

This method creates a construction (reference) plane at an angle from
the selected plane along the selected edge.

Syntax (OLE Automation)

void ModelDoc.CreatePlaneAtAngle (
val, flipDir)

(Table)=========================================================

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction away from the first direction |

Syntax (COM)

status = ModelDoc->CreatePlaneAtAngle
( val, flipDir )

(Table)=========================================================

| Input: | (double) val | Angle from the selected plane in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction away from the first direction |
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePlaneAtAngle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

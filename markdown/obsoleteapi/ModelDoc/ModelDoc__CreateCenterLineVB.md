---
title: "ModelDoc::CreateCenterLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCenterLineVB.htm"
---

# ModelDoc::CreateCenterLineVB

This
method is obsolete and has been superseded by[ModelDoc2::CreateCenterLineVB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCenterLineVB.htm).

Description

This method creates a center line from P1 to P2 and may be used in Visual
Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

void ModelDoc.CreateCenterLineVB (
x1, y1, z1, x2, y2, z2)

(Table)=========================================================

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |

Syntax (COM)

status = ModelDoc->CreateCenterLineVB
( x1, y1, z1, x2, y2, z2 )

(Table)=========================================================

| Input: | (double) x1 | Location of first end point, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Location of first end point, in meters |
| Input: | (double) z1 | Location of first end point, in meters |
| Input: | (double) x2 | Location of second end point, in meters |
| Input: | (double) y2 | Location of second end point, in meters |
| Input: | (double) z2 | Location of second end point, in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also create centerline construction geometry
using ModelDoc::CreateLine2 and SketchSegment::ConstructionGeometry.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateCenterLineVB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "ModelDoc2::CreateEllipticalArcByCenter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateEllipticalArcByCenter.htm"
---

# ModelDoc2::CreateEllipticalArcByCenter

This
method is obsolete and has been superseded by SketchManager::CreateEllipticalArc .

Description

This method creates an elliptical arc trimmed between two points.

Syntax (OLE Automation)

retval = ModelDoc2.CreateEllipticalArcByCenter
( center, major, minor, start, end)

(Table)=========================================================

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
the ellipse center |
| --- | --- | --- |
| Input: | (VARIANT) major | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
a point on the ellipse and on the major axis |
| Input: | (VARIANT) minor | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis |
| Input: | (VARIANT) start | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
the start point of the ellipse |
| Input: | (VARIANT) end | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
the end point of the ellipse |
| Return: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax
(COM)

status = ModelDoc2->ICreateEllipticalArcByCenter
( center, major, minor, start, end )

(Table)=========================================================

| Input: | (double*) center | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
the ellipse center |
| --- | --- | --- |
| Input: | (double*) major | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the major axis |
| Input: | (double*) minor | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis |
| Input: | (double*) start | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
the CCW start point of the ellipse |
| Input: | (double*) end | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
the CCW end point of the ellipse |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Thestartandendarguments should be specified in a Counter-Clockwise manner.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateEllipticalArcByCenter.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateEllipticalArcByCenter.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

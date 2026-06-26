---
title: "ModelDoc2::CreateArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateArc.htm"
---

# ModelDoc2::CreateArc

This
method is obsolete and has been superseded by[ModelDoc2::CreateArc2](ModelDoc2__CreateArc2.htm).

Description

This function creates an arc from P1 as center, from P2 to P3. You can
use ModelDoc2::CreateArcVB in Visual Basic and other forms of Basic that
do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc2.CreateArc ( P1,
P2, P3, dir)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
the center point of the arc |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 double s(x2, y2, z2) in meters that describe
the first point of the arc |
| Input: | (VARIANT) P3 | VARIANT of type SafeArrayof 3 doubles(x2, y2, z2) in meters that describe
the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (VARIANT_BOOL) retval | TRUE
if success, FALSE if fail |

Syntax
(COM)

status = ModelDoc2->ICreateArc (
P1, P2, P3, dir )

(Table)=========================================================

| Input: | (double) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
the center point of the arc |
| --- | --- | --- |
| Input: | (double) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe
the first point of the arc |
| Input: | (double) P3 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe
the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method enables automatic relations for the arc that may not be
suitable for creating very small arcs in database.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateArc.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateArc.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

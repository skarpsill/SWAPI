---
title: "ModelDoc::CreateArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateArc.htm"
---

# ModelDoc::CreateArc

This
method is obsolete and has been superseded by[ModelDoc::CreateArc2](ModelDoc__CreateArc2.htm).

Description

This method creates an arc from P1 as center, from P2 to P3. You can
use ModelDoc::CreateArcVB in Visual Basic and other forms of Basic that
do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc.CreateArc ( P1, P2,
P3, dir)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
the center point of the arc |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles(x2, y2, z2) in meters that describe
the first point of the arc |
| Input: | (VARIANT) P3 | VARIANT of type SafeArray of 3 doubles(x2, y2, z2) in meters that describe
the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (BOOL) retval | TRUE
if successful, FALSE if not |

Syntax
(COM)

status = ModelDoc->ICreateArc (
P1, P2, P3, dir )

(Table)=========================================================

| Input: | (double) P1 | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe
the center point of the arc |
| --- | --- | --- |
| Input: | (double) P2 | VARIANT of type SafeArray of 3 doubles(x2, y2, z2) in meters that describe
the first point of the arc |
| Input: | (double) P3 | VARIANT of type SafeArray of 3 doubles(x2, y2, z2) in meters that describe
the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method enables automatic relations for an arc, which may not be
suitable for creating very small arcs in database.

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
<param name=_CURRENTFILEPATH value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__CreateArc.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan

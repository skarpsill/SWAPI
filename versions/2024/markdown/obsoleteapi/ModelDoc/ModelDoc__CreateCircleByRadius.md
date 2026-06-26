---
title: "ModelDoc::CreateCircleByRadius"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircleByRadius.htm"
---

# ModelDoc::CreateCircleByRadius

This
method is obsolete and has been superseded by[ModelDoc::CreateCircleByRadius2](ModelDoc__CreateCircleByRadius2.htm).

Description

This method creates a circle with P1 as the center point and with radius
as the radius.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircleByRadius
( P1, radius)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1,y1, z1) in meters that describe
the center point of the arc |
| --- | --- | --- |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc->ICreateCircleByRadius
( P1, radius )

(Table)=========================================================

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1,y1, z1) in meters that describe
the center point of the arc. |
| --- | --- | --- |
| Input: | (double) radius | Radius of circle in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

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
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateCircleByRadius.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan

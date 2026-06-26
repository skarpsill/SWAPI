---
title: "ModelDoc::CreateEllipse"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipse.htm"
---

# ModelDoc::CreateEllipse

This
method is obsolete and has been superseded by[ModelDoc::CreateEllipse2](ModelDoc__CreateEllipse2.htm).

Description

This method creates an ellipse.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipse ( center,
major, minor)

(Table)=========================================================

| Input: | (VARIANT) center | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis. |
| --- | --- | --- |
| Input: | (VARIANT) major | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the major axis |
| Input: | (VARIANT) minor | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->ICreateEllipse
( center, major, minor )

(Table)=========================================================

| Input: | (double*) center | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis. |
| --- | --- | --- |
| Input: | (double*) major | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the major axis |
| Input: | (double*) minor | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
a point on the ellipse and on the minor axis |
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
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateEllipse.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan

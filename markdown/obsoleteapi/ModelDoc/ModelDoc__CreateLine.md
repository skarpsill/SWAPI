---
title: "ModelDoc::CreateLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLine.htm"
---

# ModelDoc::CreateLine

This
method is obsolete and has been superseded by[ModelDoc::CreateLine2](ModelDoc__CreateLine2.htm).

Description

This method creates a line from P1 to P2.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}It
also enables automatic relations for the line,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}which
may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

retval = ModelDoc.CreateLine ( P1,
P2)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1,
z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe
the second point of the line |
| Return: | (BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc->ICreateLine (
P1, P2 )

(Table)=========================================================

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe
the first point of the line |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x2, y2, z2) in meters that describe
the second point of the line |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The ModelDoc::SetAddToDB method increases performance during entity
creation by adding entities directly to the SolidWorks database, and it
also avoids inferencing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1217" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="" >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateLine.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan

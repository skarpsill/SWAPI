---
title: "DrawingDoc::AddCenterMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddCenterMark.htm"
---

# DrawingDoc::AddCenterMark

This method is obsolete and has been superseded by[DrawingDoc::InsertCenterMark](DrawingDoc__InsertCenterMark.htm).

Description

This
method creates a center mark from the last edge selection.

Syntax (OLE Automation)

retval
= DrawingDoc.AddCenterMark ( cmSize, cmShowLines)

(Table)=========================================================

| Input: | (double)
cmSize | Centermark
size; this is half the size of the + at the circle center; it is also
the distance that the centermark lines overshoot the circle if cmShowLines
is set to TRUE |
| --- | --- | --- |
| Input: | (BOOL)
cmShowLines | TRUE
if you want to display the centermark lines, FALSE if you want only the
+ to appear at the circle center |
| Return: | (BOOL)
retval | TRUE
if successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->AddCenterMark
( cmSize, cmShowLines, &retval )

(Table)=========================================================

| Input: | (double) cmSize | Centermark size; this is half the size of the + at the circle center;
it is also the distance that the centermark lines overshoot the circle
if cmShowLines is set to TRUE |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) cmShowLines | TRUE if you want to display the centermark lines, FALSE if you want
only the + to appear at the circle center |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name=_Version value="65536" >
<param name=_ExtentX value="1217" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="DrawingDoc_Object$$**$$DrawingDoc::CenterMark$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="D:\sw2003\DrawingDoc\DrawingDoc__AddCenterMark.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspanRemarks

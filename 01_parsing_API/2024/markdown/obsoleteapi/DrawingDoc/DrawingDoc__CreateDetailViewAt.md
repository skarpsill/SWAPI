---
title: "DrawingDoc::CreateDetailViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDetailViewAt.htm"
---

# DrawingDoc::CreateDetailViewAt

This
method is obsolete and has been superseded by[DrawingDoc::CreateDetailViewAt2](DrawingDoc__CreateDetailViewAt2.htm).

Description

This method creates a detail view at the specified location in sheet
space based on the selected closed contour.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateDetailViewAt ( x, y, z )

(Table)=========================================================

| Input: | (double)
x | x
location |
| --- | --- | --- |
| Input: | (double)
y | y
location |
| Input: | (double)
z | z
location |
| Return: | (BOOL)
retval | TRUE
if successfully created, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateDetailViewAt
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | x location |
| --- | --- | --- |
| Input: | (double) y | y location |
| Input: | (double) z | z location |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDwgView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__CreateDetailViewAt.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

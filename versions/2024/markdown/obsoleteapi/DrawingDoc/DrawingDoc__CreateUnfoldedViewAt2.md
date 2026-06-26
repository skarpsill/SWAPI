---
title: "DrawingDoc::CreateUnfoldedViewAt2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt2.htm"
---

# DrawingDoc::CreateUnfoldedViewAt2

This method is obsolete and has been superseded
by[DrawingDoc::CreateUnfoldedViewAt3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt3.htm).

Description

This
method creates an unfolded drawing view from the selected drawing view
and places it in the drawing at the specified location.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateUnfoldedViewAt2 ( x, y, z, notAligned )

(Table)=========================================================

| Input: | (double)
x | X
position in the drawing sheet space for the center of the drawing view |
| --- | --- | --- |
| Input: | (double)
y | Y
position in the drawing sheet space for the center of the drawing view |
| Input: | (double)
z | Z
position in the drawing sheet space for the center of the drawing view |
| Input: | (BOOL)
notAligned | TRUE
if you want to break the alignment with the parent view, FALSE if you
want to keep the view aligned with the parent view |
| Return: | (BOOL)
retval | TRUE
if successful |

Syntax (COM)

status
= DrawingDoc->CreateUnfoldedViewAt2 ( x, y, z, notAligned, &retval
)

(Table)=========================================================

| Input: | (double)
x | X
position in the drawing sheet space for the center of the drawing view |
| --- | --- | --- |
| Input: | (double)
y | Y
position in the drawing sheet space for the center of the drawing view |
| Input: | (double)
z | Z
position in the drawing sheet space for the center of the drawing view |
| Input: | (VARIANT_BOOL)
notAligned | TRUE
if you want to break the alignment with the parent view, FALSE if you
want to keep the view aligned with the parent view |
| Output: | (VARIANT_BOOL)
retval | TRUE
if successful |
| Return: | (HRESULT)
status | S_OK
if successful |

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDwgView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateUnfoldedViewAt2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

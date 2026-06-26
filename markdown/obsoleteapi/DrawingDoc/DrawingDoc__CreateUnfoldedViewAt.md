---
title: "DrawingDoc::CreateUnfoldedViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateUnfoldedViewAt.htm"
---

# DrawingDoc::CreateUnfoldedViewAt

This
method is obsolete and has been superseded by[DrawingDoc::CreateUnfoldedViewAt2](DrawingDoc__CreateUnfoldedViewAt2.htm).

Description

This
method uses the selected drawing view to create a unfolded drawing view
and places it in the drawing at the location specified.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateUnfoldedViewAt ( x, y, z)

(Table)=========================================================

| Input: | (double)
x | X
location of the unfolded drawing view in meters |
| --- | --- | --- |
| Input: | (double)
y | Y
location of the unfolded drawing view in meters |
| Input: | (double)
z | Z
location of the unfolded drawing view in meters |
| Return: | (BOOL)
retval | TRUE
if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateUnfoldedViewAt
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | X location of the unfolded drawing view in meters |
| --- | --- | --- |
| Input: | (double) y | Y location of the unfolded
drawing view in meters |
| Input: | (double) z | Z location of the unfolded
drawing view in meters |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateUnfoldedViewAt.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

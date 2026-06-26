---
title: "DrawingDoc::CreateAuxiliaryViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateAuxiliaryViewAt.htm"
---

# DrawingDoc::CreateAuxiliaryViewAt

This
method is obsolete and has been superseded by DrawingDoc::CreateAuxiliaryViewAt2 .

Description

This method creates an auxiliary view at the specified location in sheet
space.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateAuxiliaryViewAt ( x, y, z, notAligned )

(Table)=========================================================

| Input: | (double)
x | X
location |
| --- | --- | --- |
| Input: | (double)
y | Y
location |
| Input: | (double)
z | Z
location |
| Input: | (BOOL)
notAligned | TRUE
aligns the view from its owner, FALSE does not |
| Return: | (BOOL)
retval | TRUE
if successfully created, FALSE if not |

Syntax
(COM)

status = DrawingDoc->CreateAuxiliaryViewAt
( x, y, z, notAligned, &retval )

(Table)=========================================================

| Input: | (double) x | X location |
| --- | --- | --- |
| Input: | (double) y | Y location |
| Input: | (double) z | Z location |
| Input: | (VARIANT_BOOL) notAligned | TRUE aligns the view from its
owner, FALSE does not |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__CreateAuxiliaryViewAt.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

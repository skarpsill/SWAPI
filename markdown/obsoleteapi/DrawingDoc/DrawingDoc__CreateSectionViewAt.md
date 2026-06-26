---
title: "DrawingDoc::CreateSectionViewAt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateSectionViewAt.htm"
---

# DrawingDoc::CreateSectionViewAt

This
method is obsolete and has been superseded byDrawingDoc::CreateSectionViewAt2 .

Description

This method creates a new section view at the specified location on
the drawing.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateSectionViewAt ( x, y, z, notAligned, isOffsetSection
)

(Table)=========================================================

| Input: | (double)
x | X
position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double)
y | Y
position on the drawing sheet for the center of the drawing view |
| Input: | (double)
z | Z
position on the drawing sheet for the center of the drawing view |
| Input: | (BOOL)
notAligned | TRUE
breaks the alignment from the parent view, FALSE snaps into alignment
with the parent view |
| Input: | (BOOL)
isOffsetSection | TRUE
creates an aligned section (two lines at an angle), FALSE creates a normal
projection section view |
| Return: | (BOOL)
retval | TRUE
if successful |

Syntax (COM)

status = DrawingDoc->CreateSectionViewAt
( x, y, z, notAligned, isOffsetSection, &retval )

(Table)=========================================================

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment
with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section (two lines at an angle), FALSE creates
a normal projection section view |
| Output: | (VARIANT_BOOL) retval | TRUE if successful |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__CreateSectionViewAt.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

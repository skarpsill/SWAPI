---
title: "DrawingDoc::CreateSectionViewAt2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateSectionViewAt2.htm"
---

# DrawingDoc::CreateSectionViewAt2

This method is obsolete and has been superseded
by[DrawingDoc::CreateSectionViewAt3](DrawingDoc__CreateSectionViewAt3.htm).

Description

This method creates a new section view at a
given location on the drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateSectionViewAt2 ( x, y,
z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial,
dispsurfcut )

(Table)=========================================================

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment
with the parent view |
| Input: | (BOOL) isOffsetSection | TRUE creates an aligned section (two lines at an angle), FALSE creates
a normal projection section view |
| Input: | (BSTR) label | String value containing the label name of this section view |
| Input: | (BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (BOOL) switchmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (BOOL) dispsurfcut | TRUE displays only the surface cut, FALSE does not |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created View object |

Syntax (COM)

status = DrawingDoc->ICreateSectionViewAt2 ( x,
y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial,
dispsurfcut, &retval )

(Table)=========================================================

| Input: | (double) x | X position on the drawing sheet for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from the parent view, FALSE snaps into alignment
with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section (two lines at an angle), FALSE creates
a normal projection section view |
| Input: | (BSTR) label | String value containing the label name of this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of this section view, FALSE does not |
| Input: | (VARIANT_BOOL) switchmodel | TRUE scales the section view with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE displays only the surface cut, FALSE does not |
| Output: | (LPVIEW) retval | Point to the newly View object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateSectionViewAt2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanThis method runs silently; the end-user is not prompted for label. Then
use View::GetSection to get the DrSection object, and use DrSection::SetLabel2
to set the label, which provides a warning if the name is a duplicate
and the standard does not accept duplicate names.

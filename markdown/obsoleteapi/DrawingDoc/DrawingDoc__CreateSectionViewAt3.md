---
title: "DrawingDoc::CreateSectionViewAt3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateSectionViewAt3.htm"
---

# DrawingDoc::CreateSectionViewAt3

This method is obsolete and has been superseded
by[DrawingDoc::CreateSectionView4](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateSectionViewAt4.htm).

Description

This method creates a section
view at the specified location on the drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateSectionViewAt3 ( x, y,
z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial,
dispsurfcut, excludedComponents)

(Table)=========================================================

| Input: | (double) x | X position on the drawing sheet
for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet
for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet
for the center of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from
the parent view, FALSE snaps into alignment with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section
view (two lines at an angle), FALSE creates a normal projection section
view |
| Input: | (BSTR) label | String containing the letter
for the label for this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of
this section view, FALSE does not |
| Input: | (VARIANT_BOOL) scwithmodel | TRUE scales the section view
with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section
view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE if only the surfaces cut
by the section line are to appear in the section view, FALSE if not |
| Input: | (VARIANT) excludedComponents | Array of components to exclude
from section view |
| Output: | (LPDISPATCH) retval | Pointer to a Dispatch object,
the newly created View object |

Syntax (COM)

status = DrawingDoc->ICreateSectionViewAt3 ( x,
y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial,
dispsurfcut, numExcludedComponents, pExcludedComponents, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (double) x | X position on the drawing sheet
for the center of the drawing view |
| --- | --- | --- |
| Input: | (double) y | Y position on the drawing sheet
for the center of the drawing view |
| Input: | (double) z | Z position on the drawing sheet for the center
of the drawing view |
| Input: | (VARIANT_BOOL) notAligned | TRUE breaks the alignment from
the parent view, FALSE snaps into alignment with the parent view |
| Input: | (VARIANT_BOOL) isOffsetSection | TRUE creates an aligned section view (two lines
at an angle), FALSE creates a normal projection section view |
| Input: | (BSTR) label | String containing the letter for the label
for this section view |
| Input: | (VARIANT_BOOL) chgdirection | TRUE changes the direction of
this section view, FALSE does not |
| Input: | (VARIANT_BOOL) scwithmodel | TRUE scales the section view
with the model, FALSE does not |
| Input: | (VARIANT_BOOL) partial | TRUE displays a partial section
view, FALSE does not |
| Input: | (VARIANT_BOOL) dispsurfcut | TRUE if only the surfaces cut
by the section line are to appear in the section view, FALSE if not |
| Input: | (long) numExcludedComponents | Number of excluded components
in this section view |
| Input: | (LPDISPATCH) pExcludedComponents | Array of components to exclude from section view |
| Output: | (LPVIEW) retval | Pointer the newly created View
object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Select the section line or the lines to use as
a section line before calling this method.

This method runs silently; the end-user is not
prompted for a label.

Use View::GetSection to get the DrSection object,
and use DrSection::SetLabel2 to set the name for the label, which provides
a warning if the name is a duplicate and the standard does not accept
duplicate names.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateSectionViewAt3.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateSectionViewAt3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXCreateSectionViewAtLocation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateSectionViewAt3.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

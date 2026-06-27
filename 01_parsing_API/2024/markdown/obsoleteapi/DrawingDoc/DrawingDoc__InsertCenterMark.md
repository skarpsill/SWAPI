---
title: "DrawingDoc::InsertCenterMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCenterMark.htm"
---

# DrawingDoc::InsertCenterMark

This method is obsolete and has been superseded
byDrawingDoc::InsertCenterMark2.

Description

This method creates a center mark from the
last edge selection.

Syntax (OLE Automation)

retval = DrawingDoc.InsertCenterMark ( UseDoc, Size,
ShowLines, Angle )

(Table)=========================================================

| Input: | (BOOL) UseDoc | TRUE uses the document defaults for center mark display attributes,
FALSE uses the values specified in the Size and ShowLines arguments |
| --- | --- | --- |
| Input: | (double) Size | Center mark size in meters; half the size of the plus sign (+) at the
circle center |
| Input: | (BOOL) ShowLines | TRUE displays the center mark lines, FALSE displays only the plus sign
(+) at the circle center |
| Input: | (double) Angle | Angle that the center mark is rotated in radians |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the new center mark |

Syntax (COM)

status = DrawingDoc->InsertCenterMark ( UseDoc,
Size, ShowLines, Angle, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) UseDoc | TRUE uses the document defaults for center mark display attributes,
FALSE uses the values specified in the Size and ShowLines arguments |
| --- | --- | --- |
| Input: | (double) Size | Center mark size in meters; half the size of the plus sign (+) at
the circle center |
| Input: | (VARIANT_BOOL) ShowLines | TRUE displays the center mark lines, FALSE displays only the plus sign
(+) at the circle center |
| Input: | (double) Angle | Angle that the center mark is rotated in radians |
| Output: | (LPCENTERMARK) retval | Pointer to the new center mark |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

In addition to Size being half the size of the
plus sign (+) at the circle center, it is also the distance that the center
mark lines overshoot the circle if ShowLines is TRUE.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__InsertCenterMark.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__InsertCenterMark.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

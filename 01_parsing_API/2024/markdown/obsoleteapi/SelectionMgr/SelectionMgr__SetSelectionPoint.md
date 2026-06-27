---
title: "SelectionMgr::SetSelectionPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__SetSelectionPoint.htm"
---

# SelectionMgr::SetSelectionPoint

This method is obsolete and has been superseded
by[SelectionMgr::SetSelectionPoint2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__SetSelectionPoint2.htm).

Description

This method sets the selection
point in model space.

Syntax (OLE Automation)

retval = SelectionMgr.SetSelectionPoint ( AtIndex,
x, y, z )

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount. |
| --- | --- | --- |
| Input: | (double) x | x location of the selection point |
| Input: | (double) y | y location of the selection point |
| Input: | (double) z | z location of the selection point |
| Output: | (VARIANT_BOOL) retval | TRUE if the position of the selection point is set, FALSE if not |

Syntax (COM)

status = SelectionMgr->SetSelectionPoint ( AtIndex,
x, y, z, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex
ranges from 1 to SelectionMgr::GetSelectedObjectCount. |
| --- | --- | --- |
| Input: | (double) x | x location of the selection point |
| Input: | (double) y | y location of the selection point |
| Input: | (double) z | z location of the selection point |
| Output: | (VARIANT_BOOL) retval | TRUE if the position of the selection point is set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method allows an application
to provide an XYZ position to a selected object at the given index in
the SelectionMgr. This XYZ position represents a world-coordinate location
in the context of that SelectionMgr.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__SetSelectionPoint.htm" >
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
<param name="Items" value="SelectionMgr_Object$$**$$SelectionMgr::GetSelectionPoint$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__SetSelectionPoint.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

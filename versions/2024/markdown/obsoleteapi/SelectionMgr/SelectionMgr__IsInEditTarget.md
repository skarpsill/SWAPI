---
title: "SelectionMgr::IsInEditTarget"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__IsInEditTarget.htm"
---

# SelectionMgr::IsInEditTarget

This method is obsolete and has been superseded
by[SelectionMgr::IsInEditTarget2](sldworksAPI.chm::/SelectionMgr/SelectionMgr__IsInEditTarget2.htm).

Description

This method determines if the selected object is in the edit target.
This is necessary in assemblies when the end-user performs in-context
editing of a part. This method allows you to determine if a selected item
belongs to the model that is the current edit target.

Syntax (OLE Automation)

retval = SelectionMgr.IsInEditTarget
( atIndex)

(Table)=========================================================

| Input: | (long) atIndex | Position within the current list of selected items where AtIndex ranges
from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the selected item specified by AtIndex belongs to a model which
is the current edit target, FALSE if not |

Syntax (COM)

status = SelectionMgr->IsInEditTarget
( atIndex, &retval )

(Table)=========================================================

| Input: | (long) atIndex | Position within the current list of selected items where AtIndex ranges
from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the selected item specified by AtIndex belongs to a model which
is the current edit target, FALSE if not |
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__IsInEditTarget.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

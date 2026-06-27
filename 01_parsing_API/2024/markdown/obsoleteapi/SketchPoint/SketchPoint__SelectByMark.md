---
title: "SketchPoint::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__SelectByMark.htm"
---

# SketchPoint::SelectByMark

This
method is obsolete and has been superseded by SketchPoint::Select2 .

Description

This method selects the SketchPoint object
and appends it to the current set of selections or replaces the entire
selection list. The selection is also marked with the value specified.
This mark is used by certain API functions that require multiple selections.

Syntax (OLE Automation)

retval = SketchPoint.SelectByMark (appendFlag, markValue)

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE if you want to append this item to the current
selection list, FALSE if you want this item to replace the current selection
list |
| --- | --- | --- |
| Input: | (long) markValue | Number you want to use as a mark; this number
is used by certain API functions that require ordered entity selection |
| Return: | (BOOL) retval | TRUE if successfully selected, FALSE if not |

Syntax (COM)

status = SketchPoint->SelectByMark (appendFlag, markValue, &retval)

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE if you want to append this item to the current
selection list, FALSE if you want this item to replace the current selection
list |
| --- | --- | --- |
| Input: | (long) markValue | Number you want to use as a mark; this number
is used by certain API functions that require ordered entity selection |
| Output: | (BOOL) retval | TRUE if successfully selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByMark instead of using this
method. This method does not work well when a PropertyManager page is
open or a command is running. ModelDoc2::SelectByMark handles selection
correctly whether or not a command is running.

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
<param name="Items" value="SketchPoint_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SketchPoint\SketchPoint__SelectByMark.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

---
title: "Component2::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SelectByMark.htm"
---

# Component2::SelectByMark

This method is obsolete and has been superseded
by[Component2::Select2](Component2__Select2.htm).

Description

This method selects the component and either appends it to the selection
list or replaces the entire selection list. The selection is also marked
with the value specified. This mark is used by certain API functions that
require multiple selections.

Syntax (OLE Automation)

retval = Component.SelectByMark ( appendFlag, mark
)

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE appends the selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if not |

Syntax (COM)

status = Component->SelectByMark ( appendFlag,
mark, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the selection list, FALSE replaces the selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you wish to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The mark value is used by certain API functions
that require ordered entity selection.

Use ModelDoc2::SelectByMark instead of using this
method. This method does not work well when a PropertyManager page is
open or a command is running. ModelDoc2::SelectByMark handles selection
correctly whether or not a command is running.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Component2\Component2__SelectByMark.htm" >
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
<param name="Items" value="Component2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Component2\Component2__SelectByMark.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

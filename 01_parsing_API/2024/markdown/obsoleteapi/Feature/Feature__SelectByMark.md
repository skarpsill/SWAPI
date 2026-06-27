---
title: "Feature::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__SelectByMark.htm"
---

# Feature::SelectByMark

This
method is obsolete and has been superseded by Feature::Select2 .

Description

This method selects and marks this feature.

Syntax (OLE Automation)

retval = Feature.SelectByMark ( appendFlag, mark
)

(Table)=========================================================

| Input: | (BOOL) appendFlag | TRUE appends the feature to the selection list, FALSE replaces the current
selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Return: | (BOOL) retval | TRUE if the feature was selected, FALSE if not |

Syntax (COM)

status = Feature->SelectByMark ( appendFlag, mark,
&retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) appendFlag | TRUE appends the feature to the selection list, FALSE replaces the current
selection list |
| --- | --- | --- |
| Input: | (long) mark | Number you want to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selection mark is used by other functions that
require multiple selections, such as InsertMfDraft2, InsertSplitLineSil,
and InsertSplitLineProject.

Use[ModelDoc2::SelectByMark](../ModelDoc2/ModelDoc2__SelectByMark.htm)instead of this method. This method does not work well when a PropertyManager
page is open or a command is running. ModelDoc2::SelectByMark handles
selection correctly whether or not a command is running.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\Feature\Feature__SelectByMark.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Feature_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\Feature\Feature__SelectByMark.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

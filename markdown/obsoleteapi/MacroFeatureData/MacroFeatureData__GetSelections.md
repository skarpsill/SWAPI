---
title: "MacroFeatureData::GetSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__GetSelections.htm"
---

# MacroFeatureData::GetSelections

This
method is obsolete and has been superseded by[MacroFeatureData::GetSelections2](MacroFeatureData__GetSelections2.htm).

Description

This method gets the selected objects for this
macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.GetSelections ( objects,
objectTypes, selMarks )

(Table)=========================================================

| Output: | (VARIANT) *objects | Array of selected object names |
| --- | --- | --- |
| Output: | (VARIANT) *objectTypes | Array of object types of the selections as defined in swSelectType_e |
| Output: | (VARIANT) *selMarks | Array of marks associated with the selections |

Syntax (COM)

status = MacroFeatureData->IGetSelections ( selCount,
objects, objectTypes, selMarks )

(Table)=========================================================

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Output: | (LPDISPATCH) *objects | Array of size selCount containing selected
object names |
| Output: | (long) *objectTypes | Array of size selCount containing object types
of the selections as defined in swSelectType_e |
| Output: | (long) *selMarks | Array of size selCount containing marks associated
with the selections |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\MacroFeatureData\MacroFeatureData__GetSelections.htm" >
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
<param name="Items" value="MacroFeatureData Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\MacroFeatureData\MacroFeatureData__GetSelections.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

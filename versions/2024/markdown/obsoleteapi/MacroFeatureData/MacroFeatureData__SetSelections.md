---
title: "MacroFeatureData::SetSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__SetSelections.htm"
---

# MacroFeatureData::SetSelections

This
method is obsolete and has been superseded by[MacroFeatureData::SetSelections2](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__SetSelections2.htm).

Description

This method sets the selected objects for the
macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.SetSelections ( objects,
selMarks )

(Table)=========================================================

| Input: | (VARIANT) objects | Array of object names |
| --- | --- | --- |
| Input: | (VARIANT) selMarks | Array of marks associated with the objects |

Syntax (COM)

status = MacroFeatureData->ISetSelections ( selCount,
objects, selMarks )

Parameters Table Start

(Table)=========================================================

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Input: | (LPDISPATCH*) objects | Array of size selCount containing the object
names |
| Input: | (long) *selMarks | Array of size selCount containing the marks
associated with the objects |
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\MacroFeatureData\MacroFeatureData__SetSelections.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\MacroFeatureData\MacroFeatureData__SetSelections.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

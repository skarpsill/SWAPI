---
title: "MacroFeatureData::GetSelections2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__GetSelections2.htm"
---

# MacroFeatureData::GetSelections2

This method is obsolete and has been superseded
by[MacroFeatureData::GetSelections3](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__GetSelections3.htm).

Description

This method gets the selected objects for the
macro feature.

Syntax (OLE Automation)

void = MacroFeatureData.GetSelections2 ( objects,
objectTypes, selMarks, drViews )

(Table)=========================================================

| Output: | (VARIANT) *objects | Array of selected objects |
| --- | --- | --- |
| Output: | (VARIANT) *objectTypes | Array of selected object types as defined in swSelectType |
| Output: | (VARIANT) *selMarks | Array of marks for the selected objects |
| Output: | (VARIANT) *drViews | Array of drawing views |

Syntax (COM)

status = MacroFeatureData->IGetSelections2 ( selCount,
objects, objectTypes, selMarks, drViews )

Parameters Table Start

(Table)=========================================================

| Input: | (long) selCount | Number of selected objects |
| --- | --- | --- |
| Output: | (LPDISPATCH) *objects | Array of selected object of size selCount |
| Output: | (long) *objectTypes | Array of the selected object types as defined
in swSelectType_e of size selCount |
| Output: | (long) *selMarks | Array of marks associated with the selected objects
of size selCount |
| Output: | (LPVIEW) *drViews | Array of drawing views of size selCount |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Accessing Selections that
Define Features for details on using this method.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\MacroFeatureData\MacroFeatureData__GetSelections2.htm" >
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
<param name="Items" value="MacroFeatureData_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\MacroFeatureData\MacroFeatureData__GetSelections2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

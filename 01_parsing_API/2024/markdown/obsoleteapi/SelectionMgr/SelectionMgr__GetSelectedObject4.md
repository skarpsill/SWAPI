---
title: "SelectionMgr::GetSelectedObject4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SelectionMgr/SelectionMgr__GetSelectedObject4.htm"
---

# SelectionMgr::GetSelectedObject4

This method is obsolete and has been superseded
by[SelectionMgr::GetSelectedObject5](SelectionMgr__GetSelectedObject5.htm).

Description

This method gets the selected
object.

Syntax (kadov_tag{{<ignored>}}OLEkadov_tag{{</ignored>}}Automation)

kadov_tag{{<ignored>}}retvalkadov_tag{{</ignored>}}= SelectionMgr.GetSelectedObject4 (kadov_tag{{<ignored>}}AtIndexkadov_tag{{</ignored>}})

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | ( LPDISPATCH ) retval | Pointer to the Dispatch object as defined in swSelType_e; NULL may be
returned if type is not supported or if nothing is selected |

Syntax (kadov_tag{{<ignored>}}COMkadov_tag{{</ignored>}})

status = SelectionMgr->IGetSelectedObject4 (kadov_tag{{<ignored>}}AtIndexkadov_tag{{</ignored>}},
&kadov_tag{{<ignored>}}retvalkadov_tag{{</ignored>}})

Parameters Table Start

(Table)=========================================================

| Input: | (long) AtIndex | Index position within the current list of selected items where AtIndex ranges from 1 to SelectionMgr::GetSelectedObjectCount |
| --- | --- | --- |
| Output: | ( LPUNKNOWN ) retval | Pointer to the Dispatch object as defined in swSelType_e; NULL may be
returned if type is not supported or if nothing is selected |
| Return: | ( HRESULT )
status | S_OK if successful |

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject4.htm" >
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
<param name="Items" value="SelectionMgr_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject4.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="EXGetSelectedObject$$**$$RetrieveExtRef_Example$$**$$Selections_Example$$**$$AnnotationTraverse_Example$$**$$SectionProperties_Example$$**$$TransformSketch_Example$$**$$SelectTangentFaces_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SelectionMgr\SelectionMgr__GetSelectedObject4.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
